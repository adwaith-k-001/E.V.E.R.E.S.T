# main.py

from Modules.llm_interface import get_llm_response  # fixed import path

def main():
    print("=" * 40)
    print("      E.V.E.R.E.S.T. AI Assistant")
    print("Engine for Voice, Embeddings, Response, and Enhanced Semantic Tasks")
    print("=" * 40)

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() in {"exit", "quit", "bye"}:
            print("EVEREST: Shutting down. Stay sharp.")
            break

        response = get_llm_response(user_input)
        print("EVEREST:", response)

if __name__ == "__main__":
    main()
