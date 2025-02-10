from streamlit import session_state

from agents.chatAgent import chat_agent
def chat_onsubmit():
    print('chat_onsubmit')
    chat_agent(query=session_state.query,system_message=session_state.system_message)


