from agno.agent import Agent

from src.models.groq_models import llama
from src.agents.web_search_agent import web_search_agent
from src.agents.finance_agent import finance_agent

multi_ai_agent=Agent(model=llama,
                     instructions=["Always Include Sources","Use table to display the data"],
                     team=[web_search_agent,finance_agent],
                     show_tool_calls=True,
                     markdown=True)