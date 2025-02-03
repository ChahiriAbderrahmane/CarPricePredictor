import pandas as pd
import numpy as np
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import KNNImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# List of brands to process
brands_cat = ['BMW', 'Volvo', 'Lexus', 'Lincoln', 'INFINITI', 'Land Rover', 'Volkswagen', 'Hyundai', 'Subaru', 'Mazda', 'Honda', 'MINI', 'Bentley', 'Chrysler', 'Lotus', 'Maserati', 'Aston Martin', 'Rolls-Royce']

def train_and_save_model(df, model_dir):

    if not os.path.exists(model_dir):
        os.makedirs(model_dir)   # Create the directory if it does not exist

    for brand in brands_cat:
        brand_dataframe = df[df['brand'] == brand]

        # Separation of features (X) and price (Y)
        X = brand_dataframe.drop(columns=['Price (USD)', 'Car Model', 'Condition', 'Mileage', 'Dealer Name', 'brand', 'Monthly Payment'])
        Y = brand_dataframe['Price (USD)']

        # Identification of numerical and categorical variables
        num_features = X.select_dtypes(include=['number']).columns.tolist()
        cat_features = X.select_dtypes(include=['object']).columns.tolist()

        # Preprocessing pipelines
        num_transformer = Pipeline([
            ('imputer', KNNImputer(n_neighbors=5)), 
            ('scaler', StandardScaler())
        ])
        cat_transformer = Pipeline([
            ('encoder', OneHotEncoder(handle_unknown='ignore'))
        ])
        preprocessor = ColumnTransformer([
            ('num', num_transformer, num_features),
            ('cat', cat_transformer, cat_features)
        ])

        # Model
        model = Pipeline([
            ('preprocessor', preprocessor),
            ('regressor', RandomForestRegressor(n_estimators=300, max_depth=11, random_state=42))
        ])

        # Training
        model.fit(X, Y)

        # Save the brand-specific model
        model_filename = os.path.join(model_dir, f"model_{brand}.pkl")
        with open(model_filename, "wb") as file:
            pickle.dump(model, file)
        
        print(f"Model saved for {brand}: {model_filename}")


def load_model_and_predict(model_dir, brand, new_data):
    # Load the brand model and make a prediction on the new data
    model_filename = os.path.join(model_dir, f"model_{brand}.pkl")

    # Check if the model exists
    if not os.path.exists(model_filename):
        print(f"Model for {brand} not found.")
        return None

    # Load the model
    with open(model_filename, "rb") as file:
        model = pickle.load(file)

    # Predict
    return model.predict(new_data)


if __name__ == "__main__":
    # Load the dataset
    df_path = "C:\\Users\\elect\\Desktop\\ds_cars_proj\\Transformed_data\\Cleaned_data.csv"
    model_dir = "C:\\Users\\elect\\Desktop\\ds_cars_proj\\model\\brands"

    if not os.path.exists(df_path):
        print("Data file not found.")
    else:
        df = pd.read_csv(df_path)
        train_and_save_model(df, model_dir)

