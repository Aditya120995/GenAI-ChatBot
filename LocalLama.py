from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama


##All third party integration is done through Langchain Community


import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

#Langsmith Tracking
os.environ["LANGCHAIN_TRACING_V2"]="True" 
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

prompt=ChatPromptTemplate.from_messages(
    [
       ("system", "You Are A Helpful Assistant.Please response to the user queries."), 
       ("user", "Question:{question}")
    ]
    )

##streamlit framework 

st.title('Langchain Demo with OPENAI API')
input_text= st.text_input("Search the topic you want:")

# ollama LLAma2 LLm
llm = Ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))


