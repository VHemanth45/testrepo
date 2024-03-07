from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title="Image Describer")
st.header("Image Describer")

input_text = st.text_input("Input: ", key="input")
submit_button = st.button("Ask the question")

if submit_button and input_text:
    response = get_gemini_response(input_text)
    st.subheader("The Response is")
    st.write(response)
