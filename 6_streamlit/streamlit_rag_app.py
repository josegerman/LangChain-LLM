# ==================================
# About:
# ==================================
# RAG application using Langchain, GPT4(OpenAI), streamlit, python

# ==================================
# Imports
# ==================================
import os

from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# ==================================
# Load the variables from .env
# ==================================
load_dotenv()

st.write("Hello, Metadocs readers!")

template = """Answer the following question
Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

model = ChatOpenAI(temperature=0, model_name="gpt-4", openai_api_key=os.environ["OPENAI_API_KEY"])

result = model.invoke("What is langchain framework in the context of Large Language Models ?")

st.write("What is the langchain framework in the context of Large Language Models ?")
st.write(result.content)



# ==================================
# Run streamlit app
# ==================================
# streamlit run C:\_DEV\VSCode\Workspaces\lanchain-llm\6_streamlit\streamlit_rag_app.py


