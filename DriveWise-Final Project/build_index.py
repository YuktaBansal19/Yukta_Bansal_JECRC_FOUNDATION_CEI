
from src.ingest import load_all_brochures
from src.vector_store import VectorStore


def main():
    print("loading brochures from data/brochures ...")
    chunks = load_all_brochures("data/brochures")
    print(f"got {len(chunks)} chunks total")

    store = VectorStore()
    print("building embeddings (first run downloads the model, can take a minute)...")
    store.build(chunks)

    store.save("index")
    print(f"index saved to index/ (mode={store.mode})")


if __name__ == "__main__":
    main()
