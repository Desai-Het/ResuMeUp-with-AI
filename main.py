import streamlit as st
import PyPDF2
import io
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

st.set_page_config(page_title="ResuMeUp", page_icon="📜", layout="centered")
st.title("ResuMeUp with AI")
st.markdown("Upload your resume and get AI-powered feedback for you job position!")

API_KEY = os.getenv("API_KEY")

uploaded_file = st.file_uploader("Upload you resume", type=["pdf", "txt"])
job_role = st.text_input("Enter the role of your job goal (Optional)")

analyze = st.button("Analyze Resume")

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text+=page.extract_text()+"\n"
    return text

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")

if analyze and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)

        if not file_content.strip():
            st.error("File does not have any content...")
            st.stop()
        prompt = f"""PLease analyze this resume of mine and provide me constructive feedback like what should be the changes need to be done for better resume.
        Suggest changes for: {job_role if job_role else 'general job applications'}
        My resume is:{file_content}
        Please provide your analysis in a clear, structured format with specific recommendations."""

        genai.configure(api_key=API_KEY)

        model = genai.GenerativeModel("gemini-1.5-flash")  
        response = model.generate_content(prompt)

        st.markdown("### The Analysis")
        st.markdown(response.text)
    except Exception as e:
        st.error(f"An error occured: {str(e)}")