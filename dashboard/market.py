import streamlit as st
import pandas as pd

def show():

    st.title("📈 Market Intelligence")

    df = pd.read_csv("data/processed/sentiment_documents.csv")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("News Sources")
        st.bar_chart(df["source"].value_counts())

    with col2:
        st.subheader("Topics")
        st.bar_chart(df["topic"].value_counts())

    st.subheader("Latest News")

    st.dataframe(
        df[
            [
                "title",
                "source",
                "sentiment"
            ]
        ].head(20),
        use_container_width=True
    )