import streamlit as st
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import json
from relevance import get_relevance
from huggingface import hugging_face

def extract_name_from_url(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    if domain.startswith('www.'):
        domain = domain[4:]  
    name = domain.split('.')[0]
    return name

def extract_website_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    return soup.get_text()


st.title("StartupScout")

url = st.text_input("Enter the startup website URL:")

if st.button("Extract Information"):
    if url:
        with st.spinner('Extracting information...'):
            try:
                
                try:
                    name=extract_name_from_url(url)
                    relevance_content=get_relevance(url)
                except Exception as e:
                    website_content="No info"
                    crunchbase_content="No info"
                    relevance_content="No info"

                st.success("Information extracted successfully!")
                st.subheader("Startup Information")
                st.write(f"**Name:** {name}")       
                st.write(f"**Details:** {relevance_content}")
                
            
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter a valid URL.")