import asyncio

from autogen_agentchat.agents import UserProxyAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.ui import Console

from autogen_movie_ticket.agents.customer_agent import get_agent as get_customer_agent
from autogen_movie_ticket.agents.movie_name_agent import (
    get_agent as get_movie_name_agent,
)
from autogen_movie_ticket.agents.num_ticket_verifier_agent import (
    get_agent as get_num_ticket_verifier_agent,
)
from autogen_movie_ticket.hosting import container
from autogen_movie_ticket.protocols.i_azure_openai_service import IAzureOpenAIService

llm_client = container[IAzureOpenAIService].get_model()

selector_prompt = """Select an agent to perform task.

{roles}

Current conversation context:
{history}

Read the above conversation, then select an agent from {participants} to perform the
next task.
Make sure the planner agent has assigned tasks before other agents start working.
Only select one agent.
"""


async def main():
    customer_agent = get_customer_agent(llm_client)
    movie_name_agent = get_movie_name_agent(llm_client)
    num_ticket_verifier_agent = get_num_ticket_verifier_agent(llm_client)
    user_proxy = UserProxyAgent("user_proxy", input_func=input)

    termination = TextMentionTermination("TERMINATE")
    team = SelectorGroupChat(
        [customer_agent, movie_name_agent, num_ticket_verifier_agent, user_proxy],
        model_client=llm_client,
        termination_condition=termination,
        selector_prompt=selector_prompt,
        allow_repeated_speaker=True,  # Allow an agent to speak multiple turns in a row.
    )

    result = await Console(
        team.run_stream(
            task="Hello",
        )
    )

    for message in result.messages:
        if message.models_usage:
            print(f"{message.source}: {message.models_usage}")


if __name__ == "__main__":
    asyncio.run(main())
