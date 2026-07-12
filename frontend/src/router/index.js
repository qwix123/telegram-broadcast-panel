import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/LoginView.vue'),
  },
  {
    path: '/',
    component: () => import('@/views/DashboardLayout.vue'),
    meta: { requiresAuth: true },
    children: [
      {
        path: 'dashboard',
        name: 'Home',
        component: () => import('@/views/HomeView.vue'),
      },
      {
        path: 'broadcast',
        name: 'Broadcast',
        component: () => import('@/views/BroadcastView.vue'),
      },
      {
        path: 'chats',
        name: 'Chats',
        component: () => import('@/views/ChatsView.vue'),
      },
      {
        path: 'folders',
        name: 'Folders',
        component: () => import('@/views/FoldersView.vue'),
      },
      {
        path: 'proxy',
        name: 'Proxy',
        component: () => import('@/views/ProxyView.vue'),
      },
    ],
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/dashboard',
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()

  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next('/login')
  } else if (to.path === '/login' && authStore.isAuthenticated) {
    next('/dashboard')
  } else {
    next()
  }
})

export default router
