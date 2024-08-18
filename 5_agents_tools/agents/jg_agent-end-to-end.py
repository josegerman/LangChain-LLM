# =====================================
# About:
# =====================================
# This code demostrates how to create an agent along with memory checkpointer and tools. These type of agents are stateless
# which means it does not remember previous interactions. The tools in this example is basically a call to a weather lookup
# service. The agent decides when to go and use the tool based on the query from the user.

# =====================================
# Import relevant functionality
# =====================================
from dotenv import load_dotenv
#from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

# =====================================
# Load environment variables from .env
# =====================================
load_dotenv()

# =====================================
# Create the agent
# =====================================
memory = MemorySaver()
#model = ChatAnthropic(model_name="claude-3-sonnet-20240229")
model = ChatOpenAI(model="gpt-3.5-turbo")
search = TavilySearchResults(max_results=2)
tools = [search]
agent_executor = create_react_agent(model, tools, checkpointer=memory)

# =====================================
# Use the agent
# =====================================
config = {"configurable": {"thread_id": "abc123"}}
def continual_chat():
    print("Start chatting with the AI! Type 'exit' to end the conversation.")
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break
        for chunk in agent_executor.stream({"messages": [HumanMessage(content=query)]}, config
        ):
            print(f"AI: {chunk}")

# =====================================
# Main function to start the continual chat
# =====================================
if __name__ == "__main__":
    continual_chat()