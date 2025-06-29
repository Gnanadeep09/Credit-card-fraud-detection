
# Credit Card Fraud Detection

A machine learning project to detect fraudulent credit card transactions using a Random Forest classifier. This project includes data preprocessing, model training, evaluation, and a user-friendly web app built with Streamlit.

---

##  Project Features

- Detects fraud in credit card transactions
- Uses a realistic synthetic dataset (under 25MB)
- Streamlit web app for easy use
- Google Colab compatible
- Downloadable prediction results

---
## File Structure

├── app.py                        # Streamlit web app
├── fraud_model.py               # Model training script
├── credit_card_fraud.csv        # Full dataset
├── credit_card_fraud_small.csv  # Smaller sample dataset (10k rows)
├── fraud_model.pkl              # Trained model file
├── scaler.pkl                   # Preprocessing scaler file
├── sample_input.csv             # Sample input file for testing
└── README.md                    # Project documentation

---
- Python 3
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Pyngrok (for Colab use)

---

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/credit-card-fraud-detection.git
   cd credit-card-fraud-detection
   
	2.	Install required packages:
pip install -r requirements.txt

	3.	Train the model:
python fraud_model.py

	4.	Launch the web app:
streamlit run app.py
__

☁️ Run on Google Colab
1.	Upload the dataset (credit_card_fraud.csv) and scripts.
 2.	Install necessary packages:
!pip install streamlit pyngrok joblib

3.	Authenticate ngrok:
!ngrok config add-authtoken YOUR_NGROK_TOKEN

4.	Start the app:
get_ipython().system_raw('streamlit run app.py &')
from pyngrok import ngrok
print(ngrok.connect(8501))

⸻
📊 Sample Data
You can use the provided credit_card_fraud.csv (10,000 rows) as input for quick testing or upload a custom CSV with similar structure.
⸻
🧾 Output Columns
After prediction:
	•	Prediction: 1 = Fraud, 0 = Normal
	•	Fraud_Probability: Confidence score from the model
⸻

📃 License
This project is free to use for academic and educational purpose

✍️ Author
 by Konka Gnanadeep as part of a Machine Learning Internship Project.
