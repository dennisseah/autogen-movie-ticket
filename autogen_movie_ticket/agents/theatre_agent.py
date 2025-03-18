from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient

from autogen_movie_ticket.tools.tools import available_theatres

system_message = (
    "You are an agent who provide a list of available theatres of a given movie name."
)


def get_agent(llm_client: AzureOpenAIChatCompletionClient) -> AssistantAgent:
    return AssistantAgent(
        "theatre_agent",
        model_client=llm_client,
        description="Theatre agent.",
        tools=[available_theatres],
        system_message=system_message,
    )
