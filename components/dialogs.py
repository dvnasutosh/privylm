
from streamlit import dialog, fragment, session_state,text_input,container, write,button

@fragment(run_every=1)
@dialog('Configurations',width='large')
def config_window():

    data=session_state['API_KEYS']
    
    write(session_state['API_KEYS'])

    with container(border=True):
        write('# LLM Setup')
        data['MISTRAL_API_KEY']=text_input('MISTRAL_API_KEY')
        data['OPENAI_API_KEY']=text_input('OPENAI_API_KEY')
        data['GOOGLE_API_KEY']=text_input('GOOGLE_API_KEY')
        data['GROQ_API_KEY']=text_input('GROQ_API_KEY')
        data['ANTHROPIC_API_KEY']=text_input('ANTHROPIC_API_KEY')
        
    with container(border=True):
        write('# Data Storage Setup')
        data['MONGO_STRING']=text_input('MONGO_STRING')  
        data['PINECONE_API_KEY']=text_input('PINECONE_API_KEY')
        data['NEO4J_HOST']=text_input('NEO4J_HOST')
        data['NEO4J_USER']=text_input('NEO4J_USER')
        data['NEO4J_PASSWORD']=text_input('NEO4J_PASSWORD')
    with container(border=True):
        write('Tools for AI to Use')
        data['RIZA_API_KEY']=text_input('RIZA_API_KEY')
        data['TAVILY_API_KEY']=text_input('TAVILY_API_KEY')
    if button('Set',use_container_width=True):
        session_state['API_KEYS']=data


# I have 2 options
    # 1 to create config secure api and  store it in a database in our backend or store the same thing in cookies in their local databases. FOr now cookie seem to be way. Only problem is on refresh it restarts.
    # give second option. Login get login token (available for 1 day) access the dataset as is. (This will be implemented later on)
    