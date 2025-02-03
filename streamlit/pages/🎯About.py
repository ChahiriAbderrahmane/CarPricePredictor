import streamlit as st

st.set_page_config(page_title="About", page_icon='📊')

st.header("📊 About The Project")

st.markdown("---")

st.markdown("### 🎯 Goal :")

st.write("""
         The goal of this data science project is to extract insights from cars.com data to understand trends in car sales. 
          By analyzing various features such as brand, price, mileage, and year, the project aims to identify key factors 
          affecting car prices. Additionally, a machine learning model will be developed to predict car prices based on these factors. 
         """)

st.markdown("### 🔬 Project Overview :")

st.write("""The project begins by **scraping** the **cars.com** website, extracting data from **500 pages**. This data includes detailed information 
         about each car: **model, condition, mileage, production year, dealer name, as well as total and monthly prices**. Each page is stored
         locally in **JSON format** within the **"data"** folder. For precautionary purposes, a backup copy is maintained in **"data copy"**. 
         Once collected, the data is **merged, converted to CSV format, cleaned**, and then saved in the **"transformed_data"** folder.""")

st.write("""**The EDA** step aimed to extract insights and patterns from the data. This included creating visualizations and analyzing **Average 
         Car Price by Brand and Condition, Evolution of Average Car Price Based on Mileage, Brands with the Most Models, Top 10 Dealers with 
         Highest Sales, Top 10 Dealers with Highest Average Car Prices, and Location of Top 10 Dealers**.
         This step ultimately provided several **insights**, which are presented here in the second tab of the first page.

         """)

st.write("""After **EDA, feature engineering** is performed to create new features that may improve the accuracy of the price prediction model, 
         such as **'brand', 'mileage_mi'**, and others. This includes creating **dummy variables** for categorical features like **brand**.
         """)

st.write("""The **price prediction model** is built using a **RandomForestRegressor**. Finally, the model is deployed in a **web application** 
         using **Streamlit**, enabling users to input their own data and receive a **price prediction** based on the model.
         """)

st.write("I would like to highlight that the scraped data is from January 20, 2025, and I contributed it on Kaggle.")

st.markdown("---")

st.markdown("### 📝 Project Architecture :")

st.image("assets/cars_ds_pworkflow.jpg")

st.markdown("---")

st.markdown("### 🔗 Links :")

st.markdown("""##### [🚗 Cars.com](https://www.cars.com/) | [📘 Data on Kaggle](https://www.kaggle.com/datasets/chahiriiscoding/car-sales-data-from-cars-com) |  [😼 See full project on GitHub](https://github.com/ChahiriAbderrahmane/CarPricePredictor) 
        |[📨 Contact me via LinkedIn](https://www.linkedin.com/in/abderrahmane-chahiri-151b26237/) """)

with st.sidebar:
    st.title('🚗 Cars Exploration & Price Prediction | Analyzing Cars.com Listings')
    st.logo("assets/cars_com_Logo.jpg",size='large')

# Hide Left Menu
st.markdown("""<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>""", unsafe_allow_html=True)

