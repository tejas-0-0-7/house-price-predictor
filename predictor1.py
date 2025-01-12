import pandas as pd
import json
import joblib

# Load model and preprocessing pipeline
model = joblib.load('C:\\Users\\DELL\\om\\ml_model\\bangalore_home_prices_model.pickle')
pipeline = joblib.load('preprocessing_pipeline.pkl')  # If you saved preprocessing separately

# Input data
input_data = json.loads(input_json)
input_df = pd.DataFrame([input_data])

# Preprocess input data
processed_input = pipeline.transform(input_df)

# Make prediction
prediction = model.predict(processed_input)
