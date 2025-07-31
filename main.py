# main.py

from Modules.llm_interface import get_llm_response  # fixed import path
from Modules.memory import store_memory, retrieve_memory

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

        # Retrieve memory context
        memory_snippets = retrieve_memory(user_input)

        # Format memory as internal assistant knowledge
        system_prefix = (
            "You are E.V.E.R.E.S.T., an AI assistant that remembers past interactions and facts. "
            "Use the following known context only if relevant:\n"
        )
        memory_block = "\n".join(f"- {m}" for m in memory_snippets)
        full_prompt = f"{system_prefix}{memory_block}\nUser: {user_input}" if memory_snippets else user_input

        # Get response from LLM
        response = get_llm_response(full_prompt)
        print("EVEREST:", response)

        # Store both question and answer
        store_memory("user", user_input)
        store_memory("bot", response)

if __name__ == "__main__":
    main()
