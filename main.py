import streamlit as st
import plotly.express as px
import re
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

diaries = ["diary/2023-10-21.txt", "diary/2023-10-22.txt", "diary/2023-10-23.txt", "diary/2023-10-23.txt",
           "diary/2023-10-23.txt", "diary/2023-10-26.txt", "diary/2023-10-27.txt"]
positive_list = []
negativity_list = []
dates = []
for diary in diaries:

    with open(f"{diary}", "r") as file:
        content = file.read()
    analysis = SentimentIntensityAnalyzer()
    score = analysis.polarity_scores(content)
    date = diary[14:16]
    dates.append(date)
    # print(score)
    for (key, value) in score.items():
        if key == "pos":
            positive_list.append(value)
        elif key == "neg":
            negativity_list.append(value)

st.title("Diary tone")

figure = px.line(x=dates, y=positive_list, labels={"x": "Dates",
                                                   "y": "Positivity"})

st.subheader("Positivity")
st.plotly_chart(figure)
st.subheader("Negativity")
figure2 = px.line(x=dates, y=negativity_list, labels={"x": "Dates",
                                                      "y": "Negativity"})
st.plotly_chart(figure2)

