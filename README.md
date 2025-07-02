# -AI-HR-Self-Service-Assistant-
Simulated AI-driven HR assistant built using modern microservices, LLMs, and secure cloud-native architecture.
## 🧩 Features
- ✅ Mock ISV APIs using FastAPI (e.g., Leave Management)
- ✅ gRPC microservices with Protobuf
- ✅ OAuth2-secured Gateway + JWT auth
- ✅ OpenAI LLM integration for NLU intent parsing
- ✅ React + Tailwind conversational frontend
- ✅ Docker Compose orchestration
- ✅ GitHub Actions CI/CD pipeline
- ✅ Exportable ticket CSVs + Admin panel

## 📦 Stack
- Python, FastAPI, gRPC, Protobuf
- React, Tailwind CSS
- OpenAI API (GPT-4)
- Docker, GitHub Actions, Makefile

## 🛠️ Setup
```bash
make proto   # Compile .proto files
make build   # Build all services
make run     # Start via Docker Compose
