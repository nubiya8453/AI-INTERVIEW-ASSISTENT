
import streamlit as st
from groq import Groq
st.set_page_config(page_title='AI-INTERVIEW-ASSISTENT', layout='centered')
st.title('AI-INTERVIEW-ASSISTENT')
st.caption('Practice interview with AI-generated and constructive feedback ''Nubiya Fathima AI&DS.')
try:
    client = Groq(api_key=st.secrets['GROQ_API_KEY'])
    st.success("API connection successful!")
except Exception as e:
    st.error("GROQ_API_KEY is missing or invalid.")
    st.write("Add your API key in Streamlit Cloud → App settings → Secrets.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("AI Interview Assistant")

role = st.selectbox("Select Job Role",[
"Python Developer",
"Java Developer",
"Data Analyst",
"Machine Learning Engineer",
"Software Engineer",
"HR Executive"
])
if st.button("Generate Interview questions"):
    prompt = "Generate 5 interview questions for the role of " + role = "with" + diff + "difficulty"
  prompt = "Generate  5 interview questions for the role of " + role
  response = client.chat.completions.create(
    model = "openai/gpt-oss-120b",
    messages= [
              {"role" : "system", "content" : "You are an expert technical Interviewer"},
        {"role" : "user" ,"content" : prompt}
  ]
  )

  output = response.choices[0].message.content
  st.write(output)    
