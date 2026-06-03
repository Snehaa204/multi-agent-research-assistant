from autogen import AssistantAgent
from config import llm_config

web_researcher = AssistantAgent(
    name="WebResearcher",
    llm_config=llm_config,
    system_message="""
    Research latest developments.

    Use web sources.
    Find industry trends.
    """
)