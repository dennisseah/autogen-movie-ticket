from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient

from autogen_movie_ticket.tools.tools import is_movie

system_message = """You are an agent who can provide verified movie name.
Response with the exact movie name if the given name is a movie in this json format:
```json
{
    "movie_name": "<exact movie name>"
}
```

if the given name is not a movie, response with an empty json object:
```json
{}
```
"""  # noqa E501


def get_agent(llm_client: AzureOpenAIChatCompletionClient) -> AssistantAgent:
    return AssistantAgent(
        "movie_name_agent",
        model_client=llm_client,
        description="Movie name agent.",
        tools=[is_movie],
        system_message=system_message,
    )
