from agno.agent import Agent

from src.models.groq_models import llama
from src.tools.tools import yfinance_tool

finance_agent=Agent(model=llama,
            name="Finance Advisor Agent",
            role="give proper response to user querys",
            tools=[yfinance_tool],
            instructions=["Always Include Sources"],
            markdown=True,
            show_tool_calls=True)