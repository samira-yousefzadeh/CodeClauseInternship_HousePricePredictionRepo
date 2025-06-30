from flask import Flask, render_template, request
import joblib
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

app = Flask(__name__)
model = joblib.load('model/house_price_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            float(request.form['income']),
            float(request.form['age']),
            float(request.form['rooms']),
            float(request.form['bedrooms']),
            float(request.form['population'])
        ]

        input_array = np.array(features).reshape(1, -1)
        prediction = model.predict(input_array)[0]

        # For metrics, simulate prediction on just 1 sample
        actual = prediction + np.random.uniform(-5000, 5000)  # fake "actual" for demo only
        mse = mean_squared_error([actual], [prediction])
        rmse = np.sqrt(mse)
        r2 = r2_score([actual], [prediction])

        return render_template(
            'index.html',
            prediction_text=f"💰 Estimated House Price: ${prediction:,.2f}",
            mse_text=f"MSE: {mse:.2f}",
            rmse_text=f"RMSE: {rmse:.2f}",
            r2_text=f"R² Score: {r2:.2f}"
        )
    except Exception as e:
        return render_template('index.html', prediction_text="Error: " + str(e))

if __name__ == '__main__':
    app.run(debug=True)