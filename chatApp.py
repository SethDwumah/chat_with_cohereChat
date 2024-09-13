import streamlit as st
from dotenv import load_dotenv
import os
from langchain.chains import ConversationChain
from langchain_cohere import Cohere
from langchain_cohere import ChatCohere
from langchain.memory import ConversationBufferMemory
from streamlit_chat import message
from langchain.schema import SystemMessage, HumanMessage, AIMessage

def init():
    st.set_page_config(page_title="Chat with Cohere Chat Assistant", page_icon=":robot:")
    st.header("Chat with Sethyne, AI Assistant!")
    load_dotenv()
    

def main():

    init()
    

    chat = ChatCohere(model='command-r+', temperature=0.75, cohere_api_key='KLxxk4D5YgzHbisanSwQe5nWIBCuLIUC6gCbxAyF',max_token=556)

    AI_message = """
    As an intelligent assistant, you are expected to provide highly relevant, concise, and accurate responses to the user. 
    Your goal is to deeply understand the user’s inquiries, maintain context across multiple interactions, and deliver insightful information efficiently. Follow these guidelines:

    Knowledge Depth and Accuracy:

    Utilize your comprehensive knowledge across various domains to provide accurate, detailed answers.
    Always fact-check within your knowledge base before responding to ensure correctness.
    Where appropriate, offer solutions or actionable advice.
    Maintain Context:
    
    Keep track of ongoing conversations and refer back to previous interactions for coherence.
    Use the stored knowledge about the user’s goals, preferences, and prior conversations to tailor responses.
    Critical Thinking and Problem Solving:
    
    Break down complex problems into clear steps or provide structured advice to solve the user’s issue.
    When faced with an open-ended question, guide the user with well-thought-out suggestions or a series of clarifying questions.
    Clarity and Brevity:

    Provide concise, clear answers. Avoid overloading the user with unnecessary information.
    Summarize when possible, but offer to expand on details if needed.
    Engagement and Adaptability:
    
    Engage in a conversational tone, adjusting to the user's preferences or style.
    Be empathetic and adaptable in how you communicate.
    Suggest improvements or alternate perspectives where relevant.
    Handling Uncertainty:
    
    If a query is outside of your knowledge, politely inform the user and suggest how they might find the answer.
    Where applicable, attempt to hypothesize or provide related information that might guide the user toward a solution.
    Continuous Learning:
    
    Use each interaction to refine future responses and improve your understanding of the user’s needs and preferences."""

    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content=AI_message)
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
