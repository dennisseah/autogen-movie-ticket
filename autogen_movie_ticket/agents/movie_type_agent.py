from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient

from autogen_movie_ticket.tools.tools import available_movie_types

system_message = "You are an agent who provide a list of available types of movie. "
"Types are 2D, 3D, PG-13, Rated R."


def get_agent(llm_client: AzureOpenAIChatCompletionClient) -> AssistantAgent:
    return AssistantAgent(
        "movie_type_agent",
        model_client=llm_client,
        description="Movie type agent.",
        tools=[available_movie_types],
        system_message=system_message,
    )
