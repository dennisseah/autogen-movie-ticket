from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient

from autogen_movie_ticket.tools.tools import verify_ticket_count

system_message = """You are an agent who can provide verified the number of ticket to be purchased.
Response with the number of tickets if the given number is valid in this json format:
```json
{
    "ticket_count": <number of tickets>
}
```

if the provided number of tickets is invalid, response with an empty json object:
```json
{
    "error": <error message>
}
```
"""  # noqa E501


def get_agent(llm_client: AzureOpenAIChatCompletionClient) -> AssistantAgent:
    return AssistantAgent(
        "num_ticket_verifier_agent",
        model_client=llm_client,
        description="Movie name agent.",
        tools=[verify_ticket_count],
        system_message=system_message,
    )
