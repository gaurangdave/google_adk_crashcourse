from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

root_agent = Agent(
    model="gemini-2.5-flash",
    name="google_search_agent",
    description="A helpful assistant that searches for restaurants",
    instruction="""
    You are a helpful assitant that helps plan meals. 
    Ask the user if they are hungry, then ask them what kind of food they are craving and their location.
    Suggest 5 restaurants using the using the following tools:
    - google_search
    """,
    tools=[google_search]
)
