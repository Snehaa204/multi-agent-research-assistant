from autogen import AssistantAgent
from config import llm_config

topic_refiner = AssistantAgent(
    name="TopicRefiner",
    llm_config=llm_config,
    system_message="""
    Refine research topics.

    Improve clarity.
    Improve scope.
    Improve specificity.
    """
)