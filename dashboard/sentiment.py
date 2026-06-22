import streamlit as st
import pandas as pd

def show():

    st.title("😊 Sentiment Analysis")

    df = pd.read_csv("data/processed/sentiment_documents.csv")

    st.subheader("Sentiment Distribution")

    st.bar_chart(df["sentiment"].value_counts())

    st.subheader("Counts")

    st.dataframe(
        df["sentiment"].value_counts()
    )