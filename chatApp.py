import streamlit as st
from dotenv import load_dotenv
import os
from langchain.chains import ConversationChain
from langchain_community.llms import Cohere
from langchain_community.chat_models import ChatCohere
from langchain.memory import ConversationBufferMemory
from streamlit_chat import message
from langchain.schema import SystemMessage, HumanMessage, AIMessage

def init():
    st.set_page_config(page_title="Chat with Cohere Chat Assistant", page_icon=":robot:")
    st.header("Chat with Sethyne, AI Assistant!")
    load_dotenv()
    

def main():

    init()
    

    chat = ChatCohere(model='command', temperature=0.75, cohere_api_key='KLxxk4D5YgzHbisanSwQe5nWIBCuLIUC6gCbxAyF',max_token=551)

    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="You are a helpful assistant, called Sethyne")
        ]

    #with st.sidebar:
    user_input = st.chat_input("Ask anything", key='user_input')

    if user_input:
        st.session_state.messages.append(HumanMessage(content=user_input))
        #with st.spinner("Thinking..."): 
        response = chat(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=response.content))

    placeholder = st.empty()
    with placeholder.container():

        messages = st.session_state.get('messages', [])
        for i, msg in enumerate(messages[1:]):
            if i % 2 == 0:
                message(msg.content, is_user=True, key=str(i) + '_user')
            else:
                message(msg.content, is_user=False, key=str(i) + '_ai')

if __name__ == '__main__':
    main()
