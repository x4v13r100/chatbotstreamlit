import streamlit as st
#from langchain_openai import OpenAI
from langchain_community.llms import Ollama

llm =  Ollama(model="phi3", temperature=0)
#llm =  Ollama(model="llama3", temperature=0)
#llm =  OpenAI(model="gpt-3.5-turbo", temperature=0, api_key="OPENAI_API_KEY")

st.title("ChatBot phi3")

messages = [("system", "Eres un chatbot AI util, te llamas Dana.")]

# Inicializar historial
if "messages" not in st.session_state:
    st.session_state.messages = []
    
# Mostrar mensajes de chat del historial al recargar la app
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
# Reaccionar a la entrada
if prompt := st.chat_input("Escribe tu mensaje"):
    # Mostrar mensaje del usuario en el contenedor de chat
    st.chat_message("user").markdown(prompt)
    # Agregar mensaje del usuario al historial
    st.session_state.messages.append({"role": "user", "content": prompt})
    messages.append(["human", prompt])
    
    response = llm.invoke(messages)
    # Mostrar respuesta del asistente en el contenedor de mensajes de chat
    with st.chat_message("assistant"):
        st.markdown(response)
    # Agrega respuesta del asistente al historial de chat
    st.session_state.messages.append({"role": "assistant", "content": response})
    
### streamlit run main.py