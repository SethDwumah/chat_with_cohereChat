cohere_api_key='K9Is93rqVi3TXAoIvYgwJzuECMVIhLRzlzJ8r086'
import streamlit as st
from dotenv import load_dotenv
import os
from langchain_cohere import ChatCohere
from langchain.schema import SystemMessage, HumanMessage, AIMessage

def init():
    st.set_page_config(page_title="Chat with Cohere Chat Assistant", page_icon=":robot:")
    st.header("Chat with ReichRath, AI Assistant!")
    load_dotenv()

def main():
    init()

    cohere_api_key = os.getenv("COHERE_API_KEY")
    if not cohere_api_key:
        st.error("⚠️ Cohere API key not found. Please set COHERE_API_KEY in your .env file.")
        return

    chat = ChatCohere(
        model="command-r-plus-08-2024",
        temperature=0.75,
        cohere_api_key=cohere_api_key,
        max_tokens=256,
    )

    AI_message = """As an intelligent assistant, you are expected to provide highly relevant, concise, and accurate responses..."""

    if "messages" not in st.session_state:
        st.session_state.messages = [SystemMessage(content=AI_message)]

    user_input = st.chat_input("Ask anything", key="user_input")

    if user_input:
        st.session_state.messages.append(HumanMessage(content=user_input))

        try:
            response = chat(st.session_state.messages)
            ai_text = getattr(response, "content", str(response))
            st.session_state.messages.append(AIMessage(content=ai_text))
        except Exception as e:
            st.error(f"Error generating response: {str(e)}")

    # Display conversation
    for msg in st.session_state.messages[1:]:  # skip system message
        role = "user" if isinstance(msg, HumanMessage) else "assistant"
        with st.chat_message(role):
            st.markdown(msg.content)

if __name__ == "__main__":
    main()

   
