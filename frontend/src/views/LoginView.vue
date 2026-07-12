<template>
  <div class="min-h-screen flex items-center justify-center p-4">
    <div class="w-full max-w-md">
      <!-- Logo -->
      <div class="text-center mb-8">
        <div class="inline-flex items-center justify-center w-16 h-16 bg-gradient-to-br from-blue-500 to-blue-600 rounded-2xl mb-4">
          <Smartphone class="w-8 h-8 text-white" />
        </div>
        <h1 class="text-3xl font-bold text-white mb-2">📱 Telegram Panel</h1>
        <p class="text-slate-300">Мощная рассылка по Telegram</p>
      </div>

      <!-- Login Card -->
      <div class="card mb-6">
        <!-- Step 1: Phone -->
        <div v-if="authStore.step === 'phone'" class="space-y-4">
          <h2 class="text-xl font-bold text-white mb-6">Вход в аккаунт</h2>
          
          <div>
            <label class="block text-sm font-medium text-slate-300 mb-2">Номер телефона</label>
            <input
              v-model="phone"
              type="tel"
              placeholder="+7 (999) 123-45-67"
              class="input-field"
              @keyup.enter="handleRequestCode"
            />
          </div>

          <button
            @click="handleRequestCode"
            :disabled="authStore.loading || !phone"
            class="w-full btn-primary disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <span v-if="!authStore.loading">Получить код</span>
            <span v-else class="flex items-center justify-center gap-2">
              <div class="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
              Загрузка...
            </span>
          </button>
        </div>

        <!-- Step 2: Code -->
        <div v-else-if="authStore.step === 'code'" class="space-y-4">
          <h2 class="text-xl font-bold text-white mb-6">Подтверждение</h2>
          <p class="text-slate-300 text-sm">Код отправлен на номер {{ authStore.phoneNumber }}</p>
          
          <div>
            <label class="block text-sm font-medium text-slate-300 mb-2">Код подтверждения</label>
            <input
              v-model="code"
              type="text"
              placeholder="12345"
              maxlength="6"
              class="input-field text-center text-2xl tracking-widest"
              @keyup.enter="handleLogin"
            />
          </div>

          <button
            @click="handleLogin"
            :disabled="authStore.loading || !code"
            class="w-full btn-primary disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <span v-if="!authStore.loading">Войти</span>
            <span v-else class="flex items-center justify-center gap-2">
              <div class="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
              Вход...
            </span>
          </button>

          <button
            @click="authStore.step = 'phone'"
            class="w-full btn-secondary"
          >
            Назад
          </button>
        </div>
      </div>

      <!-- Error message -->
      <div v-if="authStore.error" class="bg-red-900 border border-red-700 text-red-100 px-4 py-3 rounded-lg text-sm">
        {{ authStore.error }}
      </div>

      <!-- Features -->
      <div class="grid grid-cols-3 gap-3 mt-8">
        <div class="text-center">
          <div class="text-2xl mb-1">📤</div>
          <p class="text-xs text-slate-300">Рассылка</p>
        </div>
        <div class="text-center">
          <div class="text-2xl mb-1">📁</div>
          <p class="text-xs text-slate-300">Папки</p>
        </div>
        <div class="text-center">
          <div class="text-2xl mb-1">🛡️</div>
          <p class="text-xs text-slate-300">Прокси</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { Smartphone } from 'lucide-vue-next'

const authStore = useAuthStore()
const router = useRouter()
const phone = ref('')
const code = ref('')

async function handleRequestCode() {
  try {
    await authStore.requestCode(phone.value)
  } catch (err) {
    console.error(err)
  }
}

async function handleLogin() {
  try {
    await authStore.login(code.value)
    router.push('/dashboard')
  } catch (err) {
    console.error(err)
  }
}
</script>
