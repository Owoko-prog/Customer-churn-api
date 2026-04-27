import streamlit as st
import requests

API_URL = "https://customer-churn-api-gbgn.onrender.com/predict"

st.title("Customer Churn Predictor")

st.write("Fill customer information below:")


# Encoding helper functions
def encode_yes_no(value):
    return 1 if value == "Yes" else 0


def encode_gender(value):
    return 1 if value == "Male" else 0


def encode_contract(value):
    mapping = {
        "Month-to-month": 0,
        "One year": 1,
        "Two year": 2
    }
    return mapping[value]


def encode_internet(value):
    mapping = {
        "DSL": 0,
        "Fiber optic": 1,
        "No": 2
    }
    return mapping[value]


def encode_payment(value):
    mapping = {
        "Electronic check": 0,
        "Mailed check": 1,
        "Bank transfer (automatic)": 2,
        "Credit card (automatic)": 3
    }
    return mapping[value]


# UI inputs
gender = st.selectbox("Gender", ["Female", "Male"])
senior = st.selectbox("Senior Citizen", ["No", "Yes"])
partner = st.selectbox("Partner", ["No", "Yes"])
dependents = st.selectbox("Dependents", ["No", "Yes"])

tenure = st.slider("Tenure (months)", 0, 72, 12)

phone_service = st.selectbox("Phone Service", ["No", "Yes"])
multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes"])

internet_service = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

online_security = st.selectbox("Online Security", ["No", "Yes"])
online_backup = st.selectbox("Online Backup", ["No", "Yes"])
device_protection = st.selectbox("Device Protection", ["No", "Yes"])
tech_support = st.selectbox("Tech Support", ["No", "Yes"])

streaming_tv = st.selectbox("Streaming TV", ["No", "Yes"])
streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes"])

contract = st.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

paperless = st.selectbox("Paperless Billing", ["No", "Yes"])

payment_method = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

monthly_charges = st.number_input("Monthly Charges", value=29.85)
total_charges = st.number_input("Total Charges", value=1889.5)


if st.button("Predict Churn"):

    features = [
        encode_gender(gender),
        encode_yes_no(senior),
        encode_yes_no(partner),
        encode_yes_no(dependents),
        tenure,
        encode_yes_no(phone_service),
        encode_yes_no(multiple_lines),
        encode_internet(internet_service),
        encode_yes_no(online_security),
        encode_yes_no(online_backup),
        encode_yes_no(device_protection),
        encode_yes_no(tech_support),
        encode_yes_no(streaming_tv),
        encode_yes_no(streaming_movies),
        encode_contract(contract),
        encode_yes_no(paperless),
        encode_payment(payment_method),
        monthly_charges,
        total_charges
    ]

    response = requests.post(
        API_URL,
        json={"features": features}
    )

    result = response.json()

    if result["churn_prediction"] == 1:
        st.error("⚠️ Customer likely to churn")
    else:
        st.success("✅ Customer likely to stay")