# 🚗 AI CEO Strategic Intelligence Agent

## Project Overview

This project is an AI-powered Strategic Intelligence Agent developed for Tesla. It collects live business intelligence from multiple public sources, processes the information using Natural Language Processing, stores embeddings in ChromaDB, and uses Retrieval-Augmented Generation (RAG) with Ollama (Qwen2.5) to generate executive-level strategic recommendations.

The application assists executives in identifying opportunities, risks, competitor activities, and market trends through an interactive Streamlit dashboard.

---

## Objectives

- Collect Tesla-related news automatically
- Monitor competitors
- Detect market opportunities
- Identify strategic risks
- Generate executive recommendations
- Support evidence-based decision making

---

## Technologies

- Python
- Streamlit
- Ollama (Qwen2.5)
- ChromaDB
- BAAI BGE Embeddings
- Pandas
- Feedparser
- BeautifulSoup
- Sentence Transformers

---

## Project Architecture

```
Google News
Competitor News
Tesla News
        │
        ▼
Data Collection
        │
Cleaning & Deduplication
        │
Chunking
        │
BGE Embeddings
        │
ChromaDB Vector Database
        │
Semantic Search (RAG)
        │
Ollama (Qwen2.5)
        │
Strategic Intelligence Engine
        │
Streamlit Dashboard
```

---

## Project Structure

```
Strategic-Intelligence-Agent/

dashboard/
scraper/
processing/
database/
intelligence/
data/

app.py
config.py
requirements.txt
README.md
```

---

## Features

- Live News Collection
- Competitor Monitoring
- Market Intelligence Dashboard
- Sentiment Analysis
- Opportunity Monitor
- Risk Monitor
- Strategic Recommendations
- CEO Briefing
- Retrieval-Augmented Generation (RAG)

---

## AI Pipeline

1. Data Collection
2. Data Cleaning
3. Deduplication
4. Chunking
5. Embedding Generation
6. ChromaDB Storage
7. Semantic Retrieval
8. AI Reasoning using Ollama
9. Executive Dashboard

---

## Running the Project

Install:

```bash
pip install -r requirements.txt
```

Collect data:

```bash
python -m scraper.collect
```

Clean:

```bash
python -m processing.clean
python -m processing.deduplicate
```

Chunk:

```bash
python -m processing.chunking
```

Embeddings:

```bash
python -m processing.embeddings
```

Sentiment:

```bash
python -m processing.sentiment
```

Launch:

```bash
streamlit run app.py
```

---

## Dashboard

- Overview
- Market Intelligence
- Sentiment Analysis
- Opportunity Monitor
- Risk Monitor
- Strategic Recommendations
- CEO Briefing

---

## Future Work

- Financial Report Analysis
- Live Stock Market Data
- Multi-company Comparison
- Cloud Deployment
- PDF Report Generation