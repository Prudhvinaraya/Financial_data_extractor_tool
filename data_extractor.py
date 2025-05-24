from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

llm = ChatNVIDIA(
    model="meta/llama-4-maverick-17b-128e-instruct",
    api_key=st.secrets["NVIDIA_API_KEY"],
    temperature=0.2
)

def extract(article_text):
    prompt = '''
    From the below news article, extract revenue and EPS in JSON format with these keys:
    'revenue_actual', 'revenue_expected', 'eps_actual', 'eps_expected'.

    Use units (e.g., million, billion). Return **only valid JSON**.

    Article
    =======
    {article}
    '''

    pt = PromptTemplate.from_template(prompt)
    chain = pt | llm
    response = chain.invoke({'article': article_text})
    parser = JsonOutputParser()

    try:
        return parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Failed to parse valid JSON response.")
