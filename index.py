from dotenv import load_dotenv
import streamlit as st

load_dotenv()
st.set_page_config('Privy Lm',layout='wide')
st.header('# PrivyLM')
c1,c2=st.columns([0.5,0.5])
c1.container(border=True).page_link('pages/SImple Chat Assistant.py',label='Instant Chat Assistant',use_container_width=True)