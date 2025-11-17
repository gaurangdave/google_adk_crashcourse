
from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent
from google.adk.tools.agent_tool import AgentTool

from .sub_agents.funny_agent.agent import funny_agent
from .sub_agents.pirate_translator_agent.agent import pirate_translator_agent

load_dotenv()


root_agent = Agent(
    model="gemini-2.5-flash",
    name="manager",
    description="",
    instruction="""You are a highly efficient and intelligent task manager. Your sole purpose is to analyze a user's request and delegate the task to the correct tool.

        2.  **Joke Intent:** If the user's request is about getting a joke (e.g., "make me laugh", "tell me a funny", "joke about dogs"):
            * Identify any topics.
            * Delegate to the `funny_agent`.

        3.  **Pirate Intent:** If the user's request is about pirate translation (e.g., "say ... like a pirate", "translate this to pirate", "pirate version of..."):
            * Identify the exact sentence(s) to translate.
            * Delegate to pirate_translator_agent

        4.  **Fallback (Out of Scope):** If the request is **not** about jokes or pirate translation (e.g., "what's the weather?", "how are you?", "summarize this text"), you **MUST NOT** call any tool. Instead, you must respond directly with a polite refusal.
        """,
    sub_agents=[pirate_translator_agent, funny_agent],
    # tools=[AgentTool(funny_agent)]

)
