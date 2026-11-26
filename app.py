
import streamlit as st
from groq import Groq

# Page configuration
st.set_page_config(
    page_title="AI-INTERVIEW-ASSISTANT",
    layout="centered"
)

# Application title
st.title("AI-INTERVIEW-ASSISTANT")
st.caption(
    "Practice interviews with AI-generated questions "
    "and constructive feedback - Nubiya Fathima AI&DS."
)

# Groq API connection
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    st.success("API connection successful!")

except Exception:
    st.error("GROQ_API_KEY is missing or invalid.")
    st.write("Add your API key in Streamlit Cloud → App settings → Secrets.")
    st.stop()

# Job role selection
role = st.selectbox(
    "Select Job Role",
    [
        "Python Developer",
        "Java Developer",
        "Data Analyst",
        "Machine Learning Engineer",
        "Software Engineer",
        "HR Executive"
    ]
)

# Difficulty selection
diff = st.selectbox(
    "Select Difficulty",
    ["Easy", "Medium", "Hard"]
)

# Generate interview questions
if st.button("Generate Interview Questions"):

    prompt = (
        "Generate 5 interview questions for the role of "
        + role
        + " with "
        + diff
        + " difficulty."
    )

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert technical interviewer."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        output = response.choices[0].message.content

        st.subheader("Generated Interview Questions")
        st.write(output)

    except Exception as e:
        st.error(f"Error generating questions: {e}")
