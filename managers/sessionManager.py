from streamlit import session_state
from langchain_community.chat_message_histories import StreamlitChatMessageHistory


init_system_message=lambda: "You are helpful chat assistant. You will truthfully answer any questions I have. You will not hallucinate. YOu ask back questions for confirming any details you might think is relevant to know."
def init_states():
    state_items={
        # 'API_KEYS':dict,
        # 'messages':list,
        'system_message': init_system_message,
        'counter':int,
        'history':StreamlitChatMessageHistory
    }
    for item,Type in state_items.items():
        session_state[item]=Type() if item not in session_state else session_state[item]
        
