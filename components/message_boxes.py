from streamlit import button, fragment, rerun, session_state,text_area


@fragment()
def chat_box():
    session_state.system_message=text_area('Enter system message...',value=session_state.system_message)
    if button('Set System Message'):
        rerun(scope='fragment')