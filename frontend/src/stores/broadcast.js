import { defineStore } from 'pinia'
import { ref } from 'vue'
import api from '@/services/api'

export const useBroadcastStore = defineStore('broadcast', () => {
  const broadcasts = ref([])
  const loading = ref(false)
  const error = ref(null)
  const selectedChats = ref([])
  const broadcastType = ref('favorites') // 'favorites' or 'forward'
  const message = ref('')

  async function sendBroadcast() {
    loading.value = true
    error.value = null
    try {
      const response = await api.post('/broadcast/send', {
        message: message.value,
        chat_ids: selectedChats.value,
        broadcast_type: broadcastType.value,
      })
      broadcasts.value.push(response.data)
      message.value = ''
      selectedChats.value = []
      return response.data
    } catch (err) {
      error.value = err.response?.data?.detail || 'Failed to send broadcast'
      throw error.value
    } finally {
      loading.value = false
    }
  }

  async function getHistory() {
    loading.value = true
    try {
      const response = await api.get('/broadcast/history')
      broadcasts.value = response.data.broadcasts
    } catch (err) {
      error.value = err.response?.data?.detail || 'Failed to fetch history'
    } finally {
      loading.value = false
    }
  }

  return {
    broadcasts,
    loading,
    error,
    selectedChats,
    broadcastType,
    message,
    sendBroadcast,
    getHistory,
  }
})
