# Credit Card Fraud Detection

This project detects fraudulent credit card transactions using a machine learning model trained on real transaction data. It includes a Streamlit web application for users to upload data and analyze predictions in real time.

---

## Features

- Detects fraudulent transactions in credit card datasets
- Trained using Random Forest Classifier
- Handles imbalanced data with class weighting
- CSV upload for bulk predictions
- Streamlit-based interface
- Google Colab compatible

---

## Project Structure

```
├── app.py                       # Streamlit web app
├── fraud_model.py              # Model training script
├── fraud_model.pkl             # Trained model (Joblib format)
├── scaler.pkl                  # StandardScaler for preprocessing
├── credit_card_fraud.csv       # Full dataset
└── README.md                   # Project documentation
```

---

## Technologies Used

- Python 3
- Pandas
- Scikit-learn
- Joblib
- Streamlit

---

## How to Run

### Local Environment

1. Clone the repository:
   ```
   git clone https://github.com/your-username/credit-card-fraud-detection.git
   cd credit-card-fraud-detection
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Train the model:
   ```
   python fraud_model.py
   ```

4. Launch the web app:
   ```
   streamlit run app.py
   ```

---

### Google Colab Instructions

1. Upload all required files to Colab
2. Install packages:
   ```python
   !pip install streamlit pyngrok joblib
   ```

3. Start the app:
   ```python
   from pyngrok import ngrok
   get_ipython().system_raw('streamlit run app.py &')
   print(ngrok.connect(8501))
   ```

---

## Input Format

The input CSV should contain all features used during training. Example format:

```csv
V1,V2,V3,...,V28,Amount
-1.359807,-0.072781,2.536346,...,-0.021053,149.62
```

No `Class` column is needed during prediction. The app will return predictions and probabilities.

---

## Output Format

After prediction, the output will include:

- Original features
- `Prediction` (1 = Fraud, 0 = Normal)
- `Fraud_Probability` (model confidence)

Users can download results directly from the interface.

---

## License

This project is intended for educational and academic purposes only.

---

## Author

Submitted as part of a Machine Learning Internship Project.
