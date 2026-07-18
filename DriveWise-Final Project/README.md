# DriveWise — Metadata-Aware Automotive RAG Assistant

## Project Description

Developed an end-to-end AI-powered assistant that lets users interact conversationally with Hyundai car brochures — including the Grand i10 NIOS, i20, i20 N Line, AURA, VERNA and VENUE.

The system leverages Retrieval-Augmented Generation (RAG) to provide accurate, context-aware answers by converting brochure content into vector embeddings, filtering by metadata, and performing semantic search.

Users select a car brand and model and ask normal questions about it, receiving answers grounded in that specific brochure's content along with the section and page the answer came from.

---

## Key Features

- **Metadata-Aware Filtering**
  - Retrieval is restricted to the selected brand/model before any embedding search runs, so answers never mix content from different cars

- **Structured Chunking**
  - Brochures are split by actual sections (exterior, interior, safety, technology, engine, variants, technical specs) with page numbers, not arbitrary text splits

- **Semantic Search**
  - Sentence-transformer embeddings for retrieval, with automatic TF-IDF fallback if the model can't be downloaded

- **Re-Ranking**
  - Cross-encoder re-ranks the initial retrieval results for more accurate relevance ordering, with a keyword-overlap fallback

- **Context Window Control**
  - Only the top 3–4 re-ranked chunks are passed to the model, keeping answers focused and reducing noise

- **Source Attribution**
  - Every answer returns the brochure section, page number and doc version it came from

- **Query Logging**
  - Question, response time, chunk count and success/fail status logged to `logs/query_log.jsonl`

- **Runs Fully Locally**
  - No server, no paid API required — optional local LLM generation via Ollama

---

## System Architecture

- **Data Ingestion**
  - Reads brochure `.txt` files from `data/brochures/`

- **Metadata Parsing**
  - Front-matter block (brand, model, year, category, fuel types, doc version) parsed separately from section content

- **Chunking**
  - One brochure section = one chunk, each tagged with section title and page number

- **Embedding Generation**
  - Chunks converted to vector embeddings using a sentence-transformer model (MiniLM)

- **Metadata Filtering**
  - Chunks filtered to the selected brand/model before vector search runs

- **Vector Search**
  - Cosine similarity search over the filtered chunk set

- **Re-Ranking**
  - Cross-encoder re-scores the top retrieved chunks for relevance

- **Answer Generation**
  - Context passed to a local LLM (via Ollama) if configured, otherwise the best-matching passage is returned directly

- **Logging & Evaluation**
  - Query logs written per request; `eval/eval_questions.json` used to check correctness and context relevance

---

## Known Limitations

- Only 6 models currently — a proper vector DB (Chroma/FAISS) would be worth switching to at larger scale
- No UI for uploading new brochures — drop a `.txt` file into `data/brochures/` and re-run `build_index.py`
- Faithfulness evaluation is manual
- Logging is a flat JSONL file

---

## Tech Stack

Python, sentence-transformers (MiniLM embeddings + MiniLM cross-encoder), scikit-learn (TF-IDF fallback), Ollama for generation (optional)
