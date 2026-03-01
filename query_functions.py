import json
import numpy as np
import pandas as pd
import re
from sentence_transformers import SentenceTransformer, util
import torch

# =========================
# Load SHL Catalogue
# =========================
catalog_df = pd.read_csv("SHL_catalog.csv")

def combine_row(row):
    parts = [
        str(row.get("Assessment Name", "")),
        str(row.get("Duration", "")),
        str(row.get("Remote Testing Support", "")),
        str(row.get("Adaptive/IRT", "")),
        str(row.get("Test Type", "")),
        str(row.get("Skills", "")),
        str(row.get("Description", "")),
    ]
    return " ".join(parts)

catalog_df["combined"] = catalog_df.apply(combine_row, axis=1)
corpus = catalog_df["combined"].tolist()

# =========================
# Embedding Model
# =========================
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
corpus_embeddings = embedding_model.encode(corpus, convert_to_tensor=True)

# =========================
# Semantic Search Logic
# =========================
def find_assessments(user_query, k=5):
    query_embedding = embedding_model.encode(user_query, convert_to_tensor=True)
    cosine_scores = util.cos_sim(query_embedding, corpus_embeddings)[0]

    top_k = min(k, len(corpus))
    top_results = torch.topk(cosine_scores, k=top_k)

    results = []
    for score, idx in zip(top_results[0], top_results[1]):
        idx = idx.item()
        results.append({
            "Assessment Name": catalog_df.iloc[idx]["Assessment Name"],
            "Skills": catalog_df.iloc[idx]["Skills"],
            "Test Type": catalog_df.iloc[idx]["Test Type"],
            "Description": catalog_df.iloc[idx]["Description"],
            "Remote Testing Support": catalog_df.iloc[idx]["Remote Testing Support"],
            "Adaptive/IRT": catalog_df.iloc[idx]["Adaptive/IRT"],
            "Duration": catalog_df.iloc[idx]["Duration"],
            "URL": catalog_df.iloc[idx]["URL"],
            "Relevance Score": round(float(score), 4),
        })

    return results

# =========================
# MAIN FUNCTION (USED BY app.py)
# =========================
def query_handling_using_LLM_updated(query):
    """
    Main entry point used by app.py
    Returns a DataFrame of recommended SHL assessments
    """
    results = find_assessments(query, k=5)
    return pd.DataFrame(results)