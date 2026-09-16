# 📧 Spam Email Detection using Machine Learning

A machine learning project that classifies messages as **Spam** or **Not Spam** using Natural Language Processing (NLP).

## 🚀 Project Overview

Spam messages are unwanted messages that may contain advertisements, scams, fraudulent offers, or malicious links.

This project uses **TF-IDF vectorization** and machine learning classification to automatically identify spam messages.

## About --> Website
https://spamemaildetectionml-rovnbzuurvdkmwgken9w6y.streamlit.app/


## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* Matplotlib
* Seaborn
* Joblib
* Streamlit

## 🤖 Machine Learning Approach

The project follows these steps:

1. Load the dataset
2. Clean the data
3. Explore the dataset
4. Split data into training and testing sets
5. Convert text into numerical features using TF-IDF
6. Train multiple machine learning models
7. Compare model performance
8. Select the best model
9. Save the trained model
10. Build a Streamlit application
11. Deploy the application

## 📊 Models Tested

* Logistic Regression
* Multinomial Naive Bayes
* Random Forest

The final model was selected based on its classification performance, with particular attention to precision, recall and F1-score.

## 📁 Project Structure

```text
spam-detection/
│
├── data/
├── notebooks/
├── models/
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 💻 Run Locally

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Move into the project directory:

```bash
cd spam-detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## 🌐 Application

The project can be accessed through the deployed Streamlit application.

**Live Demo:** Add your deployment URL here.

## 📌 Example

Input:

> Congratulations! You have won a free prize. Click now to claim your reward!

Prediction:

> 🚨 SPAM MESSAGE

## 👩‍💻 Author

Bhumika G S
