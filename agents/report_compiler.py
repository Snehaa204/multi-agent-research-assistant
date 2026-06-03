from autogen import AssistantAgent
from config import llm_config

report_compiler = AssistantAgent(
    name="ReportCompiler",
    llm_config=llm_config,
    system_message="""
    Generate final professional report.

    Include:
    - Executive Summary
    - Literature Review
    - Insights
    - Research Gaps
    - Evaluation
    - Recommendations
    """
)