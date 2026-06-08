
# 🚀 DocuMind: Multi-Agent RAG System

> An AI-powered document intelligence platform that uses a multi-agent Retrieval-Augmented Generation (RAG) architecture to answer questions from uploaded PDFs with grounded, source-aware responses.

---

## 🌟 Overview

DocuMind enables users to upload documents and interact with them using natural language.

Instead of relying on a single AI agent, DocuMind uses a **multi-agent architecture** where specialized agents collaborate to:

* Plan the retrieval strategy
* Retrieve relevant document chunks
* Generate contextual answers
* Critique and refine responses

This design improves answer quality, transparency, and maintainability.

---

## 🏗️ System Architecture

```text
User
  │
  ▼
Streamlit Frontend
  │
  ▼
Planner Agent
  │
  ▼
Retriever Agent
  │
  ▼
ChromaDB Vector Store
  │
  ▼
Answer Generator Agent
  │
  ▼
Critic Agent
  │
  ▼
Final Response + Sources
```

---

## ✨ Features

### 📄 Document Intelligence

* PDF document ingestion
* Text extraction and chunking
* Semantic search over documents
* Source-aware answers

### 🤖 Multi-Agent Workflow

* Planner Agent
* Retriever Agent
* Generator Agent
* Critic Agent

### 🧠 Retrieval-Augmented Generation

* Context-aware responses
* Hallucination reduction
* Source traceability

### ⚙️ DevOps & Cloud

* Dockerized application
* GitHub Actions CI/CD
* Docker Hub integration
* AWS EC2 deployment workflow

---

## 🛠️ Tech Stack

### AI & Machine Learning

* LangChain
* HuggingFace Embeddings
* Sentence Transformers
* Groq LLM

### Vector Database

* ChromaDB

### Backend

* Python

### Frontend

* Streamlit

### DevOps

* Docker
* GitHub Actions
* Docker Hub

### Cloud

* AWS EC2

---

## 📂 Project Structure

```text
Documind/
│
├── app.py
├── ingest.py
├── requirements.txt
├── Dockerfile
│
├── rag/
│   ├── planner.py
│   ├── retriever.py
│   ├── agent_retriever.py
│   ├── critic.py
│   ├── chain.py
│   └── embedder.py
│
├── frontend/
│
├── test_loader.py
├── test_chunker.py
├── test_embedder.py
├── test_retriever.py
└── test_rag.py
```

---

## 🔄 CI/CD Pipeline

```text
Developer
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ▼
Docker Build
    │
    ▼
Docker Hub
```

### Automated Workflow

* Triggered on every push to main
* Builds Docker image automatically
* Validates container build process
* Publishes image to Docker Hub

---

## 🐳 Docker

### Build

```bash
docker build -t documind .
```

### Run

```bash
docker run -p 8501:8501 documind
```

---

## ☁️ AWS Experience

During development, the project was tested using:

* Amazon EC2
* SSH-based deployment workflows
* Security Group configuration
* Linux server administration
* Container deployment practices

---

## 🎯 Key Learnings

* Retrieval-Augmented Generation (RAG)
* Multi-Agent AI Systems
* Vector Databases
* Docker Containerization
* GitHub Actions CI/CD
* AWS Cloud Fundamentals
* Linux Administration
* Production-Oriented AI Development

---

## 🚀 Future Improvements

* Authentication & User Management
* Multi-document conversations
* Agent evaluation framework
* Automated deployment to EC2
* Monitoring & Observability
* Kubernetes deployment
* Production-grade CI/CD pipeline

---

## 👩‍💻 Author

**Richa Chandra**

Passionate about AI Engineering, Cloud Computing, and Building Production-Ready Intelligent Systems.

---

⭐ If you found this project interesting, consider starring the repository.
