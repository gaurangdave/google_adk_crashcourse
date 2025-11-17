from google.adk.agents.llm_agent import Agent
from google.adk.agents.callback_context import CallbackContext

# from pydantic import BaseModel,Field
from google.adk.tools.tool_context import ToolContext
from google.adk.tools.function_tool import FunctionTool
from typing import Any

def add_jokes_to_state(jokes: list[str], tool_context: ToolContext):
    """Saves the newly written jokes to the sate

    Args:
        jokes (list[str]): list of jokes to save
    """
    existing_jokes = tool_context.state.get("jokes", [])
    updated_jokes = existing_jokes + jokes
    ## update the state 
    tool_context.state["jokes"] = updated_jokes
    return {
        "status": "success",
        "message": "newly written jokes have been saved"    
    }
    

    
funny_agent = Agent(
    model="gemini-2.5-flash",
    name="funny_agent",
    description="Generates a list of one-liner jokes. It can generate jokes for a provided list of topics or, if no topics are given, will generate a single random one-liner.",
    instruction="""You are a witty and clever stand-up comedian. Your job is to generate one-liner jokes. 

    You will receive topics from the state variable `{topics?}`.

    ## Your Logic:
    1.  **If the `{topics?}` variable exists and contains one or more topics:** You must generate **one** concise, one-liner joke for **each** topic in the list.
    2.  **If the `{topics?}` variable is empty or not provided:** You must generate **exactly one** one-liner joke on a random topic of your choosing (e.g., programming, animals, food, etc.).

    ## Constraints:
    * **Strictly One-Liners:** Do not provide long jokes or stories.
    * **No Banter:** Do not add any greetings, commentary, or extra text like "Here are your jokes!" or "I hope you like this one!". Your response must *only* contain the jokes.

    Once the joke is generated use the following tool to save the joke.
    
    - add_jokes_to_state : saves the generated joke for the user
    
    Update the user that the joke has been saved and delegate back to the "manager" agent
    """,
    output_key="jokes",
    tools=[FunctionTool(add_jokes_to_state)],
)
