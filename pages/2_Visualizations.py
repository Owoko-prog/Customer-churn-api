import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Customer Churn Visualizations")

@st.cache_data
def load_data():
    return pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

df = load_data()

st.subheader("Dataset Preview")
st.dataframe(df.head())


# Churn distribution
st.subheader("Churn Distribution")

fig, ax = plt.subplots()

df["Churn"].value_counts().plot.pie(
    autopct="%1.1f%%",
    ax=ax
)

ax.set_ylabel("")

st.pyplot(fig)


# Tenure vs churn
st.subheader("Tenure vs Churn")

fig2, ax2 = plt.subplots()

df.boxplot(column="tenure", by="Churn", ax=ax2)

st.pyplot(fig2)


# Monthly charges vs churn
st.subheader("Monthly Charges vs Churn")

fig3, ax3 = plt.subplots()

df.boxplot(column="MonthlyCharges", by="Churn", ax=ax3)

st.pyplot(fig3)


# Contract type vs churn
st.subheader("Contract Type vs Churn")

contract_churn = pd.crosstab(df["Contract"], df["Churn"])

st.bar_chart(contract_churn)