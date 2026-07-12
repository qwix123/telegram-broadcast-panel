<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-900 via-blue-900 to-slate-900">
    <!-- Navbar -->
    <nav class="bg-slate-900 border-b border-slate-700 sticky top-0 z-20">
      <div class="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 bg-gradient-to-br from-blue-500 to-blue-600 rounded-lg flex items-center justify-center">
            <Smartphone class="w-6 h-6 text-white" />
          </div>
          <h1 class="text-2xl font-bold text-white">Telegram Panel</h1>
        </div>
        <button
          @click="handleLogout"
          class="flex items-center gap-2 px-4 py-2 bg-red-600 hover:bg-red-700 text-white rounded-lg transition"
        >
          <LogOut class="w-4 h-4" />
          Выход
        </button>
      </div>
    </nav>

    <div class="max-w-7xl mx-auto">
      <div class="grid grid-cols-1 lg:grid-cols-4 gap-6 p-6">
        <!-- Sidebar -->
        <div class="lg:col-span-1">
          <div class="card sticky top-24">
            <nav class="sidebar-nav space-y-1">
              <RouterLink
                to="/dashboard"
                active-class="active"
                class="flex items-center gap-2"
              >
                <BarChart3 class="w-5 h-5" />
                Главная
              </RouterLink>
              <RouterLink
                to="/broadcast"
                active-class="active"
                class="flex items-center gap-2"
              >
                <Send class="w-5 h-5" />
                Рассылка
              </RouterLink>
              <RouterLink
                to="/jokes"
                active-class="active"
                class="flex items-center gap-2"
              >
                <Smile class="w-5 h-5" />
                Шутки
              </RouterLink>
              <RouterLink
                to="/chats"
                active-class="active"
                class="flex items-center gap-2"
              >
                <MessageSquare class="w-5 h-5" />
                Чаты
              </RouterLink>
              <RouterLink
                to="/folders"
                active-class="active"
                class="flex items-center gap-2"
              >
                <Folder class="w-5 h-5" />
                Папки
              </RouterLink>
              <RouterLink
                to="/proxy"
                active-class="active"
                class="flex items-center gap-2"
              >
                <Shield class="w-5 h-5" />
                Прокси
              </RouterLink>
            </nav>
          </div>
        </div>

        <!-- Main content -->
        <div class="lg:col-span-3">
          <RouterView />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { RouterView, RouterLink } from 'vue-router'
import {
  Smartphone,
  LogOut,
  BarChart3,
  Send,
  MessageSquare,
  Folder,
  Shield,
  Smile,
} from 'lucide-vue-next'

const authStore = useAuthStore()
const router = useRouter()

async function handleLogout() {
  await authStore.logout()
  router.push('/login')
}
</script>
