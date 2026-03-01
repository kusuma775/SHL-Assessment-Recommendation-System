# 🧠 SHL Assessment Recommendation Engine

An **AI-powered assessment recommendation system** that intelligently suggests the most relevant **SHL assessments** based on a given job role or skill requirement using **semantic search and NLP embeddings**.

---

## 📌 Project Overview

Recruiters and hiring teams often spend significant time manually browsing large assessment catalogs to find the right tests for a role.  
This project automates that process by building a **smart recommendation engine** that maps **job requirements** to the most relevant **SHL assessments**.

Instead of relying on keyword matching, the system uses **transformer-based sentence embeddings** to understand semantic meaning.

---

## 🎯 Key Features

- 🔍 **Semantic Search using AI**
  - Understands intent behind queries like:
    - Software Developer
    - Python skills assessment
    - Backend engineer

- 📊 **SHL Product Catalogue Integration**
  - Uses a structured SHL assessment dataset (`SHL_catalog.csv`)

- ⚡ **Fast & Offline Execution**
  - No external APIs
  - No paid services
  - No unstable dependencies

- 🧠 **Transformer-Based NLP**
  - Powered by `SentenceTransformer (all-MiniLM-L6-v2)`

- 🖥️ **Interactive Web UI**
  - Simple and clean UI built with **Streamlit**

---

## 🏗️ System Architecture

User Query (Job Role / Skills)  
↓  
Sentence Embedding (Transformer Model)  
↓  
Cosine Similarity Matching  
↓  
Ranked SHL Assessments  
↓  
Results Displayed in UI  

---

## 🛠️ Tech Stack

| Category | Technology |
|--------|-----------|
| Language | Python |
| NLP / AI | SentenceTransformers |
| Similarity | Cosine Similarity |
| ML Backend | PyTorch |
| UI | Streamlit |
| Data Source | SHL Assessment Catalogue (CSV) |

---

## 📂 Project Structure

SHL-Assessment-Recommendation-System/  
│  
├── app.py                     # Streamlit UI  
├── query_functions.py          # Core recommendation logic  
├── SHL_catalog.csv             # SHL assessment dataset  
├── requirements.txt            # Python dependencies  
├── README.md                   # Project documentation  
└── venv/                       # Virtual environment (ignored)  

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/SHL-Assessment-Recommendation-System.git
cd SHL-Assessment-Recommendation-System
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
```

### 3️⃣ Activate Virtual Environment

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

### 6️⃣ Open in Browser
```bash
http://localhost:8501
```

## 🧪 Example Usage

### Input
```text
Software Developer
## Output (Sample)

| Assessment Name                | Skills             | Test Type | Duration | Relevance Score |
|--------------------------------|--------------------|-----------|----------|-----------------|
| Software Development Aptitude  | Programming, Logic | Cognitive | 40 mins  | 0.83            |
| Coding Skills Assessment       | Python, Java       | Technical | 60 mins  | 0.79            |
| Logical Reasoning Test         | Problem Solving    | Cognitive | 30 mins  | 0.74            |

---

## 🧠 Why This Project Is Strong

- Solves a real-world hiring problem
- Uses AI/NLP instead of rule-based logic
- Clean, modular, production-ready code
- Fast, deterministic, and reliable
- Easily extensible for enterprise use

---

## 🔮 Future Enhancements

- Role-based weighting (Developer vs Sales roles)
- Assessment duration and test-type filters
- Resume-to-assessment mapping
- Database integration (PostgreSQL / MongoDB)
- Recruiter analytics dashboard

---

## 👤 Author

Kurumu Kusuma  
B.Tech (ECE) | Python & AI Developer  
Interested in AI-driven systems, hiring technology, and scalable applications
