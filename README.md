# ResuMeUp

ResuMeUp is a Streamlit app that analyzes your resume and provides AI-powered feedback tailored to your job goals using Google's Gemini AI.

---

## Features

- Upload PDF or TXT resumes
- Get constructive feedback on sections, skills, experience, and clarity
- Optional job role input for tailored advice
- Powered by Google Gemini generative AI

---

## Setup Instructions

### 1. Initialize the project environment

uv init .

### 2. Install required dependencies

uv add streamlit google-generativeai PyPDF2 python-dotenv

### 3. Add API key

Add your API key in a .env file in the same folder of the project

### 4. Running the app

uv run streamlit run main.py

## How to use
- Upload your resume file (PDF or TXT)

- Optionally enter your job goal role

- Click Analyze Resume to get AI-generated feedback





