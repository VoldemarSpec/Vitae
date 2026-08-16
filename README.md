# 🚀 Vitae — Interactive AI Resume

**Vitae** turns a static CV into a live conversation. Instead of reading a boring PDF, recruiters and tech leads can chat directly with an AI avatar of **Volodymyr Spetsialnyi** to ask about my IT experience, tech stack, and career goals in real-time.

![Vue.js](https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)

---

## ✨ How It Works

1. **User asks a question** via the frontend chat interface (e.g., _"What is your backend stack?"_).
2. Frontend sends the chat history to the FastAPI backend.
3. Backend prepends a securely cached **System Prompt** to enforce role boundaries and professional context.
4. The request is processed by the **OpenAI API** (`gpt-4o-mini`).
5. If OpenAI is unavailable, a graceful fallback response is returned with direct contact info.

---

## 🛠️ Tech Stack

### Backend

- **Python 3.10+** & **FastAPI**
- **Pydantic v2** (Strict Data Validation)
- **SlowAPI** (Rate Limiting)
- **OpenAI Async API**
- **Uvicorn**

### Frontend

- **Vue 3** (Composition API)
- **Vite**
- **TailwindCSS v4**

### Testing

- **pytest** & **fastapi.testclient**

---

## 🔒 Security & Architecture Guardrails

Built with production readiness in mind:

- **Prompt Injection Protection:** Strict validation of user roles and content length via Pydantic model validators.
- **Fail-Fast I/O:** The system prompt is read from the disk exactly once at startup and cached in memory to eliminate I/O bottlenecks.
- **DDoS Protection:** Endpoint is protected by SlowAPI, limiting requests to 5 per minute per IP.
- **Separation of Concerns:** Route handlers only process HTTP context, while business logic and external APIs are decoupled.

---

## 📡 API Reference

### `POST /api/v1/chat/chatsend`

**Request:**

```json
{
  "messages": [{ "role": "user", "content": "Hi! Tell me about your stack." }]
}
```

**Response:**

```json
{
  "role": "assistant",
  "content": "I specialize in Python, FastAPI, and Vue.js..."
}
```

**Validation & Limits:**

- Max **20** messages in chat history.
- Max **500** characters per user message.
- Rate limit: **5 requests/minute** per client.

---

## 🚀 Quick Start (Local Setup)

To run this project locally, you will need two terminal windows.

### 1. Backend Setup

Navigate to the project root and create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows use: .venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Set up environment variables by creating a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_api_key_here
```

Start the backend server:

```bash
python main.py
```

_Backend is now running at `http://localhost:8000`_

### 2. Frontend Setup

Open a new terminal window and navigate to the frontend folder:

```bash
cd Vitae/app/frontend
npm install
npm run dev
```

_Frontend is now running at `http://localhost:5173`_

---

## 📂 Project Structure

```text
Vitae/
├── main.py
├── requirements.txt
├── .env                  # Environment variables (ignored in git)
├── tests/
│   └── test_chat.py
└── Vitae/
    └── app/
        ├── backend/
        │   ├── routes/chat.py
        │   └── schemas/chat.py
        ├── core/
        │   ├── limiter.py
        │   └── prompt.txt
        ├── externalservices/
        │   └── openai/openai_api.py
        └── frontend/
            ├── src/
            │   ├── App.vue
            │   └── main.js
            ├── package.json
            └── vite.config.js
```

---

## 🧪 Testing

Run the test suite from the project root:

```bash
pytest
```

_Tests cover successful API responses, OpenAI fallback mechanisms, and validation errors._

---

## 🔮 Future Improvements

- Add persistent personal sessions (Auth).
- Implement token streaming for real-time typing generation.
- Add Docker Compose for a one-command setup.
- Set up a CI/CD pipeline (Linting, Tests, Auto-deploy).

---

## 📬 Contact & Links

- **Email:** Vova.Spetcialny@gmail.com
- **GitHub:** [VoldemarSpec](https://github.com/VoldemarSpec)
- **License:** See `LICENSE.txt`
