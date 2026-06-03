from autogen import AssistantAgent
from config import llm_config

gap_analyzer = AssistantAgent(
    name="GapAnalyzer",
    llm_config=llm_config,
    system_message="""
    Identify research gaps.

    Suggest future directions.
    """
)