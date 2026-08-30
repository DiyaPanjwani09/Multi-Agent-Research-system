# ResearchMind - Multi-Agent Research System

A multi-agent AI system where four specialized agents collaborate to produce polished research reports on any topic. Built with LangChain, Mistral AI, and Streamlit.

## Architecture

```
User Input (Topic)
       |
       v
  ┌─────────────┐
  │ Search Agent │ ── Tavily web search for recent info
  └──────┬──────┘
         v
  ┌─────────────┐
  │ Reader Agent│ ── Scrapes top URLs for deeper content
  └──────┬──────┘
         v
  ┌─────────────┐
  │ Writer Chain│ ── Drafts a structured research report
  └──────┬──────┘
         v
  ┌─────────────┐
  │ Critic Chain│ ── Reviews and scores the report
  └─────────────┘
```

## Agents

| Agent | Role | Tools |
|-------|------|-------|
| **Search Agent** | Finds recent, reliable web information | Tavily Search API |
| **Reader Agent** | Scrapes and extracts deep content from URLs | BeautifulSoup scraping |
| **Writer Chain** | Drafts structured research reports | LLM (Mistral) |
| **Critic Chain** | Reviews, scores, and provides feedback | LLM (Mistral) |

## Tech Stack

- **LLM**: Mistral AI (`mistral-small-latest`)
- **Agent Framework**: LangChain + LangGraph
- **Web Search**: Tavily API
- **Scraping**: BeautifulSoup + requests
- **UI**: Streamlit

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/DiyaPanjwani09/Multi-Agent-Research-system.git
cd Multi-Agent-Research-system
```

### 2. Create a virtual environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API keys

Create a `.env` file in the project root:

```
TAVILY_API_KEY=your-tavily-api-key
MISTRAL_API_KEY=your-mistral-api-key
```

Get your keys:
- **Tavily**: [tavily.com](https://tavily.com) (free tier available)
- **Mistral**: [console.mistral.ai](https://console.mistral.ai)

### 5. Run the app

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`.

## Project Structure

```
.
├── app.py              # Streamlit UI and pipeline orchestration
├── agents.py           # Agent and chain definitions (Search, Reader, Writer, Critic)
├── tools.py            # Tool implementations (web_search, scrape_url)
├── pipeline.py         # CLI version of the research pipeline
├── requirements.txt    # Python dependencies
├── .env                # API keys (not committed)
└── .gitignore          # Git ignore rules
```

## Usage

1. Enter a research topic in the text input (e.g., "Quantum computing breakthroughs in 2025")
2. Click **Run Research Pipeline**
3. Watch each agent execute in sequence
4. View the final report with critic feedback
5. Download the report as a Markdown file

## License

MIT
