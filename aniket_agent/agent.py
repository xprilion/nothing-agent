from google.adk.agents import Agent


root_agent = Agent(
    name="aniket_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to do nothing."
    ),
    instruction=(
        "You are a helpful agent who can do nothing."
    ),
    tools=[],
)