import streamlit as st

st.title("Model Information")

st.write("""
Model Used:
Random Forest Classifier

Dataset:
IBM Telco Customer Churn Dataset

Target Variable:
Churn (Yes / No)

Number of Features:
19 customer attributes

Deployment Pipeline:

Dataset
↓
Model Training (Scikit-learn)
↓
FastAPI Backend
↓
Render Deployment
↓
Streamlit Frontend Dashboard
""")

st.success("Model deployed successfully as an end-to-end ML system.")