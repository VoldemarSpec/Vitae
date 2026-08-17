<template>
  <div
    class="min-h-screen bg-slate-900 flex items-center justify-center p-0 sm:p-4 overflow-hidden"
  >
    <div
      class="w-full max-w-2xl bg-slate-800 sm:rounded-2xl shadow-xl overflow-hidden flex flex-col h-[100dvh] sm:h-[80vh]"
    >
      <!-- HEADER -->
      <div
        class="bg-slate-950 px-4 py-3 sm:p-4 border-b border-slate-700 flex items-center gap-3 shrink-0"
      >
        <div
          class="w-9 h-9 sm:w-10 sm:h-10 bg-sky-500 rounded-full flex items-center justify-center text-white font-bold text-base sm:text-xl shrink-0 overflow-hidden shadow-lg shadow-sky-500/20"
        >
          <span class="text-sm">VS</span>
        </div>

        <div class="min-w-0">
          <h1
            class="text-white font-semibold text-sm sm:text-base flex items-center gap-2 truncate"
          >
            Volodymyr Spetsialnyi

            <span
              class="w-2 h-2 bg-emerald-400 rounded-full animate-pulse shrink-0"
            ></span>
          </h1>

          <p class="text-sky-400 text-[11px] sm:text-xs">AI Resume Assistant</p>
        </div>
      </div>

      <!-- CHAT -->
      <div
        ref="chatContainer"
        class="flex-1 min-h-0 overflow-y-auto px-3 py-4 sm:p-4 space-y-3 sm:space-y-4 bg-slate-800 text-sm no-scrollbar"
      >
        <div
          v-for="(msg, index) in messages"
          :key="index"
          class="flex"
          :class="msg.role === 'user' ? 'justify-end' : 'justify-start'"
        >
          <div
            class="px-3 py-2.5 sm:p-3 rounded-2xl max-w-[90%] sm:max-w-[80%] shadow-sm whitespace-pre-wrap break-words leading-relaxed"
            :class="
              msg.role === 'user'
                ? 'bg-sky-600 text-white rounded-tr-none'
                : 'bg-slate-700 text-white rounded-tl-none border border-slate-600'
            "
          >
            {{ msg.content }}
          </div>
        </div>

        <div v-if="isLoading" class="flex justify-start">
          <div
            class="bg-slate-700 px-4 py-3 rounded-2xl rounded-tl-none shadow-sm border border-slate-600 flex items-center gap-1.5 h-[44px]"
          >
            <div
              class="w-2 h-2 bg-sky-400 rounded-full animate-bounce"
              style="animation-delay: 0ms"
            ></div>

            <div
              class="w-2 h-2 bg-sky-400 rounded-full animate-bounce"
              style="animation-delay: 150ms"
            ></div>

            <div
              class="w-2 h-2 bg-sky-400 rounded-full animate-bounce"
              style="animation-delay: 300ms"
            ></div>
          </div>
        </div>
      </div>

      <!-- INPUT AREA -->
      <div
        class="shrink-0 px-3 pt-3 pb-[calc(0.75rem+env(safe-area-inset-bottom))] sm:p-4 bg-slate-900 border-t border-slate-700 flex flex-col gap-2.5 sm:gap-3"
      >
        <!-- QUICK REPLIES -->
        <div
          class="flex gap-2 overflow-x-auto pb-1 no-scrollbar sm:flex-wrap sm:overflow-visible"
        >
          <button
            v-for="reply in quickReplies"
            :key="reply"
            @click="sendQuickReply(reply)"
            :disabled="isLoading"
            class="px-3 sm:px-4 py-1.5 bg-slate-800/50 hover:bg-sky-600 text-sky-400 hover:text-white border border-sky-500/30 rounded-full text-[11px] sm:text-xs font-medium whitespace-nowrap transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed shrink-0"
          >
            {{ reply }}
          </button>
        </div>

        <!-- INPUT -->
        <div class="flex gap-2">
          <input
            v-model="userInput"
            @keyup.enter="sendMessage"
            :disabled="isLoading"
            type="text"
            inputmode="text"
            autocomplete="off"
            enterkeyhint="send"
            placeholder="Type your question..."
            class="min-w-0 flex-1 bg-slate-800 text-white px-3 sm:px-4 py-2.5 sm:py-3 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-sky-500 placeholder-slate-500 disabled:opacity-50 shadow-inner"
          />

          <button
            @click="sendMessage"
            :disabled="isLoading || !userInput.trim()"
            aria-label="Send message"
            class="w-11 h-11 sm:w-auto sm:h-auto sm:px-6 sm:py-3 shrink-0 bg-sky-500 hover:bg-sky-400 text-white rounded-xl font-medium transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center shadow-lg shadow-sky-500/20"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24"
              fill="currentColor"
              class="w-5 h-5"
            >
              <path
                d="M3.478 2.404a.75.75 0 0 0-.926.941l2.432 7.905H13.5a.75.75 0 0 1 0 1.5H4.984l-2.432 7.905a.75.75 0 0 0 .926.94 60.519 60.519 0 0 0 18.445-8.986.75.75 0 0 0 0-1.218A60.517 60.517 0 0 0 3.478 2.404Z"
              />
            </svg>

            <span class="hidden sm:inline ml-2"> Send </span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, nextTick } from "vue";

const quickReplies = [
  "💻 What is your tech stack?",
  "🚀 Tell me about your recent projects",
  "🎓 What is your education?",
  "📫 How can I contact you?",
];

const messages = ref([
  {
    role: "assistant",
    content:
      "Hello! I am the digital AI avatar of Volodymyr. Ask me anything about his IT experience, skills, or projects!",
  },
]);

const userInput = ref("");
const isLoading = ref(false);
const chatContainer = ref(null);

const scrollToBottom = async () => {
  await nextTick();

  if (chatContainer.value) {
    chatContainer.value.scrollTo({
      top: chatContainer.value.scrollHeight,
      behavior: "smooth",
    });
  }
};

const sendQuickReply = (text) => {
  const cleanText = text.replace(/^[^\w\s]+/, "").trim();

  userInput.value = cleanText;
  sendMessage();
};

const sendMessage = async () => {
  const text = userInput.value.trim();

  if (!text || isLoading.value) return;

  messages.value.push({
    role: "user",
    content: text,
  });

  userInput.value = "";
  isLoading.value = true;

  await scrollToBottom();

  try {
    const baseUrl =
      import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000";

    const response = await fetch(`${baseUrl}/api/v1/chat/chatsend`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        messages: messages.value,
      }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }

    const data = await response.json();

    messages.value.push({
      role: data.role,
      content: data.content,
    });
  } catch (error) {
    console.error("Chat error:", error);

    messages.value.push({
      role: "assistant",
      content: "Oops! Cannot connect to the server. Is the backend running?",
    });
  } finally {
    isLoading.value = false;
    await scrollToBottom();
  }
};
</script>

<style scoped>
.no-scrollbar::-webkit-scrollbar {
  display: none;
}

.no-scrollbar {
  -ms-overflow-style: none;
  scrollbar-width: none;
}

@media (max-width: 640px) {
  input {
    font-size: 16px;
  }
}
</style>
