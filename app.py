import streamlit as st
import pandas as pd
import joblib

model = joblib.load("fraud_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Credit Card Fraud Detection")

file = st.file_uploader("Upload transaction CSV", type="csv")
if file:
    df = pd.read_csv(file)
    if 'Time' in df.columns and 'Amount' in df.columns:
        df[['Time', 'Amount']] = scaler.transform(df[['Time', 'Amount']])
    if 'Class' in df.columns:
        df = df.drop('Class', axis=1)
    preds = model.predict(df)
    probs = model.predict_proba(df)[:,1]
    df['Prediction'] = preds
    df['Fraud_Probability'] = probs.round(3)
    st.dataframe(df[['Prediction','Fraud_Probability']].head())
    st.download_button("Download CSV", df.to_csv(index=False).encode(), "results.csv", "text/csv")
