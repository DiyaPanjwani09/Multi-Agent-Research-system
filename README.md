# ResearchMind - Multi-Agent Research System

[![Live Demo](https://img.shields.io/badge/LIVE-Deployed-green)](https://researchmind-as9m.onrender.com/)

A multi-agent AI system where four specialized agents collaborate to produce polished research reports on any topic. Built with LangChain, Mistral AI, and Streamlit.

**Live App:** https://researchmind-as9m.onrender.com/

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

### Deploy on Render

#### Step 1: Push to GitHub

```bash
git add -A
git commit -m "Ready for deployment"
git push
```

#### Step 2: Create Web Service on Render

1. Go to [render.com](https://render.com) and sign in
2. Click **New** → **Web Service**
3. Connect your GitHub repo: `DiyaPanjwani09/Multi-Agent-Research-system`

#### Step 3: Configure Settings

| Field | Value |
|-------|-------|
| **Name** | `researchmind` |
| **Region** | Oregon (or closest to you) |
| **Branch** | `main` |
| **Runtime** | Python |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `streamlit run app.py --server.port $PORT --server.address 0.0.0.0` |
| **Python Version** | `3.11` (or `3.10` / `3.12`) |

#### Step 4: Add Environment Variables

In Render dashboard → **Environment** tab, add:

```
TAVILY_API_KEY    = tvly-dev-your-key-here
MISTRAL_API_KEY   = your-mistral-key-here
```

> **Important:** Do NOT put `.env` in your repo for Render. Use Render's Environment Variables section instead.

#### Step 5: Deploy

Click **Create Web Service**. Render will:
1. Pull your repo
2. Run `pip install -r requirements.txt`
3. Run `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`

Your app will be live at: `https://researchmind.onrender.com`

---

#### Render CLI Commands (Optional)

```bash
# Install Render CLI
npm install -g @anthropic-ai/render

# Login
render login

# Deploy from repo
render deploy

# Check logs
render logs --service researchmind

# Set env var via CLI
render env:set TAVILY_API_KEY=tvly-dev-xxx --service researchmind
render env:set MISTRAL_API_KEY=xxx --service researchmind
```

#### Troubleshooting Render

```bash
# If build fails, check Python version is set to 3.11+
# If app crashes, check logs:
render logs --service researchmind

# Common issues:
# 1. Missing env vars → Add them in Environment tab
# 2. Port conflict → Ensure start command uses $PORT
# 3. Dependency errors → Pin versions in requirements.txt
# 4. Free tier spins down after 15 min idle → Upgrade or add uptime pinger
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
