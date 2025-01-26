import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun,DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
import os
from dotenv import load_dotenv

# arxiv and wikipedia tools
api_wrapper_wiki = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=250)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper_wiki)

api_wrapper_arxiv = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=250)
arxiv = ArxivQueryRun(api_wrapper=api_wrapper_arxiv)

search=DuckDuckGoSearchRun(name="Run")

st.title("LangChain-Chat with search")
"""
In this example, we are using "StreamlitCallbackHandler" to display thoughts and actions of an interactive Streamlit app.

"""
# siderbar for settings 
st.sidebar.title("Settings")
api_key=st.sidebar.text_input("Enter your Groq API Key:",type="password")

if api_key:
    if "messages" not in st.session_state:
        st.session_state["messages"]=[
            {"role":"assistant","content":"Hi, I am a chatbot who can search the web. How can I help you?"}

        ]
    for msg in st.session_state.messages:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

    if prompt := st.chat_input(placeholder="What is machine learning?"):
        
        st.session_state.messages.append({"role":"user","content":prompt})
        st.chat_message("user").write(prompt)


        llm=ChatGroq(groq_api_key=api_key,model_name="llama3-8b-8192",streaming=True)
        tools=[search,arxiv,wiki]

        search_agent=initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,handling_parsing_errors=True)

        with st.chat_message("assistant"):
            st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
            response=search_agent.run(st.session_state.messages,callbacks=[st_cb])
            st.session_state.messages.append({"role":"assistant","content":response})
else:
    st.warning("Please enter your GROQ API key")

        
 