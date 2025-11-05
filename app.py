import streamlit as st

from dotenv import load_dotenv
load_dotenv(override=True)


from src.graphs.multi_ai_agent import multi_ai_agent



multi_ai_agent.print_response("nvidia stock price", stream=True)