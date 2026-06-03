from autogen import AssistantAgent
from config import llm_config

insight_synthesizer = AssistantAgent(
    name="InsightSynthesizer",
    llm_config=llm_config,
    system_message="""
    Combine research findings.

    Generate key insights.
    """
)