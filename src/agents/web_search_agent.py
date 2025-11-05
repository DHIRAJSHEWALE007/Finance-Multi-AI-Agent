from agno.agent import Agent

from src.models.groq_models import llama
from src.tools.tools import duckduckgo_search_tool

web_search_agent=Agent(model=llama,
            name="web searcher Agent",
            role="give proper response to user querys",
            tools=[duckduckgo_search_tool],
            instructions=["Always Include Sources"],
            markdown=True,
            show_tool_calls=True)