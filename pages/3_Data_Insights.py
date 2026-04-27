import streamlit as st

st.title("Dataset Insights")

st.write("""
Key churn patterns discovered from the dataset:

• Customers with short tenure churn more often

• Month-to-month contracts show highest churn rates

• Fiber optic users churn more frequently than DSL users

• Customers without Online Security churn more

• Higher monthly charges slightly increase churn likelihood
""")

st.success("These insights guided feature selection during model training.")