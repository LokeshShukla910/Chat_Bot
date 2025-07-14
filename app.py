from dotenv import load_dotenv 
load_dotenv() 
import streamlit as st 
import os 
import google.generativeai as genai 
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

genai.configure(api_key=os.getenv(GOOGLE_API_KEY))

model = genai.GenerativeModel("gemini-2.0-flash") 

def my_output(query):
    response = model.generate_content(query) 
    return response.text 

#### UI Development using streamlit 

st.set_page_config(page_title="RX Chat BOT")
st.header("RX Chat BOT") 
input = st.text_input("Input " , key = "input")  
submit = st.button("Ask your query") 

if submit :
    response = my_output(input) 
    st.subheader("The Response is :")
    st.write(response)
