from autogen import AssistantAgent
from config import llm_config

paper_discovery_agent = AssistantAgent(
    name="PaperDiscoveryAgent",
    llm_config=llm_config,
    system_message="""
    Search and summarize research papers.

    Use Arxiv findings.
    """
)