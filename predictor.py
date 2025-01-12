import sys
import json
import pickle
import numpy as np

# Load the pre-trained model
MODEL_FILE = 'C:\\Users\\DELL\\om\\ml_model\\bangalore_home_prices_model.pickle'

try:
    with open(MODEL_FILE, 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    print(json.dumps({"error": f"Model file {MODEL_FILE} not found"}))
    sys.exit(1)

# Parse input arguments from the command line
if __name__ == '__main__':
    try:
        input_data = json.loads(sys.argv[1])  # Read JSON from backend
    except (IndexError, json.JSONDecodeError):
        print(json.dumps({"error": "Invalid input format"}))
        sys.exit(1)

    # Extract input features
    area_type = input_data.get('area_type', '')
    location = input_data.get('location', '')
    availability = input_data.get('availability', '')
    total_sqft = input_data.get('total_sqft', 0)
    bath = input_data.get('bath', 0)
    balcony = input_data.get('balcony', 0)
    BHK = input_data.get('BHK', 0)

    # Validate and process inputs
    try:
        total_sqft = float(total_sqft)
        bath = int(bath)
        balcony = int(balcony)
        BHK = int(BHK)
    except ValueError:
        print(json.dumps({"error": "Numeric fields must be valid numbers"}))
        sys.exit(1)

    # Example encoding logic (adjust according to your model)
    # This assumes your model expects encoded inputs like one-hot encoded area_type/location
    encoded_area_type = 1  # Replace with actual encoding logic
    encoded_location = 2  # Replace with actual encoding logic

    # Create the feature array
    try:
        input_features = np.array([[encoded_area_type, encoded_location, total_sqft, bath, balcony, BHK]])

        # Make the prediction
        predicted_price = model.predict(input_features)[0]

        # Return the prediction as JSON
        print(json.dumps({"predicted_price": predicted_price}))

    except Exception as e:
        print(json.dumps({"error": f"Prediction failed: {str(e)}"}))
        sys.exit(1)
