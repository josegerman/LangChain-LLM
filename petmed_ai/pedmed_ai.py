# =====================================
# About:
# =====================================
# Date: 2023-08-11
# Developer: Jose German
# Code: This code builds a retriever tools which is called by the agent; The data is read from the diseases csv file

# =====================================
# Required imports
# =====================================
import os

from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools.retriever import create_retriever_tool
from langchain_core.tools import Tool
from langchain_chroma import Chroma
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import HumanMessage # added
from langchain import hub # added
#from langgraph.checkpoint.sqlite import SqliteSaver # requires separate library
#from langgraph.prebuilt import create_react_agent
from langchain_community.document_loaders.csv_loader import CSVLoader # added
from langchain_openai import ChatOpenAI

# =====================================
# OpenAI Key
# =====================================
# Load environment variables from .env file
load_dotenv()

# =====================================
# Load, chunk and index the contents of the CSV.
# =====================================
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "docs", "DogsCatsDiseases.csv")
loader = CSVLoader(file_path)
documents = loader.load()

# =====================================
# Create Chroma vector database
# =====================================
vectorstore = Chroma.from_documents(documents=documents, embedding=OpenAIEmbeddings()) # using chroma vectorstore

# =====================================
# Construct retriever
# =====================================
retriever = vectorstore.as_retriever()

# =====================================
# List tools available to the agent
# =====================================
tool = create_retriever_tool(
    retriever,
    "pet_diagnosis_retriever",
    "Searches and returns pet diagnosis.",
)
tools = [tool]

# =====================================
# Pull prompt
# =====================================
prompt = hub.pull("vetincharge/petdiag")

# =====================================
# Initialize a ChatOpenAI model
# =====================================
llm = ChatOpenAI(model="gpt-4o", temperature=0) # model

# =====================================
# Create the ReAct agent using the create_react_agent function
# =====================================
agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt,
    stop_sequence=True,
)

# =====================================
# Create an agent executor from the agent and tools
# =====================================
agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent,
    tools=tools,
    verbose=True,
)

# =====================================
# Run the agent with a test query
# =====================================
#response = agent_executor.invoke({"input": "What is Anaplasmosis??"})
response = agent_executor.invoke({"input": "My dog is coughing a lot?"})


# =====================================
# Print the response from the agent
# =====================================
print("response:", response)

# =====================================
# Notes:
# =====================================
# 