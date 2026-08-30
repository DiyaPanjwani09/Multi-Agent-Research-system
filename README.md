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

## Commands

### Local Development

```bash
# Clone
git clone https://github.com/DiyaPanjwani09/Multi-Agent-Research-system.git
cd Multi-Agent-Research-system

# Create & activate virtual environment
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run Streamlit UI
streamlit run app.py

# Run CLI pipeline (no UI)
python pipeline.py
```

### Docker

```bash
# Build image
docker build -t researchmind .

# Run container
docker run -p 8501:8501 --env-file .env researchmind
```

### Streamlit Cloud / Deployment

```bash
# Specify Python version (add to Streamlit Cloud settings)
python --version

# Install deps (if build fails)
pip install --no-cache-dir -r requirements.txt

# Start command for most platforms
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

### Environment Variables

```bash
# Set env vars manually (alternative to .env)
export TAVILY_API_KEY="tvly-dev-..."
export MISTRAL_API_KEY="..."

# Windows PowerShell
$env:TAVILY_API_KEY="tvly-dev-..."
$env:MISTRAL_API_KEY="..."
```

### Useful Commands

```bash
# Check installed packages
pip list

# Verify Tavily key works
python -c "from tavily import TavilyClient; import os; from dotenv import load_dotenv; load_dotenv(); t=TavilyClient(api_key=os.getenv('TAVILY_API_KEY')); print(t.search('test', max_results=1))"

# Verify Mistral key works
python -c "from langchain_mistralai import ChatMistralAI; from dotenv import load_dotenv; import os; load_dotenv(); llm=ChatMistralAI(model='mistral-small-latest', api_key=os.getenv('MISTRAL_API_KEY')); print(llm.invoke('Say hi'))"

# Lint / format (if adding ruff)
pip install ruff
ruff check .
ruff format .

# Git push after changes
git add -A && git commit -m "message" && git push
```

### Platform-Specific Start Commands

| Platform | Start Command |
|----------|---------------|
| **Streamlit Cloud** | `streamlit run app.py` |
| **Heroku** | `streamlit run app.py --server.port $PORT` |
| **Railway** | `streamlit run app.py --server.port $PORT --server.address 0.0.0.0` |
| **Render** | `streamlit run app.py --server.port $PORT --server.address 0.0.0.0` |
| **AWS ECS / EC2** | `streamlit run app.py --server.port 8501 --server.address 0.0.0.0` |
| **GCP Cloud Run** | `streamlit run app.py --server.port $PORT --server.address 0.0.0.0` |
| **Docker** | `streamlit run app.py --server.port 8501 --server.address 0.0.0.0` |
| **CLI only** | `python pipeline.py` |

## License

MIT
