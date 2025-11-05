import streamlit as st

from dotenv import load_dotenv
load_dotenv(override=True)


from src.graphs.multi_ai_agent import multi_ai_agent

st.title("Multi-Agent System")

query = st.text_input("Ask a question:")

if query:
    with st.spinner("Processing..."):

        response = multi_ai_agent.print_response(query, stream=True)
        
        st.markdown(response)