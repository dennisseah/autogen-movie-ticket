from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient

from autogen_movie_ticket.tools.tools import available_dates

system_message = "You are an agent who provide a list of available dates of movie."


def get_agent(llm_client: AzureOpenAIChatCompletionClient) -> AssistantAgent:
    return AssistantAgent(
        "movie_dates_agent",
        model_client=llm_client,
        description="Movie dates agent.",
        tools=[available_dates],
        system_message=system_message,
    )
