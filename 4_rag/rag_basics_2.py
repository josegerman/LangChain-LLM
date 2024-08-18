# =====================================
# About:
# =====================================
# This code focuses on reading from the local chroma vector database and creating a basic query

# =====================================
# Required imports
# =====================================
import os

#from langchain_community.vectorstores import Chroma # <-- deprecated; using below instead
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

# =====================================
# OpenAI Key
# =====================================
os.environ["OPENAI_API_KEY"] = 'sk-proj-q5W3UsdLijEDNAV3HP45T3BlbkFJgVoJRzgYZCLuh4IELyuP'

# =====================================
# Define the persistent directory
# =====================================
current_dir = os.path.dirname(os.path.abspath(__file__))
persistent_directory = os.path.join(current_dir, "db", "chroma_db")

# =====================================
# Define the embedding model
# =====================================
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# =====================================
# Load the existing vector store with the embedding function
# =====================================
db = Chroma(persist_directory=persistent_directory,
            embedding_function=embeddings)

# =====================================
# Define the user's question
# =====================================
query = "Who is Odysseus' wife?"

# =====================================
# Retrieve relevant documents based on the query;
# k = # of documents to retrieve; higher value of threshold = more extringent to query
# =====================================
retriever = db.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"k": 3, "score_threshold": 0.2},
)
relevant_docs = retriever.invoke(query)

# =====================================
# Display the relevant results with metadata
# =====================================
print("\n--- Relevant Documents ---")
for i, doc in enumerate(relevant_docs, 1):
    print(f"Document {i}:\n{doc.page_content}\n")
    if doc.metadata:
        print(f"Source: {doc.metadata.get('source', 'Unknown')}\n")