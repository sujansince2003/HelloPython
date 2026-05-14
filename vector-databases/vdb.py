import chromadb
from datetime import datetime


chroma_client = chromadb.Client()


# creating collection


my_collection = chroma_client.get_or_create_collection(
    name="my_embeddings_collection",
    metadata={
        "description": "my first Chroma collection",
        "created": str(datetime.now()),
    },
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

# print(my_collection.get())  #get collection data (docs,metadata)

results = my_collection.query(query_texts=["solana,bitcoins,anchor,"], n_results=5)

distance_value = results["distances"][0][0]
if distance_value > 1.5:
    print("I'm sorry, I couldn't find any documents related to your question.")
else:
    print(f"I found this: {results['documents'][0][0]}")


# creating non similarity query to test the embeddings
# results = my_collection.query(
#     query_texts=["How do I fix car in the middle of forest?"], n_results=2
# )
# print(results)
