import streamlit as st
import pickle
import pandas as pd


# Load model and columns
model = pickle.load(open("model.pkl", "rb"))
scaler=pickle.load(open("scaler.pkl","rb"))
columns = pickle.load(open("columns.pkl", "rb"))

st.title("Customer Churn Prediction")

st.write(type(model))
st.write("Number of columns:", len(columns))

# Basic
gender = st.selectbox("Gender", ["Female", "Male"])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["No", "Yes"])
dependents = st.selectbox("Dependents", ["No", "Yes"])

# Services
phone = st.selectbox("Phone Service", ["No", "Yes"])

multiple = st.selectbox(
    "Multiple Lines",
    ["No", "No phone service", "Yes"]
)

internet = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

online_security = st.selectbox(
    "Online Security",
    ["No", "Yes", "No internet service"]
)

online_backup = st.selectbox(
    "Online Backup",
    ["No", "Yes", "No internet service"]
)

device = st.selectbox(
    "Device Protection",
    ["No", "Yes", "No internet service"]
)

tech = st.selectbox(
    "Tech Support",
    ["No", "Yes", "No internet service"]
)

tv = st.selectbox(
    "Streaming TV",
    ["No", "Yes", "No internet service"]
)

movies = st.selectbox(
    "Streaming Movies",
    ["No", "Yes", "No internet service"]
)

contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

paperless = st.selectbox(
    "Paperless Billing",
    ["No", "Yes"]
)

payment = st.selectbox(
    "Payment Method",
    [
        "Bank transfer (automatic)",
        "Credit card (automatic)",
        "Electronic check",
        "Mailed check"
    ]
)

# Numeric
tenure = st.slider("Tenure", 0, 72, 12)

monthly = st.number_input(
    "Monthly Charges",
    value=70.0
)

total = st.number_input(
    "Total Charges",
    value=1000.0
)

if st.button("Predict"):

    input_data = pd.DataFrame(
        [[0]*len(columns)],
        columns=columns
    )

    # Numeric columns
    input_data["SeniorCitizen"] = senior
    input_data["tenure"] = tenure
    input_data["MonthlyCharges"] = monthly
    input_data["TotalCharges"] = total

    # Binary
    if gender == "Male":
        input_data["gender_Male"] = 1

    if partner == "Yes":
        input_data["Partner_Yes"] = 1

    if dependents == "Yes":
        input_data["Dependents_Yes"] = 1

    if phone == "Yes":
        input_data["PhoneService_Yes"] = 1

    # Multiple lines
    if multiple == "No phone service":
        input_data["MultipleLines_No phone service"] = 1

    elif multiple == "Yes":
        input_data["MultipleLines_Yes"] = 1

    # Internet
    if internet == "Fiber optic":
        input_data["InternetService_Fiber optic"] = 1

    elif internet == "No":
        input_data["InternetService_No"] = 1

    # Online Security
    if online_security == "No internet service":
        input_data["OnlineSecurity_No internet service"] = 1

    elif online_security == "Yes":
        input_data["OnlineSecurity_Yes"] = 1

    # Online Backup
    if online_backup == "No internet service":
        input_data["OnlineBackup_No internet service"] = 1

    elif online_backup == "Yes":
        input_data["OnlineBackup_Yes"] = 1

    # Device Protection
    if device == "No internet service":
        input_data["DeviceProtection_No internet service"] = 1

    elif device == "Yes":
        input_data["DeviceProtection_Yes"] = 1

    # Tech Support
    if tech == "No internet service":
        input_data["TechSupport_No internet service"] = 1

    elif tech == "Yes":
        input_data["TechSupport_Yes"] = 1

    # Streaming TV
    if tv == "No internet service":
        input_data["StreamingTV_No internet service"] = 1

    elif tv == "Yes":
        input_data["StreamingTV_Yes"] = 1

    # Streaming Movies
    if movies == "No internet service":
        input_data["StreamingMovies_No internet service"] = 1

    elif movies == "Yes":
        input_data["StreamingMovies_Yes"] = 1

    # Contract
    if contract == "One year":
        input_data["Contract_One year"] = 1

    elif contract == "Two year":
        input_data["Contract_Two year"] = 1

    # Paperless
    if paperless == "Yes":
        input_data["PaperlessBilling_Yes"] = 1

    # Payment
    if payment == "Credit card (automatic)":
        input_data["PaymentMethod_Credit card (automatic)"] = 1

    elif payment == "Electronic check":
        input_data["PaymentMethod_Electronic check"] = 1

    elif payment == "Mailed check":
        input_data["PaymentMethod_Mailed check"] = 1

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    if prediction[0]:
        st.error("⚠ Customer Will Churn")

    else:
        st.success("✅ Customer Will Stay")

    st.write(
        "Churn Probability:",
        round(probability[0][1]*100,2),
        "%"
    )




