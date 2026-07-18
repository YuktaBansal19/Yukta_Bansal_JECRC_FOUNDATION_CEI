from dotenv import load_dotenv

from src.vector_store import VectorStore
from src.pipeline import DriveWisePipeline

load_dotenv()


def main():
    store = VectorStore()
    try:
        store.load("index")
    except FileNotFoundError as e:
        print(e)
        return

    pipeline = DriveWisePipeline(store)

    brands = pipeline.available_brands()
    print("Available brands:", ", ".join(brands))
    brand = input("Pick a brand: ").strip()

    models = pipeline.available_models(brand)
    if not models:
        print(f"No models found for brand '{brand}'. Check spelling and try again.")
        return
    print("Available models:", ", ".join(models))
    model = input("Pick a model: ").strip()

    print(f"\nAsk anything about the {brand} {model}. Type 'exit' to quit.\n")
    while True:
        question = input("You: ").strip()
        if question.lower() in ("exit", "quit"):
            break
        if not question:
            continue

        result = pipeline.ask(question, brand=brand, model=model)
        print(f"\nDriveWise: {result['answer']}\n")
        if result["sources"]:
            print("Sources:")
            for s in result["sources"]:
                print(f"  - {s['section']} (page {s['page']}, {s['doc_version']})")
        print()


if __name__ == "__main__":
    main()
