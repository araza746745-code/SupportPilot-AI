SupportPilot AI 🤖

AI-Powered Customer Support Platform

SupportPilot AI is an intelligent customer support platform that uses Large Language Models (LLMs) to analyze customer issues, classify support requests, detect priority levels, and generate professional customer responses.

The application combines a Next.js frontend, FastAPI backend, and Ollama-powered Llama 3.2 model.

🚀 Key Features

- AI Issue Analysis: Understands customer problems using Llama 3.2.
- Ticket Classification: Identifies customer issue categories.
- Priority Detection: Assigns priority levels such as High, Medium, and Low.
- AI-Generated Responses: Creates professional customer support replies.
- Recommended Solutions: Suggests practical troubleshooting steps.
- Ticket Management: Create, view, and resolve support tickets.
- Copy Response: Copy AI-generated replies for customer communication.

🛠️ Technology Stack

Layer| Technologies
Frontend| Next.js, React, TypeScript, Tailwind CSS
Backend| Python, FastAPI
AI / LLM| Ollama, Llama 3.2
API| REST API
Version Control| Git, GitHub

🏗️ Architecture

User
|
v
Next.js Frontend
|
v
FastAPI Backend
|
v
AI Assistant Service
|
v
Ollama - Llama 3.2
|
v
AI Analysis Result
|
v
Frontend Response

📁 Project Structure

SupportPilot-AI/
│
├── backend/
│ ├── app/
│ │ ├── ai/
│ │ │ └── assistant.py
│ │ ├── api/
│ │ │ └── routes/
│ │ │ └── tickets.py
│ │ └── main.py
│ ├── requirements.txt
│ └── .env.example
│
├── frontend/
│ ├── src/
│ ├── public/
│ └── package.json
│
└── README.md

⚙️ Installation and Setup

1. Clone the Repository

git clone https://github.com/araza746745-code/SupportPilot-AI.git
cd SupportPilot-AI

2. Backend Setup

cd backend
python -m venv venv

Activate the virtual environment on Windows:

.\venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt

Start FastAPI:

uvicorn app.main:app --reload

Backend API documentation:

http://127.0.0.1:8000/docs

3. Install and Run Ollama

Install Ollama and download the model:

ollama pull llama3.2

Make sure the Ollama service is running.

4. Frontend Setup

Open another terminal:

cd frontend
npm install
npm run dev

Open the application:

http://localhost:3000

🔌 API Endpoints

Method| Endpoint| Description
GET| "/tickets/"| Get all tickets
POST| "/tickets/"| Create a ticket
PATCH| "/tickets/{ticket_id}/resolve"| Resolve a ticket
POST| "/tickets/analyze"| Analyze customer issue using AI
GET| "/health"| Check backend health

🧠 AI Workflow

1. Customer enters their name and problem.
2. Frontend sends the request to FastAPI.
3. Backend sends the issue to Llama 3.2 through Ollama.
4. LLM identifies the issue category and generates a response.
5. Python applies priority validation for configured critical keywords.
6. Backend returns the analysis to the frontend.
7. Customer support staff can review and copy the suggested reply.

🔮 Future Enhancements

- SQLite database integration
- Persistent ticket storage
- Advanced AI ticket classification
- LangGraph-based AI workflows
- Human-in-the-Loop approval
- Authentication and role-based access
- Docker deployment
- Cloud deployment

👨‍💻 Developer

Ahmed Raza

GitHub: https://github.com/araza746745-code

---

SupportPilot AI — Making customer support smarter with AI.
