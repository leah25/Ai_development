from openai import OpenAI
client = OpenAI(
    base_url="https://api.openai.com/v1",
    api_key="ollama"
)

response = client.embeddings.create(
    model="nomic-embed-text",
    input="python is a programming language"
)

embedding = response.data[0].embedding
