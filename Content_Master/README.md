# ContentMaster AI Agent

LangGraph-powered agent that combines web search and AI content generation.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# Add your OpenAI API key to .env
```

## Usage

```bash
python run.py
```

## Features

- 8-node LangGraph workflow
- Web search with source verification  
- Multi-format content generation (presentations, documents, webpages)
- Visual creation (charts, diagrams)
- Template selection
- Quality control with retry logic

## Files

- `content_master.py` - Main workflow
- `state.py` - State management
- `run.py` - Interactive runner
- `test_content_master.py` - Test suite
- `visualize_workflow.py` - Workflow diagram 