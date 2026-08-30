from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, scrape_url
from dotenv import load_dotenv

load_dotenv()

# Model setup
llm = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0,
)


# Agent prompt template (shared base)
def _agent_prompt(system_message: str) -> ChatPromptTemplate:
    return ChatPromptTemplate.from_messages([
        ("system", system_message),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])


# 1st Agent - Web Search Agent
def build_search_agent():
    prompt = _agent_prompt(
        "You are a web search assistant. "
        "Use the web_search tool to find recent, reliable information on the given topic."
    )
    agent = create_tool_calling_agent(llm, [web_search], prompt)
    return AgentExecutor(agent=agent, tools=[web_search], verbose=False)


# 2nd Agent - Reader Agent
def build_reader_agent():
    prompt = _agent_prompt(
        "You are a content reader and scraper. "
        "Use the scrape_url tool to scrape and extract content from the most relevant URL."
    )
    agent = create_tool_calling_agent(llm, [scrape_url], prompt)
    return AgentExecutor(agent=agent, tools=[scrape_url], verbose=False)


# Writer Chain
writer_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an expert research writer. "
        "Write clear, structured and insightful research reports.",
    ),
    (
        "human",
        """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional.""",
    ),
])

writer_chain = writer_prompt | llm | StrOutputParser()


# Critic Chain
critic_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a sharp and constructive research critic. "
        "Be honest and specific.",
    ),
    (
        "human",
        """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
...""",
    ),
])

critic_chain = critic_prompt | llm | StrOutputParser()
