import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from streamlit_folium import folium_static
import joblib

# Set page config
st.set_page_config(page_title="Cars Exploration & Price Prediction | Analyzing Cars.com Listings", page_icon='🚗',layout="wide")

# Helper functions
@st.cache_data 
def load_data():
    data = pd.read_csv('Transformed_data/Cleaned_data.csv')
    return data

def avg_price_brand_condition(data):
    # Calculate the average price by brand and condition
    avg_price = data.groupby(['brand', 'Condition_car'])['Price (USD)'].mean().reset_index()

    # Sort brands by overall average price (useful for ordered presentation)
    brand_order = avg_price.groupby('brand')['Price (USD)'].mean().sort_values(ascending=False).index
    avg_price['brand'] = pd.Categorical(avg_price['brand'], categories=brand_order, ordered=True)

    # Define the style and colors for a polished presentation
    sns.set_style("whitegrid")
    plt.figure(figsize=(16, 7))
    palette = {"New": "#2ecc71", "Used": "#e74c3c", "Certified": "#3498db"}

    # Create the bar plot with a colorful palette
    sns.barplot(data=avg_price, x='brand', y='Price (USD)', hue='Condition_car', palette=palette)

    # Customize labels and title
    plt.xticks(rotation=45, ha="right", fontsize=12)
    plt.xlabel("Brand", fontsize=14)
    plt.ylabel("Average Price (USD)", fontsize=14)

    # Add a more readable legend
    plt.legend(title="Vehicle Condition", title_fontsize=12, fontsize=11, loc="upper right", frameon=True, edgecolor="black")

    # Display the plot
    st.pyplot(plt)

def evolution_avg_price_mileage(data):
    palette = {"New": "#2ecc71", "Used": "#e74c3c", "Certified": "#3498db"}
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x='Mileage_mi', y='Price (USD)', hue='Condition_car', palette=palette)
    plt.xlabel('Mileage (mi)', fontsize=12)
    plt.ylabel('Price (USD)', fontsize=12)
    plt.legend(title='Condition', title_fontsize='13', fontsize='11')
    st.pyplot(plt)

def Top_10_dealers(data):
    labels = data["Dealer Name"].value_counts().head(10).index
    sizes = data["Dealer Name"].value_counts().head(10)
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99',"pink","yellow"]
    plt.figure(figsize = (8,8))
    plt.pie(sizes, labels=labels, rotatelabels=False, autopct='%1.1f%%',colors=colors,shadow=True, startangle=45)
    st.pyplot(plt)

def map_dealers(data):
    # List of dealer names and their precise coordinates
    dealers = [
    ("Golf Mill Ford", 42.051183300000005, -87.83387903096333),
    ("Mercedes-Benz of Hoffman Estates", 42.048919049999995, -88.1049154048065),
    ("The Audi Exchange", 42.139192, -87.822823),
    ("Ed Napleton Acura Kia", 41.801193, -87.877048),
    ("Phillips Chevrolet", 41.5729774, -87.55983614182739),
    ("Joe Rizza Ford Lincoln", 41.558153, -87.800293),
    ("Glendale Nissan", 34.13706500000001, -118.25537322456444),
    ("Woodataield Nissan", 42.0503035, -88.09784249305503),
    ("Webb Ford", 37.36776860997453, -86.07402365718755),
    ("Packey Webb Ford", 41.8498, -88.0888)
    ]

    # Create a map centered on the USA
    m = folium.Map(location=[41.85, -87.65], zoom_start=8)

    # Add markers to the map
    for dealer, lat, lon in dealers:
        folium.Marker(
            location=[lat, lon],
            popup=f"<b>{dealer}</b>",
            tooltip=dealer,
            icon=folium.Icon(color="blue", icon="car", prefix="fa")  # Car icon
        ).add_to(m)

    # Save as an interactive HTML file
    m.save("dealers_map.html")

    # Display 
    folium_static(m)

def number_models_by_brand(data):
    # Group by brand and count the number of models for each brand
    brand_model_counts = data['brand'].value_counts()

    # Plot the brands with the most models
    plt.figure(figsize=(12, 8))
    brand_model_counts.plot(kind='bar')
    plt.xlabel('Brand', fontsize=14)
    plt.ylabel('Number of Models', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    st.pyplot(plt)

def avg_price_10dealer(data):
    # Calculate the average price per dealer
    avg_price = data.groupby('Dealer Name')['Price (USD)'].mean().reset_index()

    # Sort and select the top 10
    top_10_dealers = avg_price.sort_values(by='Price (USD)', ascending=False).head(10)

    # Define the style and colors for a polished presentation
    sns.set_style("whitegrid")
    plt.figure(figsize=(14, 6))

    # Create the bar plot
    sns.barplot(data=top_10_dealers, x='Dealer Name', y='Price (USD)', palette="Blues_r")

    # Rotate labels for readability
    plt.xticks(rotation=45, ha="right", fontsize=12)

    # Customize titles and axes
    plt.xlabel("Dealer Name", fontsize=14)
    plt.ylabel("Average Price (USD)", fontsize=14)

    # Add annotations on the bars
    for p in plt.gca().patches:
        plt.gca().text(p.get_x() + p.get_width() / 2, 
                   p.get_height() + 1000,  # Adjusted position
                   f'{int(p.get_height()):,}', 
                   ha="center", fontsize=11, fontweight="bold")

    # Display the plot
    st.pyplot(plt)

def total_sales_for_top10dealers(data):
    # Calculate the number of sales per dealer
    dealer_sales_counts = data['Dealer Name'].value_counts().reset_index()
    dealer_sales_counts.columns = ['Dealer Name', 'Sales Count']

    # Calculate the average price per dealer
    avg_price = data.groupby('Dealer Name')['Price (USD)'].mean().reset_index()

    # Merge the two DataFrames to get dealers with their sales and average prices
    dealer_stats = pd.merge(dealer_sales_counts, avg_price, on='Dealer Name')

    # Sort and select the top 10 dealers with the highest sales
    top_10_dealers_by_sales = dealer_stats.sort_values(by='Sales Count', ascending=False).head(10)

    # Define the style and colors for a polished presentation
    sns.set_style("whitegrid")
    plt.figure(figsize=(14, 6))

    # Create the bar plot to display the average price per dealer
    sns.barplot(data=top_10_dealers_by_sales, x='Dealer Name', y='Price (USD)', palette="viridis")

    # Rotate labels for readability
    plt.xticks(rotation=45, ha="right", fontsize=12)

    # Customize titles and axes
    plt.xlabel("Dealer Name", fontsize=14)
    plt.ylabel("Average Price (USD)", fontsize=14)

    # Add annotations on the bars to display average prices
    for p in plt.gca().patches:
        plt.gca().text(p.get_x() + p.get_width() / 2, 
                   p.get_height() + 1000,  # Adjust the position of the annotation
                   f'{int(p.get_height()):,}', 
                   ha="center", fontsize=11, fontweight="bold")

    # Display the plot
    st.pyplot(plt)

def format_with_commas(number):
    return f"{number:,}"

#######


# Display the first two functions, the plot of the first function on the left and the second on the right, both with container(border=True)
data = load_data()



# CSS to disploy the map
st.markdown("""
    <style>
        .custom-container {
            padding: 20px;
            border-radius: 15px;
            border: 1px solid #ddd;
            background-color: #ffffff;
            box-shadow: 3px 3px 15px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .title-text {
            font-size: 24px;
            font-weight: bold;
            color: #2c3e50;
        }
        .section-title {
            font-size: 20px;
            font-weight: bold;
            color: #34495e;
            margin-top: 20px;
        }
        .footer {
            text-align: center;
            padding: 10px;
            background-color: #f8f9fa;
            border-top: 1px solid #ddd;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

# Titre principal
st.markdown("""
    <h1 style="text-align: center; font-size: 2.5em; font-weight: bold; color: #1F618D; background-color: #D3D3D3; padding: 10px; border-radius: 10px;">
        🚗 Cars.com Listings Analysis | Data Exploration
    </h1>
    <hr style="border: 1px solid #ddd;">
""", unsafe_allow_html=True)


#tabs
tab1, tab2 = st.tabs(["Analysis 🔍", "Insights 💡"])

with tab1 :
    # display columns 
    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container():
            st.markdown('<div class="custom-container">', unsafe_allow_html=True)
            st.markdown('<p class="title-text">🚗 Average Car Price by Brand and Condition</p>', unsafe_allow_html=True)
            avg_price_brand_condition(data)
            st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        with st.container():
            st.markdown('<div class="custom-container">', unsafe_allow_html=True)
            st.markdown('<p class="title-text">📈 Evolution of Average Car Price Based on Mileage</p>', unsafe_allow_html=True)
            evolution_avg_price_mileage(data)
            st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        with st.container():
            st.markdown('<div class="custom-container">', unsafe_allow_html=True)
            st.markdown('<p class="title-text">🏎️ Brands with the Most Models</p>', unsafe_allow_html=True)
            number_models_by_brand(data)
            st.markdown('</div>', unsafe_allow_html=True)

    col4, col5, col6 = st.columns(3)

    with col4:
        with st.container():
            st.markdown('<div class="custom-container">', unsafe_allow_html=True)
            st.markdown('<p class="title-text">💰 Top 10 Dealers with Highest Sales</p>', unsafe_allow_html=True)
            total_sales_for_top10dealers(data)
            st.markdown('</div>', unsafe_allow_html=True)

    with col5:
        with st.container():
            st.markdown('<div class="custom-container">', unsafe_allow_html=True)
            st.markdown('<p class="title-text">💲 Top 10 Dealers with Highest Average Car Prices</p>', unsafe_allow_html=True)
            avg_price_10dealer(data)
            st.markdown('</div>', unsafe_allow_html=True)

    with col6:
        with st.container():
            st.markdown('<div class="custom-container">', unsafe_allow_html=True)
            st.markdown('<p class="title-text">🌍 Location of Top 10 Dealers</p>', unsafe_allow_html=True)
            map_dealers(data)
            st.markdown('</div>', unsafe_allow_html=True) 

with tab2:
    # Ajout de styles CSS pour un affichage centré et plus professionnel
    st.markdown("""
    <style>
        body {
            background-color: #f4f4f9;
            font-family: 'Arial', sans-serif;
        }
        .container {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            padding: 30px;
        }
        .insights-box {
            background-color: #ffffff;
            border: 1px solid #e0e0e0;
            border-radius: 12px;
            padding: 25px 30px;
            margin: 15px 0;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            width: 80%;
            max-width: 700px;
            transition: transform 0.3s ease;
            text-align: left;
        }
        .insights-box:hover {
            transform: scale(1.02);
        }
        .insights-title {
            font-size: 24px;
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 15px;
            text-align: center;
        }
        .insights-text {
            font-size: 15px;
            color: #555;
            line-height: 1.7;
        }
        .insights-text b {
            color: #000;
        }
        ul {
            padding-left: 20px;
        }
        li {
            margin-bottom: 8px;
        }
    </style>
""", unsafe_allow_html=True)

    # Contenu HTML avec un conteneur central
    st.markdown("""
<div class="container">
    <div class="insights-box">
        <div class="insights-title">🚀 Key Insights</div>
        <div class="insights-text">
            <ul>
                <li><b>Data Anomalies:</b>
                    <ul>
                        <li>Significant price variations driven by luxury and economy vehicles.</li>
                        <li>Mileage extremes reflecting vehicle age and usage patterns.</li>
                        <li>Year range includes both vintage and modern vehicles.</li>
                    </ul>
                </li>
                <li><b>Outlier Distribution by Brand:</b>
                    <ul>
                        <li>Top outlier brands suggest diverse market representation.</li>
                        <li>Brands with highest outliers: <b>Chevrolet, Ford, Toyota, Audi, Mercedes-Benz, GMC</b>.</li>
                    </ul>
                </li>
                <li><b>Analysis Implications:</b>
                    <ul>
                        <li>Need for robust statistical techniques to handle extreme values.</li>
                        <li>Importance of segmented analysis by vehicle's brand.</li>
                        <li>Data cleaning and normalization strategies recommended.</li>
                    </ul>
                </li>
            </ul>
        </div>
    </div>

    <div class="insights-box">
        <div class="insights-title">📊 Market Overview</div>
        <div class="insights-text">
            <ul>
                <li><b>Used cars</b> make up 55.8% of listings, while <b>new cars</b> represent 44.2%.</li>
                <li><b>8.9%</b> of used cars are certified, indicating excellent condition.</li>
            </ul>
        </div>
    </div>

    <div class="insights-box">
        <div class="insights-title">💰 Price and Monthly Payment Relationship</div>
        <div class="insights-text">
            <ul>
                <li>The monthly payment is directly proportional to the car's price.</li>
                <li>Relationship: <b>Price = (53.2 × 10⁶ × Monthly Payment) - 8.96 × 10⁶</b></li>
                <li><b>Key Points:</b>
                    <ul>
                        <li><b>Coefficient:</b> 53.2 × 10⁶</li>
                        <li><b>Intercept:</b> -8.96 × 10⁶</li>
                        <li><b>Price in USD.</b></li>
                    </ul>
                </li>
                <li>Higher monthly payments indicate a higher total car price.</li>
            </ul>
        </div>
    </div>

    <div class="insights-box">
        <div class="insights-title">🏆 Dealer Market Influence</div>
        <div class="insights-text">
            <ul>
                <li>Top 4 dealers (<i>Golf Mill Ford, Mercedes-Benz of Hoffman Estates, The Audi Exchange, Ed Napleton Acura</i>) account for over <b>40%</b> of sales among the top 10.</li>
                <li>No overlap between the <b>Top 10 Dealers</b> with the highest sales and those with the highest average prices.</li>
            </ul>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


#### 

with st.sidebar:
    st.title('🚗 Cars Exploration & Price Prediction | Analyzing Cars.com Listings')
    st.logo("assets/cars_com_Logo.jpg",size='large')


#🚗 Cars Exploration & Aanlysis
#🔍🤖💸