from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
from datetime import datetime


def get_current_time() -> dict:
    """Gets the current time in the format YYYY-MM-DD HH:MM:SS
    """
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

root_agent = Agent(
    model="gemini-2.5-flash",
    name="custom_tools_agent",
    description="A fun assistant to make the day cheerful",
    instruction="""
    You are a helpful assitant that makes the users day cheerful. 
    Check the current time using the tools below and wish the user in a funny, whimsical way:
    - google_search
    """,
    tools=[get_current_time]
)
