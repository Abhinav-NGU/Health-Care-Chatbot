<template>
  <div class="container-fluid chat-outer" style="min-height: 100vh;">
    <div class="row justify-content-center align-items-center h-100">
      <div class="col-12 col-md-10 col-lg-8 col-xl-7">
        <div class="card shadow-lg rounded-4 border-0 chat-card">
          <div class="card-header text-white text-center chat-header">
            <h2 class="mb-0 d-flex align-items-center justify-content-center" style="gap: 0.5rem;">
              <span style="font-size: 2.2rem;">🩺</span>
              Health AI Chatbot
            </h2>
          </div>
          <div class="card-body chat-box flex-grow-1" ref="chatBox">
            <div
              v-for="(message, index) in messages"
              :key="index"
              :class="['d-flex', 'mb-3', message.type === 'user' ? 'justify-content-end' : 'justify-content-start']"
            >
              <div
                :class="[
                  'p-3',
                  'rounded-4',
                  message.type === 'user'
                    ? 'bg-primary text-white align-self-end shadow-sm'
                    : 'bg-white text-dark align-self-start border border-2 border-success-subtle shadow-sm'
                ]"
                style="max-width: 80%; word-break: break-word; font-size: 1.2rem;"
              >
                <span v-if="message.type !== 'user'" class="me-2" style="font-size: 1.3rem;">🤖</span>
                {{ message.content }}
              </div>
            </div>
            <!-- Jumping dots loader for bot typing -->
            <div v-if="botTyping" class="d-flex justify-content-start mb-3">
              <div class="bg-white border border-2 border-success-subtle p-3 rounded-4 align-self-start shadow-sm">
                <span class="jumping-dots d-inline-flex align-items-center" style="font-size: 1.2rem;">
                  <span class="me-1">🤖</span>
                  <span>. </span><span>. </span><span>. </span>
                </span>
              </div>
            </div>
          </div>
          <div class="card-footer bg-white border-0 rounded-bottom-4 chat-footer">
            <form @submit.prevent="handleSend" class="d-flex gap-2 align-items-end">
              <textarea
                v-model="userMessage"
                class="form-control rounded-3 border-2 chat-input"
                placeholder="Type your health question..."
                rows="1"
                @keydown.enter.prevent="handleEnterKey"
                :disabled="loading || botTyping"
                style="resize: none; font-size: 1.15rem; min-height: 3.2rem; max-height: 5rem; height: 3.2rem;"
              ></textarea>
              <button
                type="submit"
                class="btn btn-success px-4 py-2 rounded-3"
                style="font-size: 1.15rem; height: 3.2rem;"
                :disabled="loading || botTyping || !userMessage.trim()"
              >
                Send
              </button>
            </form>
            <div v-if="error" class="alert alert-danger mt-2 mb-0 py-2 px-3" role="alert">
              {{ error }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onUpdated } from 'vue'
import useChatbot from '@/composable/ChatbotApi'

export default {
  setup() {
    const { messages, error, loading, sendMessage } = useChatbot()
    const userMessage = ref('')
    const chatBox = ref(null)
    const botTyping = ref(false)

    const handleSend = async () => {
      if (!userMessage.value.trim()) return
      botTyping.value = true
      await sendMessage(userMessage.value)
      userMessage.value = ''
      botTyping.value = false
    }

    const handleEnterKey = (event) => {
      if (!event.shiftKey) {
        handleSend()
      }
    }

    // Auto scroll to bottom when messages update or bot is typing
    onUpdated(() => {
      if (chatBox.value) {
        chatBox.value.scrollTop = chatBox.value.scrollHeight
      }
    })

    return {
      userMessage,
      messages,
      error,
      loading,
      handleSend,
      handleEnterKey,
      chatBox,
      botTyping
    }
  }
}
</script>

<style scoped>
.chat-outer {
  background: linear-gradient(135deg, #e0f7fa 0%, #f8fafc 100%);
  min-height: 100vh;
  height: 100vh;
  width: 100vw;
  padding: 0;
  margin: 0;
}
.chat-card {
  min-height: 85vh;
  max-height: 95vh;
  display: flex;
  flex-direction: column;
}
.chat-header {
  background: linear-gradient(90deg, #00bcd4 60%, #43e97b 100%);
  border-top-left-radius: 1rem;
  border-top-right-radius: 1rem;
  padding-top: 2rem;
  padding-bottom: 1rem;
}
.chat-box {
  height: 55vh;
  min-height: 350px;
  max-height: 60vh;
  overflow-y: auto;
  background-color: #f8fafc;
  border-radius: 1rem;
  margin-bottom: 0.5rem;
  border: none;
  padding-bottom: 1rem;
}
.chat-footer {
  padding-top: 1rem;
  padding-bottom: 1.5rem;
}
.chat-input {
  min-height: 3.2rem;
  max-height: 5rem;
  height: 3.2rem;
  font-size: 1.15rem;
  display: flex;
  align-items: center;
  padding-top: 0.6rem;
  padding-bottom: 0.6rem;
}
.jumping-dots span {
  display: inline-block;
  font-size: 2rem;
  line-height: 1;
  animation: jump 1s infinite;
}
.jumping-dots span:nth-child(2) {
  animation-delay: 0.2s;
}
.jumping-dots span:nth-child(3) {
  animation-delay: 0.4s;
}
@keyframes jump {
  0%, 100% { transform: translateY(0); }
  30% { transform: translateY(-8px); }
  60% { transform: translateY(0); }
}
.jumping-dots {
  line-height: 1.2;
}

</style>
