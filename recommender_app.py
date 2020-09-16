import streamlit as st
import pandas as pd
import numpy as np
import random
import pickle
from PIL import Image

# Prepare data
with open("data/park_activity_topic_df.pickle", "rb") as read_file:
    park_activity_topic_df = pickle.load(read_file)
    
with open("recommender_data/park_cosine_similarity.pickle", "rb") as read_file:
    park_cosine_similarity = pickle.load(read_file)
        

# Start App
st.title("National Park Recommender")

# Create checkbox for selecting a park

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

park_option = st.selectbox('Which park are you interested in?', park_options)

park_code = ["ACAD", "GLAC", "GRCA", "GRSM", "GRTE", "OLYM", "ROMO", "YELL", "YOSE", "ZION"]

# prepare images

image_list = []

for park in park_code:
    image = Image.open(f'recommender_images/{park}.jpg')
    image_list.append(image)
    
recommendations = st.slider('How many recommendations are you interested in?', min_value=1, max_value=10, value=1, step=1)

st.image(image_list[park_options.index(park_option)], caption=f'{park_option}', use_column_width=True)

# Only run if a park and number of recommendations has been selected
if park_option and recommendations:
    recommend_parks = []
    activities_overlap = []
    
    # Map the selected park to its park code
    selected_code = park_code[park_options.index(park_option)].lower()
    park_index = park_activity_topic_df[park_activity_topic_df["park_code"] == selected_code].index.values.astype(int)[0]
    
    # Find the closest parks by topic/activity cosine distance
    closest_park_index = np.argsort(park_cosine_similarity[park_index])[-(recommendations+1):-1][::-1]
    closest_parks = park_activity_topic_df.iloc[closest_park_index]["full_name"].values.tolist()
    
    # Get topics for the selected park
    
    original_park_topics_df = park_activity_topic_df.iloc[[park_index]].copy()
    original_park_topics = original_park_topics_df.columns[(original_park_topics_df == 1.0).any(axis=0)].tolist()
    
    # Find the number of activity/topic overlaps and print 5 of them out
    
    i = 0
    
    for park in closest_park_index:
        similar_park_topics_df = park_activity_topic_df.iloc[[park]].copy()
        similar_park_topics = similar_park_topics_df.columns[(similar_park_topics_df == 1.0).any(axis=0)].tolist()
        
        overlap = list(set(original_park_topics).intersection(set(similar_park_topics)))
        
        common_things = random.sample(overlap, k=5)
        
        st.markdown(f"{i+1}. {closest_parks[i]} is the number {i+1} recommendation.")
        st.markdown(f"Common activities/topics include {common_things[0]}, {common_things[1]}, \
                 {common_things[2]}, {common_things[3]}, and {common_things[4]}.")
        st.write("")
    
        i += 1
    
    
    
    
    