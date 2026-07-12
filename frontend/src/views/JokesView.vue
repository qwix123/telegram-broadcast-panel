<template>
  <div class="space-y-6">
    <!-- Header -->
    <div class="card">
      <h2 class="text-3xl font-bold text-white">🎭 Random Joke Generator</h2>
      <p class="text-slate-400 mt-1">Смешные шутки от API каждый день</p>
    </div>

    <!-- Joke display -->
    <div class="card border-2 border-purple-500 bg-gradient-to-br from-slate-800 to-slate-900">
      <div class="text-center space-y-6">
        <!-- Joke type selector -->
        <div>
          <label class="block text-sm font-medium text-slate-300 mb-3">Тип шутки</label>
          <div class="flex flex-wrap gap-2 justify-center">
            <button
              v-for="type in jokeTypes"
              :key="type"
              @click="selectedJokeType = type"
              :class="[
                'px-4 py-2 rounded-lg font-medium transition',
                selectedJokeType === type
                  ? 'bg-purple-600 text-white'
                  : 'bg-slate-700 text-slate-300 hover:bg-slate-600'
              ]"
            >
              {{ typeEmoji(type) }} {{ formatType(type) }}
            </button>
          </div>
        </div>

        <!-- Joke display -->
        <div v-if="currentJoke" class="min-h-32 flex items-center justify-center p-8 bg-slate-700 rounded-xl border border-slate-600">
          <div class="text-center">
            <p class="text-3xl mb-4">😂</p>
            <p class="text-xl text-white leading-relaxed">{{ currentJoke.joke }}</p>
            <p class="text-xs text-slate-400 mt-4">{{ currentJoke.type }}</p>
          </div>
        </div>

        <div v-else class="min-h-32 flex items-center justify-center p-8 bg-slate-700 rounded-xl border border-slate-600">
          <div class="text-center">
            <div class="inline-flex items-center justify-center w-12 h-12 bg-slate-600 rounded-full mb-4">
              <div class="w-6 h-6 border-2 border-purple-500 border-t-transparent rounded-full animate-spin"></div>
            </div>
            <p class="text-slate-300">Загружаем шутку...</p>
          </div>
        </div>

        <!-- Get new joke button -->
        <button
          @click="fetchJoke"
          :disabled="loading"
          class="w-full btn-primary py-3 text-lg font-bold disabled:opacity-50 disabled:cursor-not-allowed"
        >
          <span v-if="!loading">🎲 Новая шутка</span>
          <span v-else class="flex items-center justify-center gap-2">
            <div class="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
            Загружаем...
          </span>
        </button>
      </div>
    </div>

    <!-- Share joke in broadcast -->
    <div class="card">
      <h3 class="text-xl font-bold text-white mb-4">📤 Отправить в рассылку</h3>
      <div class="space-y-3">
        <button
          @click="shareJokeToBroadcast"
          :disabled="!currentJoke || broadcastStore.selectedChats.length === 0"
          class="w-full p-3 bg-green-600 hover:bg-green-700 disabled:opacity-50 disabled:cursor-not-allowed text-white rounded-lg font-medium transition"
        >
          📨 Отправить эту шутку в {{ broadcastStore.selectedChats.length }} чатов
        </button>
        <p v-if="broadcastStore.selectedChats.length === 0" class="text-sm text-slate-400">
          ⚠️ Выберите чаты для отправки
        </p>
      </div>
    </div>

    <!-- Joke history -->
    <div class="card">
      <h3 class="text-xl font-bold text-white mb-4">📝 История шуток</h3>
      <div v-if="jokeHistory.length === 0" class="text-center py-8">
        <p class="text-slate-400">История пуста. Загрузите первую шутку!</p>
      </div>
      <div v-else class="space-y-2 max-h-64 overflow-y-auto">
        <div
          v-for="(joke, idx) in jokeHistory.slice().reverse()"
          :key="idx"
          class="bg-slate-700 p-3 rounded-lg text-sm cursor-pointer hover:bg-slate-600 transition"
          @click="currentJoke = joke"
        >
          <p class="text-slate-300 line-clamp-2">{{ joke.joke }}</p>
          <p class="text-xs text-slate-500 mt-1">{{ joke.type }}</p>
        </div>
      </div>
    </div>

    <!-- Fun facts -->
    <div class="card">
      <h3 class="text-xl font-bold text-white mb-4">🎯 Интересные факты</h3>
      <ul class="space-y-2 text-slate-300 text-sm">
        <li>✅ Смех улучшает здоровье на 21%</li>
        <li>✅ Шутки помогают снять стресс</li>
        <li>✅ Юмор способствует креативности</li>
        <li>✅ Одна хорошая шутка может изменить настроение!</li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useBroadcastStore } from '@/stores/broadcast'
import api from '@/services/api'

const broadcastStore = useBroadcastStore()
const currentJoke = ref(null)
const jokeHistory = ref([])
const loading = ref(false)
const selectedJokeType = ref('general')
const jokeTypes = ['general', 'programming', 'knock-knock']

const typeEmoji = (type) => {
  const emojis = {
    general: '😂',
    programming: '💻',
    'knock-knock': '🚪',
  }
  return emojis[type] || '😂'
}

const formatType = (type) => {
  const labels = {
    general: 'Общие',
    programming: 'Программирование',
    'knock-knock': 'Стучим-стучим',
  }
  return labels[type] || type
}

async function fetchJoke() {
  loading.value = true
  try {
    const endpoint = selectedJokeType.value === 'general' 
      ? '/jokes/random' 
      : `/jokes/by-type/${selectedJokeType.value}`
    
    const response = await api.get(endpoint)
    currentJoke.value = response.data
    
    // Add to history
    if (!jokeHistory.value.some(j => j.joke === response.data.joke)) {
      jokeHistory.value.push(response.data)
    }
  } catch (err) {
    console.error('Failed to fetch joke:', err)
    currentJoke.value = {
      joke: '😅 Не удалось загрузить шутку. Попробуйте позже!',
      type: 'error'
    }
  } finally {
    loading.value = false
  }
}

function shareJokeToBroadcast() {
  if (!currentJoke.value || broadcastStore.selectedChats.length === 0) return
  
  broadcastStore.message = `🎭 Вот вам шутка:\n\n${currentJoke.value.joke}\n\n😂 Смешно?`
}

onMounted(() => {
  fetchJoke()
})
</script>
