const columns = {
    requiredFeatures: ["area_type","location","availability","total_sqft", "bath","balcony", "BHK"], // Features required for prediction
    // Optional: If you handle one-hot encoding of locations in the backend
    locations: ["Whitefield", "Indiranagar", "Koramangala", "Marathahalli"], // Add all unique locations from the dataset
  };
  
  module.exports = columns;
  