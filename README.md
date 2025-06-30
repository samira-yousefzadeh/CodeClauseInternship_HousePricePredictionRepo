# CodeClauseInternship_HousePricePredictionRepo
House Price Prediction with Flask and Linear Regression

## Project Overview

This project predicts house prices based on various features such as average income, number of rooms, bedrooms, house age, and population using **Linear Regression**.  
It is part of my CodeClause Internship, focusing on both core data science techniques and full-stack data delivery using Flask.

---

## Contents

- `Enhanced_PredictingHousePrices.ipynb`: A fully documented Jupyter notebook showing:
  - Data loading and exploration
  - Feature selection and visualization
  - Linear regression model training and evaluation
- `app.py`: A lightweight Flask server enabling interactive house price predictions
- `templates/index.html`: The UI where users input house features
- `model/house_price_model.pkl`: Pretrained regression model

---

## Flask App Features

The Flask-based web interface lets users:
- Enter house-related inputs
- Instantly see the predicted price
- View basic model evaluation: **MSE**, **RMSE**, and **R² score**

---

## How to Run Locally

1. Clone the repo:
```bash
git clone https://github.com/your-username/house-price-predictor
cd house-price-predictor

pip install flask scikit-learn numpy pandas joblib

Run the App (VScode Terminal):
python app.py
Visit:
http://127.0.0.1:5000

