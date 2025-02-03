import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import time
import os
import pickle

st.set_page_config(page_title="Predict Price", page_icon='💸')

# Helper functions
@st.cache_data
def load_data():
    data = pd.read_csv('C:\\Users\\elect\\Desktop\\ds_cars_proj\\Transformed_data\\Cleaned_data.csv')
    return data

def load_model_and_predict(brand, new_data):
    model_filename = os.path.join(MODEL_DIR, f"model_{brand}.pkl")

    # Check if the model exists
    if not os.path.exists(model_filename):
        print(f"Model for {brand} not found.")
        return None

    # Load the model
    with open(model_filename, "rb") as file:
        model = pickle.load(file)

    # Check if the columns of new_data match the training data
    expected_features = model.named_steps['preprocessor'].transformers_[0][2] + model.named_steps['preprocessor'].transformers_[1][2]
    missing_features = [col for col in expected_features if col not in new_data.columns]
    
    if missing_features:
        print(f"Missing columns: {missing_features}")
        return None

    # Predict the price
    prediction = model.predict(new_data)
    return prediction

# Loading data
data = load_data()

# Define the path to the directory containing the saved models
MODEL_DIR = "C:\\Users\\elect\\Desktop\\ds_cars_proj\\model\\brands"

# Code of the ML page
def show_predict_page():
    st.write("## 💸 Your Car's Price Prediction in (USD) 💲")
    st.markdown("<h2 style='text-align: center; color: #4CAF50;'>Please provide the following details to estimate your car's price:</h2>", 
    unsafe_allow_html=True)
    st.markdown("<hr style='border:1px solid #4CAF50;'>", unsafe_allow_html=True)

    # Selecting all brands that haven't NaN values 
    brands_cat1 = ('BMW', 'Volvo', 'Lexus', 'Lincoln', 'INFINITI', 'Land Rover', 'Volkswagen', 'Hyundai', 'Subaru', 'Mazda', 'Honda', 'MINI', 'Bentley', 'Chrysler', 'Lotus', 'Maserati', 'Aston Martin', 'Rolls-Royce')
    condition = ('Used', 'New', 'Certified (given by the vehicle manufacturer itself or from third-party organizations)')

    st.markdown("""
    <style>
    div[data-baseweb="select"] > div {
        font-size: 18px !important;
    }

    label {
        font-size: 20px !important;
        font-weight: bold;
        color: #2c3e50;
    }

    input[type="number"] {
        font-size: 18px !important;
    }

    .stSelectbox, .stNumberInput {
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)
    
    brand_user = st.selectbox("🚗 **The brand of your car is:**", brands_cat1)
    condition_user = st.selectbox("📌 **The condition of your car is:**", condition)
    mileage_user = st.number_input("📏 **The mileage of your car (in miles):** *(Type 0 if it's new)*")
    year_user_car = st.number_input("📅 **The production year of your car (e.g., 2010):**")

    new_data = pd.DataFrame([{
        "brand": brand_user,
        "Condition_car": condition_user,
        "Mileage_mi": mileage_user,
        "Year": year_user_car
    }])

    if st.button("Let's go"):
        try:
            placeholder = st.empty()
            placeholder.progress(0, "Wait for it...")
            time.sleep(1)

            prediction = load_model_and_predict(brand_user, new_data)

            placeholder.progress(50, "Wait for it...")
            time.sleep(1)
            placeholder.progress(100, "Wait for it...")
            time.sleep(1)

            if prediction is not None:
                st.markdown(f"<h3 style='text-align: center; color: #B5A642;'>Predicted Price: ${prediction[0]:,.2f}</h3>", unsafe_allow_html=True)
        finally:
            placeholder.empty()
            

show_predict_page()


with st.sidebar:
    st.title('🚗 Cars Exploration & Price Prediction | Analyzing Cars.com Listings')
    st.logo("C:\\Users\\elect\\Desktop\\ds_cars_proj\\assets\\cars_com_Logo.jpg",size='large')

# Hide Left Menu
st.markdown("""<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>""", unsafe_allow_html=True)
