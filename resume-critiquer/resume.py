import streamlit as st
import PyPDF2
import io
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Resume", page_icon="📄", layout="centered")

st.title("Gives suggestions for your Resume using AI")
st.markdown("Upload your resume and get AI-powered feedback tailored to your needs!")

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7, top_p=0.95, top_k=40, max_output_tokens=1000)

upload_file = st.file_uploader("Upload your resume (PDF of TXT)", type=["pdf", "txt"])
job_role = st.text_input("Enter job role")

analyze = st.button("Analyze Resume")

def extract_text_from_pdf(pdf_file): 
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + '\n'
    return text

def extract_text_from_file(upload_file):
    if upload_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(upload_file.read()))   
    return upload_file.read().decode("utf-8")

if analyze and upload_file:

    try:
        file_content = extract_text_from_file(upload_file) 
        
        if not file_content.strip():
            st.error("File does not content...")
            st.stop()

        prompt = f"""Please analyze this resume and provide constructive feedback. 
        Focus on the following aspects:
        1. Content clarity and impact
        2. Skills presentation
        3. Experience descriptions
        4. Specific improvements for {job_role if job_role else 'general job applications'}
        
        Resume content:
        {file_content}
        
        Please provide your analysis in a clear, structured format with specific recommendations."""
        
        # LangChain-style call to Gemini
        messages = [
            SystemMessage(content="You are an expert resume reviewer with years of experience in HR and recruitment."),
            HumanMessage(content=prompt),
        ]
        response = model.invoke(messages)

        st.markdown("### Analysis Results")
        st.markdown(response.content)

    
    except Exception as e:
        st.error(f"An error occured: {str(e)}")   