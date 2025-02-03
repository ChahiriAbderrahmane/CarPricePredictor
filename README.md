<div align="center">
  <a href="https://carpricepredictoranalyser-chahiri.streamlit.app/">
    <img src="https://github.com/ChahiriAbderrahmane/CarPricePredictor/blob/main/assets/image_data1.png" alt="Banner" width="720">
  </a>

  <div id="user-content-toc">
    <ul>
      <summary><h1 style="display: inline-block;">🚗 Cars Exploration & Price Prediction | Analyzing Cars.com Listings</h1></summary>
    </ul>
  </div>
  
  <p>In-Depth Analysis of the U.S. Automotive Market</p>
    <a href="https://carpricepredictoranalyser-chahiri.streamlit.app/" target="_blank">Live Preview</a>
    🛸
    <a href="https://www.kaggle.com/datasets/chahiriiscoding/car-sales-data-from-cars-com" target="_blank">Data on Kaggle</a>
    🌪️
    <a href="https://github.com/ChahiriAbderrahmane/CarPricePredictor/issues" target="_blank">Request Feature</a>
</div>
<br>
<div align="center">
      <a href="https://carpricepredictoranalyser-chahiri.streamlit.app/"><img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg"/></a>
      <img src="https://img.shields.io/github/stars/ChahiriAbderrahmane/CarPricePredictor?color=blue&style=social"/>
</div>

## 📝 Table of Contents

1. [ Project Overview ](#introduction)
2. [ Project Architecture ](#arch)
3. [ Web Scrapinng ](#webscraping)
4. [ Data Cleaning, EDA and Model Building](#dataedamodel)
5. [ Installation ](#installation)
6. [ References ](#refs)
7. [ Contact ](#contact)
<hr>

### 🕵️ Data Exploration Page
![image](https://github.com/ChahiriAbderrahmane/CarPricePredictor/blob/main/assets/1.png)


### 💡Insights Page
![image](https://github.com/ChahiriAbderrahmane/CarPricePredictor/blob/main/assets/2.png)

### 💸 Salary Price Page
![image](https://github.com/ChahiriAbderrahmane/CarPricePredictor/blob/main/assets/3.png)

<a name="introduction"></a>
## 🔬 Project Overview :

### 🎯 Goal :
The goal of this data science project is to extract insights from cars.com data to understand trends in car sales. 
          By analyzing various features such as brand, price, mileage, and year, the project aims to identify key factors 
          affecting car prices. Additionally, a machine learning model will be developed to predict car prices based on these factors. 
          
### 🧭 Steps :
The project begins by **scraping** the **cars.com** website, extracting data from **500 pages**. This data includes detailed information 
         about each car: **model, condition, mileage, production year, dealer name, as well as total and monthly prices**. Each page is stored
         locally in **JSON format** within the **"data"** folder. For precautionary purposes, a backup copy is maintained in **"data copy"**. 
         Once collected, the data is **merged, converted to CSV format, cleaned**, and then saved in the **"transformed_data"** folder.

**The EDA** step aimed to extract insights and patterns from the data. This included creating visualizations and analyzing **Average 
         Car Price by Brand and Condition, Evolution of Average Car Price Based on Mileage, Brands with the Most Models, Top 10 Dealers with 
         Highest Sales, Top 10 Dealers with Highest Average Car Prices, and Location of Top 10 Dealers**.
         This step ultimately provided several **insights**, which are presented here in the second tab of the first page.

After **EDA, feature engineering** is performed to create new features that may improve the accuracy of the price prediction model, 
         such as **'brand', 'mileage_mi'**, and others. This includes creating **dummy variables** for categorical features like **brand**.

The **price prediction model** is built using a **RandomForestRegressor**. Finally, the model is deployed in a **web application** 
         using **Streamlit**, enabling users to input their own data and receive a **price prediction** based on the model.
<a name="arch"></a>

## 📝 Project Architecture

![Project Arch](https://github.com/ChahiriAbderrahmane/CarPricePredictor/blob/main/assets/cars_ds_pworkflow.jpg)

### 🛠️ Technologies Used

![Visual Studio Code](https://img.shields.io/badge/Made%20with-VS%20Code-blue?style=for-the-badge&logo=visualstudiocode&logoColor=white) 
![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![AgentQL](https://img.shields.io/badge/AgentQL-%43B02A?style=for-the-badge&logo=selenium&logoColor=white) 
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) 
![Pandas](https://img.shields.io/badge/Pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) 
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white) 
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=matplotlib&logoColor=black) 
![Seaborn](https://img.shields.io/badge/Seaborn-008080?style=for-the-badge&logoColor=white) 
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white) 
![Folium](https://img.shields.io/badge/Folium-77B829?style=for-the-badge&logo=folium&logoColor=white) 
![WordCloud](https://img.shields.io/badge/WordCloud-%23150458.svg?style=for-the-badge&logoColor=white) 
![Playwright](https://img.shields.io/badge/Playwright-45ba65?style=for-the-badge&logo=playwright&logoColor=white) 
![Logging](https://img.shields.io/badge/Logging-4B0082?style=for-the-badge&logoColor=white) 
![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)

<a name="webscraping"></a>

## 🧹 Data Cleaning, EDA and Model Building

Please refer to the respective notebooks ([data cleaning](https://github.com/ChahiriAbderrahmane/CarPricePredictor/blob/main/notebooks/Cleaning.ipynb), [data eda](https://github.com/ChahiriAbderrahmane/CarPricePredictor/blob/main/notebooks/EDA.ipynb), [model buidling](https://github.com/ChahiriAbderrahmane/CarPricePredictor/blob/main/notebooks/Prediction_ML.ipynb)).

<a name="installation"></a>

## 🖥️ Installation : 
1. Clone the repository:

```
git clone https://github.com/ChahiriAbderrahmane/CarPricePredictor.git
```

2. Install the required packages:

```
pip install -r requirements.txt
```
### - Usage : 
1. Change directory to streamlit:

```
cd streamlit
```

2. Run the app:

```
streamlit run streamlit/Cars_Exploration_Aanlysis_app.py
```

<a name="refs"></a>

