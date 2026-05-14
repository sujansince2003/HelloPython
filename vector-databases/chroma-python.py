import chromadb
import os
import uuid
from dotenv import load_dotenv
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

load_dotenv()


# chroma client

client = chromadb.Client()

collection = client.get_or_create_collection(
    name="my_test_collections",
    embedding_function=OpenAIEmbeddingFunction(
        api_key=os.getenv("OPEN_AI_API_KEY"), model_name="text-embedding-3-small"
    ),
)

with open("testdata.txt", "r", encoding="UTF-8") as f:
    text_data: list[str] = [line for line in f.read().splitlines() if line.strip()]


collection.upsert(ids=[str(uuid.uuid4()) for _ in text_data], documents=text_data)

# print(collection.peek())

ask_query = collection.query(
    query_texts=["what is the importance of drinking water?"],
)

print(ask_query)
