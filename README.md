# 🚗 Used Car Price Prediction App

This project is a **Streamlit-powered web app** that predicts the price of a used car based on key features like model year, mileage, brand, accident history, and more. The app uses a **trained Random Forest Regressor model** to provide instant predictions and serves as a practical example of deploying machine learning models for real-world applications.

---

## 🧠 Project Overview

- Predicts the selling price of a used car based on various numerical and categorical inputs.
- Built using a Random Forest regression model trained on preprocessed car data.
- Offers a simple, intuitive web interface for real-time predictions.
- Demonstrates the end-to-end workflow: data preprocessing → model training → deployment using Streamlit.

---

## ⚙️ Tech Stack

- **Python**
- **pandas**, **NumPy**, **scikit-learn**
- **Streamlit** for web app UI
- **Pickle** for model serialization
- **VS Code** & **GitHub** for development & version control

---

## 💻 How to Run Locally

1. **Clone the repository**
  
   git clone https://github.com/sharmitaranii/Used-Car-Price-Prediction.git
   cd Used-Car-Price-Prediction/app
Install dependencies

pip install -r requirements.txt
Run the Streamlit app

streamlit run app.py
Enter values in the web form to get an estimated used car price.

⚠️ Note: This is a prototype and will run only with a preprocessed test CSV or manual inputs based on the trained model's schema.

🧪 Example Prediction
Inputs:

Model Year: 2015

Mileage: 45,000

Accident: No

Car Age: 8

Brand: BMW

Predicted Price: ₹7.8 Lakhs (example output)

🔗 Deployment
You can try the live app here:
👉 Used Car Price Prediction App – https://used-car-price-prediction-hhh.streamlit.app/

📂 File Structure

├── app/
│   ├── app.py                 # Streamlit app
│   ├── model_columns.pkl      # Feature columns used during training
│   ├── rf_model_log.pkl       # Trained Random Forest model
│   └── requirements.txt       # Python dependencies
├── .gitignore
└── README.md


📌 Future Enhancements
Add brand/model dropdowns for better UX

Feature importance visualization

Confidence intervals for prediction
