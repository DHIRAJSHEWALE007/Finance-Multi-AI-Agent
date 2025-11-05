from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools

duckduckgo_search_tool = DuckDuckGoTools()
yfinance_tool = YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True,company_news=True)