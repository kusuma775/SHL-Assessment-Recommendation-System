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

## 🚀 How to Run the Project

# 1️⃣ Clone the Repository
git clone https://github.com/<your-username>/SHL-Assessment-Recommendation-System.git
cd SHL-Assessment-Recommendation-System

# 2️⃣ Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

# 3️⃣ Install Dependencies
pip install -r requirements.txt

# 4️⃣ Run the Application
streamlit run app.py

# 5️⃣ Open in Browser
# http://localhost:8501

# Example Input (inside the app)
# Software Developer
