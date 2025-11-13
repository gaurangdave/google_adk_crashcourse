from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model="gemini-2.5-flash",
    name="hello_agent",
    description="A simple agent that can greet in multiple languagues",
    instruction="""Your are a simple helpful agent who first asks the user their name 
    and language preference, then greets them in that language""",
)
