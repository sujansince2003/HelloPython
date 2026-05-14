import chromadb
import os
import uuid
from dotenv import load_dotenv
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from openai import OpenAI

load_dotenv()
openai_client = OpenAI(api_key=os.getenv("OPEN_AI_API_KEY"))

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
def ask_query(query):
    results = collection.query(
        query_texts=["what is the importance of drinking water?"], n_results=3
    )
    db_context = "\n".join(results["documents"][0])
    llm_response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Answer the question using only the provided context.",
            },
            {"role": "user", "content": f"Context:\n{db_context}\n\nQuestion: {query}"},
        ],
    )
    print(llm_response.choices[0].message.content)


def main():
    while True:
        user_query = str(input("what is your query:\n"))
        ask_query(user_query)


main()
