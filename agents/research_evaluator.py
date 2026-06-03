from autogen import AssistantAgent
from config import llm_config

research_evaluator = AssistantAgent(
    name="ResearchEvaluator",
    llm_config=llm_config,
    system_message="""
    Evaluate research quality.

    Provide:
    - score
    - strengths
    - weaknesses
    - recommendations
    """
)