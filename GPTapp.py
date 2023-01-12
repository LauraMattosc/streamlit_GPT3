import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="My Streamlit App", page_icon=":guardsman:", layout="wide")

# Create some fields for user input
name = st.text_input("Enter your name")
age = st.number_input("Enter your age")

# Create a checkbox to show/hide the graph
show_graph = st.checkbox("Show graph")

if show_graph:
    # Create a sample dataset
    df = pd.DataFrame({
        "x": [1, 2, 3, 4],
        "y": [10, 15, 13, 17]
    })

    # Create a line plot
    plt.plot(df["x"], df["y"])
    st.pyplot()

# Display user input
st.write("Your name is", name)
st.write("Your age is", age)
