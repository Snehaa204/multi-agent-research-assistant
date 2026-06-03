from autogen import (
    GroupChat,
    GroupChatManager,
    UserProxyAgent
)

from agents.topic_refiner import topic_refiner
from agents.paper_discovery import paper_discovery_agent
from agents.web_researcher import web_researcher
from agents.insight_synthesizer import insight_synthesizer
from agents.gap_analyzer import gap_analyzer
from agents.research_evaluator import research_evaluator
from agents.report_compiler import report_compiler

from tools.report_saver import save_report
from tools.memory import save_memory

from config import llm_config


workflow_state = {
    "topic_approved": False,
    "papers_found": False,
    "insights_generated": False,
    "gaps_identified": False,
    "report_completed": False
}


user_proxy = UserProxyAgent(
    name="UserProxy",
    human_input_mode="NEVER",
    code_execution_config=False,
    system_message="""
    You are the human supervisor.
    Review outputs carefully.
    Approve, reject, or request modifications.
    """
)


agents = [
    topic_refiner,
    paper_discovery_agent,
    web_researcher,
    insight_synthesizer,
    gap_analyzer,
    research_evaluator,
    report_compiler
]


def custom_speaker_selection(last_speaker, groupchat):

    messages = groupchat.messages

    if last_speaker is user_proxy:
        
        print("Running Topic Refiner")

        return topic_refiner

    elif last_speaker is topic_refiner:

        workflow_state["topic_approved"] = True

        print("Running Paper Discovery")
        return paper_discovery_agent

    elif last_speaker is paper_discovery_agent:

        workflow_state["papers_found"] = True

        print("Running Web Researcher")
        return web_researcher

    elif last_speaker is web_researcher:

        print("Running Insight Synthesizer")
        return insight_synthesizer

    elif last_speaker is insight_synthesizer:

        workflow_state["insights_generated"] = True

        print("Running Gap Analyzer")
        return gap_analyzer

    elif last_speaker is gap_analyzer:

        workflow_state["gaps_identified"] = True

        print("Running Research Evaluator")
        return research_evaluator

    elif last_speaker is research_evaluator:

        print("Running Report Compiler")
        return report_compiler

    elif last_speaker is report_compiler:

        workflow_state["report_completed"] = True

        final_report = messages[-1]["content"]

        saved_file = save_report(final_report)

        save_memory(
            messages[0]["content"],
            final_report
        )

        print("\nFinal Workflow State:")
        print(workflow_state)

        print(f"\nReport saved to: {saved_file}")

        return None

    return None


groupchat = GroupChat(
    agents=agents,
    messages=[],
    max_round=15,
    speaker_selection_method=custom_speaker_selection
)

manager = GroupChatManager(
    groupchat=groupchat,
    llm_config=llm_config
)

