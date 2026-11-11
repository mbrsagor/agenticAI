# Learning Agentic AI with Python

This repository is a small, hands-on introduction to building AI applications with Python. It starts with validating structured data, then explores using a web-search tool and LangChain components.

## What you will learn

- **Structured data and validation:** define a data model with Pydantic and validate values before using them.
- **Tools:** call a search tool such as Tavily and inspect the results it returns.
- **Agent building blocks:** explore LangChain's model, tool, prompt, and agent APIs in the example notebook.
- **Secrets and configuration:** load API keys from a local `.env` file rather than putting them in source code.

An agentic application generally combines a language model with tools and instructions so it can choose or perform steps toward a task. Pydantic is useful alongside agents for validating structured inputs and outputs; it is not itself an AI agent.

## Repository contents

| File | What it demonstrates |
| --- | --- |
| [`module_pydantic.py`](./module_pydantic.py) | A Pydantic `EmployeeData` model, field constraints, typed fields, and example validation. Run it as a regular Python script. |
| [`done-examples/tavily_search.ipynb`](./done-examples/tavily_search.ipynb) | A minimal Tavily web-search example using LangChain's community integration. |
| [`resource/agent_demo.ipynb`](./resource/agent_demo.ipynb) | Imports LangChain's model and agent components and demonstrates a Tavily search. Use it to explore how these building blocks fit together. |
| [`requirements.txt`](./requirements.txt) | Python packages used by the examples. Package roles are described below. |

Notebook outputs are saved results from an earlier run; rerun the cells to make a fresh request and see current results.

## Prerequisites

- Python installed. The notebooks record Python 3.14.2 in their metadata, but this repository does not declare a tested Python-version range.
- Git.
- A Tavily API key to run the search notebooks.
- An OpenAI API key for examples that make requests to an OpenAI model.

The current search notebooks use Tavily. The agent notebook imports OpenAI/LangChain model components, but its visible example currently invokes the search tool directly.

## Setup

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/mbrsagor/agenticAI.git
cd agenticAI
python3 -m venv .venv
```

Activate it:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Configure API keys

Create a file named `.env` in the repository root:

```dotenv
TAVILY_API_KEY=your_tavily_api_key
OPENAI_API_KEY=your_openai_api_key
```

Only add the keys for services you plan to use. The repository's `.gitignore` excludes `.env`; keep your keys private and never commit them.

## Run the examples

Run the Pydantic example from the repository root:

```bash
python module_pydantic.py
```

To run a notebook, open it in VS Code with the Jupyter extension or in a Jupyter environment. Select the Python interpreter from `.venv`, and run the cells in order. Keep the notebook's working directory at the repository root so it can find `.env`. If you use the Jupyter command-line interface, install Jupyter in the virtual environment first:

```bash
python -m pip install jupyter
```

## What is in `requirements.txt`?

| Package | Purpose in this project |
| --- | --- |
| `pydantic` | Defines and validates structured data models, as shown in `module_pydantic.py`. |
| `langchain` | Provides LangChain's agent APIs and related framework functionality. |
| `langchain-core` | Shared LangChain abstractions, including messages, prompts, and tools. |
| `langchain-community` | Community integrations, including the Tavily search tool used by the notebooks. |
| `langchain-openai` | Connects LangChain to OpenAI chat models. |
| `tavily-python` | Tavily's Python client; the examples use the LangChain integration. |
| `duckduckgo-search` | Provides a DuckDuckGo search integration option; it is not used in the current example notebooks. |
| `requests` | Makes HTTP requests; it is imported in the agent demo notebook. |
| `python-dotenv` | Loads local environment variables from `.env`. |
| `langchainhub` | Supports retrieving and sharing LangChain prompts from LangChain Hub. |

Some package versions are pinned in `requirements.txt` and others are not, so an install may resolve differently over time. If installation fails, check that your Python version is compatible with the listed package versions.

## Suggested learning path

1. Run `module_pydantic.py`. Change a field or provide an invalid value and observe how validation behaves.
2. Read and run `done-examples/tavily_search.ipynb`. Notice the query passed to the tool and the results it returns.
3. Explore `resource/agent_demo.ipynb`. Identify the model, tool, prompt, and agent-related imports, then trace which ones the notebook actually uses.
4. Experiment with one small change at a time, and avoid putting API keys directly in notebook cells or Python files.
