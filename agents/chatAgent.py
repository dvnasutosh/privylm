# chat_agent.py
from langchain_google_genai import ChatGoogleGenerativeAI



from langchain_core.messages import  SystemMessage

from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.prompts import MessagesPlaceholder
from langchain.prompts import ChatPromptTemplate
from streamlit import session_state
def chat_agent(query: str, system_message: str):
    """
    Uses ChatGoogleGenerativeAI to generate a response while persisting
    the conversation history using StreamlitChatMessageHistory.
    """
    # loading llm 
    llm = ChatGoogleGenerativeAI(model='models/gemini-2.0-flash',)
    # Load (or create) the conversation history using a fixed key.
    prompt=ChatPromptTemplate.from_messages(
        [SystemMessage(system_message),
        MessagesPlaceholder(variable_name='chat_history'),
        ("human", "{input}"),]
    )

    chain=prompt|llm

    chain_with_history=RunnableWithMessageHistory(
        runnable=chain,
        get_session_history=lambda session_id: session_state.history,
        input_messages_key='input',
        history_messages_key='chat_history'
    )
    
    chain_with_history.invoke(input={"input":query},config={'session_id':'any'})
    
