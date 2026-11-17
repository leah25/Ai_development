from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
# create client that connects to the Ollama API using the base URL and API key from the .env file
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

response = client.chat.completions.create(
    model=os.getenv("Model"),
    messages=[
        {"role": "user", "content": "write a short poem about the rain in the style of Robert Frost "}
    ]
)
print(response.choices[0].message.content)