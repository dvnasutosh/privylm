from dotenv import load_dotenv
import streamlit as st
from streamlit_extras.bottom_container import bottom

from components.dialogs import config_window
from components.message_boxes import chat_box
from managers.eventManager import chat_onsubmit
from managers.sessionManager import init_states

load_dotenv()

st.set_page_config('Privy Lm',layout="wide")
init_states()

title_col,config_col=st.columns([0.8,0.2],gap='medium',vertical_alignment='center')

config_col.container().button('Configure',on_click=config_window, use_container_width=True,type='primary')

title_col.write('<h1><center>PrivyLm Playground</center></h1>',unsafe_allow_html=True)

with st.container(key='chat-container'):
    # chat_disp_sect,chat_list_sect=st.columns([0.8,0.2])
    with st.expander('System Message'):
        chat_box()
    
    for each in st.session_state['langchain_messages']:
        with st.chat_message(each.type):
            st.write(each.content)

        

    
with bottom():

    query_col,file_col=st.container(key='query-pad-container',border=True).columns([0.8,0.2],vertical_alignment='bottom',gap='small')

    query=query_col.chat_input('Enter message...',key='query',on_submit=chat_onsubmit)

    
    




