Hi, welcome to my GitHub!

In this repository you will find a few projects primarily demostrating LangChain capabilities along with OpenAI's LLM.
LangChain (https://www.langchain.com) is a large language model (LLM) integration framework. It allows developers to connect LLM with external data sources.
Some of its use-cases include chatbots, retrieval-augmented generation (RAG), document summarization and synthetic data generation.

1. Basic chat models
   1. Basic conversation with chat history.
   2. Save converation to a Google Firestore database. History is important for conversation to provide context to future questions.
3. Use of prompt templates
4. Chains
5. RAG using LangChain
   1. Basic RAG that focuses on reading a file (text in this case) and then chunking it and saving it into a local Chroma vector database.
   2. Second basic project that focuses on reading from the local Chroma vector database (created in previous project) and creating a basic query.
   3. Basic RAG conversation .
   4. Basic RAG which adds metadata to the Chroma vector database.
7. Agents and Tools
   1. Agents
         1. Basic agent ReAct (reasoning-action) chat with tools. Based on question, agent can decide to use one of two tools defined in code.
         2. Basic agent to use a local Chroma vector database.
         3. End-to-end agent converation with memory.
   3. Tools
9. Streamlit (will move to it's own repository)
   
