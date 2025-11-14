import uuid
import asyncio

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from typing import Any
from about_me_agent import about_me_agent
load_dotenv()

# Create a new session service to store state
session_service_stateful = InMemorySessionService()

initial_state: dict[str,Any] = {
    "user_name": "Tony Stark",
    "user_dietary_preferences": ["pescatarian"],
    "user_allergies": ["gluten", "nuts"]
}

APP_NAME = "WIP"
USER_ID = "tony_h_stark"
SESSION_ID = str(uuid.uuid4())


async def main():
    ## this method creates and returns the newly created session
    await session_service_stateful.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
        state=initial_state
    )

    runner = Runner(
        agent=about_me_agent,
        app_name=APP_NAME,
        session_service=session_service_stateful,
    )

    new_message = types.Content(
        role="user", parts=[types.Part(text="what is user's name?")]
    )

    for event in runner.run(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=new_message,
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                print(f"Final Response: {event.content.parts[0].text}")
                
                
                
    new_message = types.Content(
            role="user", parts=[types.Part(text="Can Tony eat peanut butter and jelly sandwich as a snack?")]
        )

    for event in runner.run(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=new_message,
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                print(f"Final Response: {event.content.parts[0].text}")                

    print("==== Session Event Exploration ====")
    session = await session_service_stateful.get_session(
        app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
    )

    # Log final Session state
    print("=== Final Session State ===")
    if session is None:
        print("No session found.")
    else:
        for key, value in session.state.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    asyncio.run(main())