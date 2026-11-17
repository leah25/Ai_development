# AI Agent Development

Hands-on exercises for building AI assistants in Python, from a first chat completion up to a simple Retrieval-Augmented Generation (RAG) assistant. The scripts use the OpenAI Python SDK pointed at an OpenAI-compatible endpoint, such as a local [Ollama](https://ollama.com) server.

## Project structure

```
.
├── hello_ai.py            # One-shot chat completion (a poem about rain)
├── assistant.py           # Interactive command-line chat assistant
├── test_embedding.py      # Creates a text embedding
└── Day6/                  # RAG assistant
    ├── knowledge/         # Text files the assistant answers from
    ├── retriever.py       # Loads the .txt documents from knowledge/
    ├── similarity.py      # Cosine similarity between two vectors
    ├── test_embedding.py  # Embedding demo + create_embedding() helper
    ├── test_retriever.py  # Prints the loaded documents
    └── rag.py             # RAG chat: picks the most relevant document and answers from it
```

## How the RAG assistant works

1. `retriever.py` loads every `.txt` file in `Day6/knowledge/`.
2. Each document is embedded with the `nomic-embed-text` model.
3. When you ask a question, the question is embedded too.
4. `similarity.py` compares the question with each document using cosine similarity.
5. The best-matching document is sent to the chat model as context. The model is told to answer using only that information.

To teach the assistant something new, add a `.txt` file to `Day6/knowledge/`.

## Setup

1. Install Python 3 and [Ollama](https://ollama.com), then pull the models:

   ```bash
   ollama pull nomic-embed-text
   ollama pull <your-chat-model>   # e.g. llama3.2
   ```

2. Create a virtual environment and install the dependencies:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install openai python-dotenv numpy
   ```

3. Create a `.env` file (it is git-ignored) with your endpoint settings:

   ```env
   BASE_URL=http://localhost:11434/v1
   API_KEY=ollama
   Model=llama3.2
   ```

## Usage

```bash
python hello_ai.py       # one-off response
python assistant.py      # chat; type "quit" to exit

cd Day6
python rag.py            # RAG chat over the knowledge files; type "quit" to exit
```

Run the `Day6` scripts from inside the `Day6` folder, because `retriever.py` looks for `knowledge/` relative to the current directory.
