<template>
  <div class="space-y-6">
    <!-- Header -->
    <div class="card">
      <h2 class="text-3xl font-bold text-white">📤 Рассылка сообщений</h2>
      <p class="text-slate-400 mt-1">Отправляйте сообщения в избранные чаты или пересылайте</p>
    </div>

    <!-- Broadcast form -->
    <div class="card">
      <h3 class="text-xl font-bold text-white mb-6">Новая рассылка</h3>
      
      <div class="space-y-4">
        <!-- Broadcast type -->
        <div>
          <label class="block text-sm font-medium text-slate-300 mb-3">Тип рассылки</label>
          <div class="flex gap-3">
            <button
              @click="broadcastStore.broadcastType = 'favorites'"
              :class="[
                'flex-1 p-3 rounded-lg font-medium transition',
                broadcastStore.broadcastType === 'favorites'
                  ? 'bg-blue-600 text-white'
                  : 'bg-slate-700 text-slate-300 hover:bg-slate-600'
              ]"
            >
              ⭐ Из избранного
            </button>
            <button
              @click="broadcastStore.broadcastType = 'forward'"
              :class="[
                'flex-1 p-3 rounded-lg font-medium transition',
                broadcastStore.broadcastType === 'forward'
                  ? 'bg-blue-600 text-white'
                  : 'bg-slate-700 text-slate-300 hover:bg-slate-600'
              ]"
            >
              ↪️ Пересылка
            </button>
          </div>
        </div>

        <!-- Message -->
        <div>
          <label class="block text-sm font-medium text-slate-300 mb-2">Сообщение</label>
          <textarea
            v-model="broadcastStore.message"
            placeholder="Введите сообщение для рассылки..."
            rows="4"
            class="input-field resize-none"
          ></textarea>
        </div>

        <!-- Selected chats count -->
        <div class="bg-slate-700 p-3 rounded-lg">
          <p class="text-slate-300 text-sm">
            ✓ Выбрано чатов: <span class="font-bold text-blue-400">{{ broadcastStore.selectedChats.length }}</span>
          </p>
        </div>

        <!-- Send button -->
        <button
          @click="handleSendBroadcast"
          :disabled="broadcastStore.loading || !broadcastStore.message || broadcastStore.selectedChats.length === 0"
          class="w-full btn-primary disabled:opacity-50 disabled:cursor-not-allowed py-3 text-lg font-bold"
        >
          <span v-if="!broadcastStore.loading">🚀 Отправить рассылку</span>
          <span v-else class="flex items-center justify-center gap-2">
            <div class="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
            Отправляется...
          </span>
        </button>
      </div>
    </div>

    <!-- Recent broadcasts -->
    <div class="card">
      <h3 class="text-xl font-bold text-white mb-4">📊 История рассылок</h3>
      <div v-if="broadcastStore.broadcasts.length === 0" class="text-center py-8">
        <p class="text-slate-400">Рассылок еще нет</p>
      </div>
      <div v-else class="space-y-2">
        <div
          v-for="(broadcast, idx) in broadcastStore.broadcasts"
          :key="idx"
          class="bg-slate-700 p-4 rounded-lg flex items-center justify-between"
        >
          <div>
            <p class="font-medium text-white">{{ broadcast.status }}</p>
            <p class="text-sm text-slate-400">{{ broadcast.sent_count }} отправлено</p>
          </div>
          <div v-if="broadcast.failed_count > 0" class="text-red-400 text-sm">
            ❌ {{ broadcast.failed_count }} ошибок
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useBroadcastStore } from '@/stores/broadcast'

const broadcastStore = useBroadcastStore()

async function handleSendBroadcast() {
  try {
    await broadcastStore.sendBroadcast()
  } catch (err) {
    console.error(err)
  }
}
</script>
