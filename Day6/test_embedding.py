from openai import OpenAI
from similarity import cosine_similarity

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
) 

text1 = "python is a programming language"
text2 = "my name is sharon."

embeding1 = client.embeddings.create(
    model="nomic-embed-text",
    input=text1
).data[0].embedding

embedding2 = client.embeddings.create(
    model="nomic-embed-text",
    input=text2
).data[0].embedding
score = cosine_similarity(embeding1, embedding2)
print("Cosine Similarity Score:", score)


def create_embedding(content):
    embedding = client.embeddings.create(
        model="nomic-embed-text",
        input=content
    ).data[0].embedding
    return embedding

