import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import api from '@/services/api'

export const useAuthStore = defineStore('auth', () => {
  const user = ref(null)
  const token = ref(localStorage.getItem('token'))
  const loading = ref(false)
  const error = ref(null)
  const phoneNumber = ref('')
  const phoneCodeHash = ref(null)
  const step = ref('phone') // 'phone', 'code', 'authenticated'

  const isAuthenticated = computed(() => !!token.value && !!user.value)

  async function requestCode(phone) {
    loading.value = true
    error.value = null
    try {
      phoneNumber.value = phone
      const response = await api.post('/auth/request-code', { phone_number: phone })
      phoneCodeHash.value = response.data.phone_code_hash
      step.value = 'code'
      return response.data
    } catch (err) {
      error.value = err.response?.data?.detail || 'Failed to request code'
      throw error.value
    } finally {
      loading.value = false
    }
  }

  async function login(code) {
    loading.value = true
    error.value = null
    try {
      const response = await api.post('/auth/login', {
        phone_number: phoneNumber.value,
        code: code,
      })
      token.value = response.data.access_token
      user.value = {
        id: response.data.user_id,
        first_name: response.data.first_name,
      }
      localStorage.setItem('token', token.value)
      localStorage.setItem('user', JSON.stringify(user.value))
      step.value = 'authenticated'
      return response.data
    } catch (err) {
      error.value = err.response?.data?.detail || 'Login failed'
      throw error.value
    } finally {
      loading.value = false
    }
  }

  async function logout() {
    try {
      await api.post('/auth/logout')
    } catch (err) {
      console.error('Logout error:', err)
    } finally {
      token.value = null
      user.value = null
      phoneNumber.value = ''
      phoneCodeHash.value = null
      step.value = 'phone'
      localStorage.removeItem('token')
      localStorage.removeItem('user')
    }
  }

  return {
    user,
    token,
    loading,
    error,
    phoneNumber,
    phoneCodeHash,
    step,
    isAuthenticated,
    requestCode,
    login,
    logout,
  }
})
