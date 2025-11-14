from google.adk.agents.llm_agent import Agent


about_me_agent = Agent(
    model="gemini-2.5-flash",
    name="about_me_agent",
    description="A helpful assitant that provides info about the user",
    instruction="""
    You are a helpful personal assistant answers questions about the user's preferences.
    
    Here is some information about the user
    Name : {user_name}
    Dietary Preferences : {user_dietary_preferences}
    Allergiese : {user_allergies}
    """,
)
