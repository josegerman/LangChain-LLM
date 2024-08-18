# =====================================
# About:
# =====================================
# 

# =====================================
# Required libraries:
# =====================================
# pip install langchainhub # <-- deprecated; need to use langsmith sdk
# pip install langsmith

# =====================================
# Required imports
# =====================================
import os

from dotenv import load_dotenv
from langchain import hub # <-- deprecated; need to use langsmith sdk
from langchain.agents import (
    AgentExecutor,
    create_react_agent,
)
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI

# =====================================
# OpenAI Key
# =====================================
# Load environment variables from .env
load_dotenv()

# Load environment variables from .env file
#load_dotenv() # <-- used when openai key is held in .env


# Define a very simple tool function that returns the current time
def get_current_time(*args, **kwargs):
    """Returns the current time in H:MM AM/PM format."""
    import datetime  # Import datetime module to get current time

    now = datetime.datetime.now()  # Get current time
    return now.strftime("%I:%M %p")  # Format time in H:MM AM/PM format


# List of tools available to the agent
tools = [
    Tool(
        name="Time",  # Name of the tool
        func=get_current_time,  # Function that the tool will execute
        # Description of the tool
        description="Useful for when you need to know the current time",
    ),
]

# Pull the prompt template from the hub
# ReAct = Reason and Action
# https://smith.langchain.com/hub/hwchase17/react
prompt = hub.pull("hwchase17/react")


# Initialize a ChatOpenAI model
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Create the ReAct agent using the create_react_agent function
agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt,
    stop_sequence=True,
)

# Create an agent executor from the agent and tools
agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent,
    tools=tools,
    verbose=True,
)

# Run the agent with a test query
response = agent_executor.invoke({"input": "What time is it?"})

# Print the response from the agent
print("response:", response)

# =====================================
# Notes:
# =====================================
# langchainhub sdk is deprecated; must use langsmith skd; pip install langsmith