import streamlit as st
from groq import Groq
st.set_page_config(page_title='AI-INTERVIEW-ASSISTENT',layout='centered')
st.title('AI-INTERVIEW-ASSISTENT')
st.caption('practice interview with AI-generated and constructive feedback Nubiya Fathima AI&DS.')
try:
  client = Groq(api_key=st.secrets['GROQ_API_KEY'])
  st.write("API connection sucessful")
  st.error('GROQ_API_KEY is missing . Add it to Streamlit Cloud -> App setting secrets')
  st.stop()
