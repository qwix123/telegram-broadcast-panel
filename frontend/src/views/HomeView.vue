<template>
  <div class="space-y-6">
    <!-- Header -->
    <div class="card border-2 border-blue-500">
      <div class="flex items-center justify-between">
        <div>
          <h2 class="text-3xl font-bold text-white mb-1">👋 Добро пожаловать!</h2>
          <p class="text-slate-400">{{ authStore.user?.first_name }}, вы успешно вошли в систему</p>
        </div>
        <div class="text-5xl">🚀</div>
      </div>
    </div>

    <!-- Stats -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      <div class="card">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-slate-400 text-sm">Всего рассылок</p>
            <p class="text-3xl font-bold text-white mt-1">0</p>
          </div>
          <Send class="w-12 h-12 text-blue-500 opacity-20" />
        </div>
      </div>
      <div class="card">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-slate-400 text-sm">Отправлено сообщений</p>
            <p class="text-3xl font-bold text-white mt-1">0</p>
          </div>
          <MessageSquare class="w-12 h-12 text-green-500 opacity-20" />
        </div>
      </div>
      <div class="card">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-slate-400 text-sm">Активных чатов</p>
            <p class="text-3xl font-bold text-white mt-1">0</p>
          </div>
          <Folder class="w-12 h-12 text-purple-500 opacity-20" />
        </div>
      </div>
    </div>

    <!-- Quick actions -->
    <div class="card">
      <h3 class="text-xl font-bold text-white mb-4">⚡ Быстрые действия</h3>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
        <RouterLink to="/broadcast" class="p-4 bg-blue-600 hover:bg-blue-700 rounded-lg text-white font-medium transition">
          📤 Начать рассылку
        </RouterLink>
        <RouterLink to="/folders" class="p-4 bg-purple-600 hover:bg-purple-700 rounded-lg text-white font-medium transition">
          📁 Управлять папками
        </RouterLink>
        <RouterLink to="/proxy" class="p-4 bg-green-600 hover:bg-green-700 rounded-lg text-white font-medium transition">
          🛡️ Настроить прокси
        </RouterLink>
        <RouterLink to="/chats" class="p-4 bg-orange-600 hover:bg-orange-700 rounded-lg text-white font-medium transition">
          💬 Просмотреть чаты
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth'
import { RouterLink } from 'vue-router'
import { Send, MessageSquare, Folder } from 'lucide-vue-next'

const authStore = useAuthStore()
</script>
