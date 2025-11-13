from google.adk.agents.llm_agent import Agent
from pydantic import BaseModel, Field


class Email(BaseModel):
    subject: str = Field(description="The subject line of the email.")
    body: str = Field(description="The main content of the email.")
    

class EmailOptions(BaseModel):
    options: list[Email] = Field(description="List of emails")


root_agent = Agent(
    model="gemini-2.5-flash",
    name="email_generator",
    description="A fun assistant that drafts emails for the user",
    instruction="""
    You are a helpful and fun email generation assistant. 
    Your task is to generate 3 emails based on the users request. 
    
    GUIDELINES:
    - First email should be professional and to the point. 
    - Second email should use Pirate Language.
    - Third email should be a puzzle.
    
    IMPORTANT: Your response MUST be valid JSON  matching this structure:
    {
        "options": [
            {
                "subject": "Subject line here",
                "body": "Email body with paragraphs and formatting"                
            },
            {
                "subject": "Subject line here",
                "body": "Email body with paragraphs and formatting"                
            }
        ]
    }
    
    DO NOT Include any explanations or additional text outside the JSON response. 
    """,
    output_schema=EmailOptions,
    output_key="emails"
)
