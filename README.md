### Introduction

For the fifth and final project of the [Metis Data Science Bootcamp](https://www.thisismetis.com/), I analyzed U.S. National park visitor counts and their activities/topics in order to build 2 models. These two models are:

1. time series model to predict visitor counts for national parks
2. content based recommender to recommend similar parks based on similarity in activities and topics

### Individual Contributor

* [Jacky Lu](https://github.com/jackywlu)

### Project Motivation

National Parks are one of America's great natural treasures. Everytime I visit a national park, I am in awe of the immense beauty within these protected lands. I've visisted Yosemite 4 times throughtout my life, and some of my favorite memories in my life have been made at national parks. I even made Yosemite's Valley View the cover of my phone case. For my passion project, I wanted to analyze visitor counts to these natural parks and create a recommender system to recommend different national parks.

### Project Submission Directory

Data

- Visitor Data: pickle files with visitor data for 10 national parks
- Model Data: pickle files with SARIMA models fit to visitor data for 10 national parks
- Recommender Data: pickle file with cosine similarity recommender based on park topics and activities

Notebooks

* Project 5 Data Collection EDA (code for collecting exploring Yosemite visitor counts and performing EDA)
* Project 5 Visitor Data (code for collecting national park visitor data)

* Project 5 National Park API (code for creating a nationl park topic/activity matrix and for exploring the API)
* Project 5 ARIMA Eval (code for evaluating ARIMA, SARIMA, and FB Prophet models)
* Project 5 Neural Net Model Eval (code for evaluating neural net models)
* Exploration Notebooks:
  * Project 5 Time Series Explore (code for exploring using different time series models)
  * Project 5 Neural Nets (code for exploring using different neural net models)

Images

- Presentation Images: images for the presentation
- Recommender Images: images for the Streamlit Recommender App

App Python Code

- Python code for deploying my time series prediction and recommender App on Streamlit

### Analysis

###### Data Collection

I obtained recreational visitor counts for the top 10 most visited national parks using the [National Park Service](https://www.nps.gov/index.htm) website. I also utilized their API to create an activity/topic matrix for each park.

###### Exploratory Data Analysis

Yosemite visitor counts show a seasonal pattern. The highest visitor counts occur in the summer months, peaking in July. Winter months had the lowest visitor counts with much lower variation. Additionally, there's a slight positive trend in the number of visitors who visited Yosemite from 1979 to 2020.

Due to the popularity of national parks and the large increase in population for the United States, I had expected the visitor counts to Yosemite to show a sharper increase in visitor counts. However, the trend was much more subtle. My guess is that national parks like Yosemite set limits on how many people can enter a park through the use of day passes and campsite reservations.

###### Time Series Modeling

I used the following time series models to predict future visitor counts for national parks: SARIMA and FB Prophet. Additionally, I used the following LSTM neural net models: simple, stacked, bidirectional, and CNN-LSTM. I compared the models against one another using mean average percent error for their predictions vs. the actual visitor counts as my metric of evaluation. I found that SARIMA predictions performed the best, followed by CNN-LSTM. SARIMA predictions had the lowest average mean average precent error and the lowest variability in this error. For the final time series model I deployed in my Streamlit app, I used a SARIMA model.

###### Content based Recommendation

For my recommender, I created a topic activity matrix using data from the National Park API. For example, Yosemite would have activities such as rock climbing or backcountry camping. Using cosine distance between different national parks, I could find how similar parks were to one another and build a content based recommender.

###### Web App

Using Streamlit, I built a web app so that users could predict visitor counts using my SARIMA model or find a national park recommendation based on my activity/topic matrix cosine distance model.

### Additional Notes

###### Techniques

* Time Series Analysis
* Content Based Recommendation
* Neural Nets
  * LSTMs & CNN
* Web App

###### Programs & Packages

* BeautifulSoup
* Jupyter Notebook
* Keras
* Matplotlib
* Numpy
* Pandas
* Requests
* Seaborn
* Sklearn
* Streamlit

###### Languages

* Python