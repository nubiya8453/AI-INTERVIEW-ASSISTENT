
import streamlit as st
from groq import Groq

st.set_page_config(
    page_title='AI-INTERVIEW-ASSISTENT',
    layout='centered'
)

st.title('AI-INTERVIEW-ASSISTENT')

st.caption(
    'Practice interview with AI-generated and constructive feedback '
    'Nubiya Fathima AI&DS.'
)

try:
    client = Groq(api_key=st.secrets['GROQ_API_KEY'])
    st.success("API connection successful!")

except Exception as e:
    st.error("GROQ_API_KEY is missing or invalid.")
    st.write("Add your API key in Streamlit Cloud → App settings → Secrets.")
    st.stop()
