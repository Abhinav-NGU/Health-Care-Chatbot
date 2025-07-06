import { ref } from 'vue'
import axios from 'axios'

export default function useChatbot() {
  const url = 'http://localhost:8000/api/chatbot/' // Replace with your actual chatbot API endpoint
  const messages = ref([])
  const error = ref(null)
  const loading = ref(false)

  // Send Message to the Chatbot
  const sendMessage = async (userMessage) => {
    loading.value = true
    error.value = null

    try {
      // Push user message to chat
      messages.value.push({ type: 'user', content: userMessage })

      const response = await axios.post(
        url,
        { user_message: userMessage }
      )

      // Push bot response to chat
      messages.value.push({ type: 'bot', content: response.data.bot_response })

    } catch (err) {
      error.value = 'Error: Unable to process your request.'
      messages.value.push({ type: 'bot', content: 'Error: Unable to process your request.' })
    } finally {
      loading.value = false
    }
  }

  return {
    messages,
    error,
    loading,
    sendMessage
  }
}
