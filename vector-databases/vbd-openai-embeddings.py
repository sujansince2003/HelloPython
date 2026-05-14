from dotenv import load_dotenv
import os
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
import chromadb
from datetime import datetime

load_dotenv()
# chromadb client

chroma_client = chromadb.Client()


my_collection = chroma_client.get_or_create_collection(
    name="my_embeddings_collection",
    metadata={
        "description": "my first Chroma collection",
        "created": str(datetime.now()),
    },
    embedding_function=OpenAIEmbeddingFunction(
        api_key=os.getenv("OPEN_AI_API_KEY"), model_name="text-embedding-3-small"
    ),
)


my_collection.upsert(
    documents=[
        "Javascript is the programming language use to build web apps",
        "Python is good for AIML",
        "Golang for backend",
        "Rust for blockchain",
    ],
    ids=["id1", "id2", "id3", "id4"],
)
results = my_collection.query(query_texts=["fastapi"], n_results=5)

distance_value = results["distances"][0][0]
if distance_value > 1.5:
    print("I'm sorry, I couldn't find any documents related to your question.")
else:
    print(f"I found this: {results['documents'][0][0]}")
