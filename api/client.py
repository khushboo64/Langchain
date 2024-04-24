import requests
import streamlit as st

def get_Openai_response(input_text):
    response=requests.post("http://locallhost:8000/essay/invoke",
                           json={'input':{'topic':input_text}})
    return response.json()['output']['content']

def get_Ollama_response(input_text):
    response=requests.post("http://locallhost:8000/poem/invoke",
                           json={'input':{'topic':input_text}})
    return response.json()['output']


###streamlit framework

st.title('Langchain Demo with LLAMA2 API')
input_text=st.text_input("Write an essay on")
input_text1=st.text_input("Write a poem on")

if input_text:
    st.write(get_Openai_response(input_text))             

if input_text1:
    st.write(get_Ollama_response(input_text))
             