# 🤖 RAG AI Project

> A powerful conversational AI system using RAG (Retrieval Augmented Generation) with advanced memory management

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat-square&logo=python)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=flat-square&logo=docker)
![Neo4j](https://img.shields.io/badge/Neo4j-Enabled-008CC1?style=flat-square&logo=neo4j)
![Qdrant](https://img.shields.io/badge/Qdrant-Vector_DB-172BF4?style=flat-square)

</div>

## 🌟 Features

- 🧠 **Smart Conversations** - Powered by Google's Gemini AI
- 📊 **Vector Storage** - Fast similarity search with Qdrant
- 🕸️ **Graph Database** - Context management using Neo4j
- 💾 **Memory System** - Enhanced with mem0ai
- 🔄 **OpenAI Compatible** - Works with Gemini through OpenAI interface

## 🚀 Quick Start

### Prerequisites

- Python 3.13+
- Docker & Docker Compose
- Google AI (Gemini) API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ashisharjun12/conversational-AI.git
   cd rag_ai
   ```

2. **Start the databases**
   ```bash
   docker-compose up -d
   ```

3. **Install dependencies**
   ```bash
   pip install .
   ```

4. **Configure environment**
   Update these variables in `main.py`:
   ```python
   GEMINI_API_KEY = "your-api-key"
   QDRANT_HOST = "localhost"
   NEO4J_URL = "bolt://localhost:7687"
   NEO4J_USERNAME = "neo4j"
   NEO4J_PASSWORD = "your-password"
   ```

## 🗄️ Services

### 📊 Qdrant Vector Database
- **Port**: 6333
- **Purpose**: Vector embeddings storage
- **Status**: Auto-configured on startup

### 🕸️ Neo4j Graph Database
- **Web Interface**: [http://localhost:7474](http://localhost:7474)
- **Bolt Port**: 7687
- **Default Credentials**:
  - Username: `neo4j`
  - Password: `reform-william-center-vibrate-press-5829`
- **Features**:
  - APOC plugin enabled
  - Graph visualization
  - Query interface

## 💻 Usage

Run the application:
```bash
python main.py
```

You'll see a prompt:
```
>> [Type your message here]
```

The system will:
- Process your input
- Generate AI responses
- Store conversation history
- Maintain context through vector and graph databases

## 📦 Dependencies

### Core Libraries
- `google-generativeai` - Gemini AI integration
- `langchain` - LLM framework
- `mem0ai` - Memory management
- `neo4j` - Graph database client
- `openai` - API compatibility layer
- `rank-bm25` - Text ranking

## 🛠️ Development

- **Python Version**: 3.13
- **Version Management**: Via `.python-version`
- **IDE Support**: VS Code configurations included

## 📝 License

[Add your license information here]

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

<div align="center">
Made with ❤️ using RAG Architecture
</div>