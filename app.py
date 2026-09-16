import streamlit as st
import joblib


# Load model and vectorizer
model = joblib.load("models/spam_model.pkl")
tfidf = joblib.load("models/tfidf_vectorizer.pkl")


# Page configuration
st.set_page_config(
    page_title="Spam Email Detector",
    page_icon="📧",
    layout="centered"
)


# Title
st.title("📧 Spam Email Detector")

st.write(
    "Enter a message below and the machine learning model "
    "will predict whether it is spam or not."
)


# User input
message = st.text_area(
    "Enter your message:",
    placeholder="Example: Congratulations! You have won a free prize..."
)


# Prediction
if st.button("Check Message"):

    if message.strip() == "":
        st.warning("Please enter a message.")

    else:
        message_tfidf = tfidf.transform([message])

        prediction = model.predict(message_tfidf)[0]

        if prediction == 1:
            st.error("🚨 This message is SPAM!")

        else:
            st.success("✅ This message is NOT SPAM!")