# Multi-Agent Research Assistant Using AutoGen

## Overview

Multi-Agent Research Assistant (MARA) is an AI-powered research automation system designed to simulate a collaborative research workflow through multiple specialized agents. The system autonomously refines research topics, discovers relevant literature, gathers supporting information, synthesizes insights, identifies research gaps, evaluates findings, and generates structured reports.

The project demonstrates the application of agent-based orchestration using Microsoft's AutoGen framework combined with Large Language Models and modern web technologies.

---

## Motivation

Scientific and technical research often requires extensive literature review, information gathering, critical analysis, and report preparation. These tasks are time-consuming and repetitive.

This project explores how multiple autonomous AI agents can collaborate to perform different stages of the research process, reducing manual effort while maintaining a structured workflow.

---

## System Architecture

The system consists of seven specialized agents:

### Topic Refiner

Refines and clarifies the initial research query.

### Paper Discovery Agent

Identifies relevant academic papers and research sources.

### Web Researcher

Collects supporting information from external sources.

### Insight Synthesizer

Combines gathered information into meaningful insights.

### Gap Analyzer

Identifies unexplored areas and potential research opportunities.

### Research Evaluator

Assesses the quality and completeness of findings.

### Report Compiler

Generates a consolidated research report.

---

## Workflow

Research requests pass through the following pipeline:

Research Topic
→ Topic Refinement
→ Paper Discovery
→ Web Research
→ Insight Synthesis
→ Gap Analysis
→ Evaluation
→ Report Generation

Each agent performs a dedicated task and passes its output to the next stage of the workflow.

---

## Features

* Multi-agent research workflow
* Automated literature discovery
* Web-based information gathering
* Insight generation and synthesis
* Research gap identification
* Professional report generation
* Workflow progress tracking
* Interactive dashboard interface
* Report export and download functionality

---

## Technology Stack

### Backend

* Python
* FastAPI
* AutoGen
* OpenRouter API
* Pydantic

### Frontend

* HTML5
* CSS3
* JavaScript

### AI Components

* Large Language Models (LLMs)
* Agent Orchestration
* Prompt Engineering

---

## Project Structure

```text
multi_agent_research_assistant/

├── agents/
│   ├── topic_refiner.py
│   ├── paper_discovery.py
│   ├── web_researcher.py
│   ├── insight_synthesizer.py
│   ├── gap_analyzer.py
│   ├── research_evaluator.py
│   └── report_compiler.py
│
├── backend/
│   └── api.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
├── tools/
│   ├── arxiv_tool.py
│   ├── memory.py
│   └── report_saver.py
│
├── reports/
├── workflow.py
├── config.py
└── requirements.txt
```

---

## Key Contributions

* Designed a complete agent-based research pipeline.
* Implemented autonomous workflow coordination using AutoGen.
* Developed a responsive research dashboard.
* Integrated research report generation and export capabilities.
* Built an extensible architecture that supports additional agents and research tools.

---

## Sample Research Domains

The system can be used for:

* Artificial Intelligence
* Drug Discovery
* Machine Learning
* Cybersecurity
* Data Science
* Quantum Computing
* Software Engineering
* Emerging Technologies

---

## Future Scope

* Integration with vector databases for semantic retrieval.
* Research citation generation.
* Advanced report visualization.
* Multi-user collaboration support.
* Cloud deployment and scalability improvements.

---
