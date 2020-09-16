import streamlit as st
import pandas as pd
import pickle
import datetime as dt
import random

# Prepare data

park_code = ["ACAD", "GLAC", "GRCA", "GRSM", "GRTE", "OLYM", "ROMO", "YELL", "YOSE", "ZION"]
model_list = []

for park in park_code:
    with open(f"model_data/{park}_sarima.pickle", "rb") as read_file:
        park_sarima = pickle.load(read_file)
    model_list.append(park_sarima)

# Start App
st.title("National Park Visitor Count Predictor")

# Create checkbox for selecting a park and select the model corresponding to the park
park_options = ['Acadia National Park',
                'Glacier National Park',
                'Grand Canyon National Park',
                'Great Smoky Mountains National Park',
                'Grand Teton National Park',
                'Olympic National Park',
                'Rocky Mountain National Park',
                'Yellowstone National Park',
                'Yosemite National Park',
                'Zion National Park']


emoji_list = [":evergreen_tree:",
              ":snow_capped_mountain:",
              ":cactus:",
              ":sunrise_over_mountains:",
              ":footprints:",
              ":seedling:",
              ":national_park:",
              ":camping:",
              ":bear:",
              ":milky_way:",
             ]

park_option = st.selectbox('Which park are you interested in?', park_options)

park_emoji = emoji_list[park_options.index(park_option)]
st.markdown(park_emoji + ' You selected: ' + park_option + " " + park_emoji)

selected_model = model_list[park_options.index(park_option)]

# Create checkbox for selecting a date and select
month_options = ["January", "February", "March", "April", "May", "June", "July", 
                 "August", "September", "October", "November", "December"]
month_option = st.selectbox('Which month are you interested in?', month_options)
year_options = ["2020", "2021", "2022", "2023", "2024", "2025"]
year_option = st.selectbox('Which year are you interested in?', year_options)

# Only run if a park and dates have been selected
if park_option and month_option and year_option:

    # Calculate how many months from February 2016 to make a prediction
    model_date = "February 2016"
    model_date = dt.datetime.strptime(model_date, "%B %Y")
    selected_date = dt.datetime.strptime((month_option + " " + year_option), "%B %Y")
    
    month_difference = (selected_date.year - model_date.year) * 12 + (selected_date.month - model_date.month)

    visitor_pred = int(selected_model.predict(n_periods = month_difference)[-1])

    st.markdown(f"### {park_option} in {month_option} {year_option} is forecast to have **{visitor_pred}** visitors.")
 

