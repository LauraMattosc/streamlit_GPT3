import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Define the API endpoint and parameters
api_key = "1036d77762adc57b8c2dddcb299ad2f9"
endpoint = "http://api.openweathermap.org/data/2.5/weather"
params = {"q": "Sao Paulo,BR", "appid": api_key, "units": "metric"}

st.title("Sao Paulo Weather")

# Fetch the current weather data from the API
response = requests.get(endpoint, params=params)
data = response.json()

# Extract the current temperature from the data
temp = data["main"]["temp"]
st.write(f"The current temperature in Sao Paulo is {temp}°C")

# Create a checkbox to show/hide the graph
show_graph = st.checkbox("Show temperature over time")

if show_graph:
    # Fetch the historical weather data from the API
    endpoint = "http://api.openweathermap.org/data/2.5/forecast"
    response = requests.get(endpoint, params=params)
    data = response.json()

    # Extract the temperature data from the response
    temp_data = [item["main"]["temp"] for item in data["list"]]

    # Create a line plot of the temperature over time
    plt.plot(temp_data)
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    st.pyplot()
