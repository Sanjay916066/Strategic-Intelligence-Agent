import streamlit as st
import pandas as pd
from datetime import datetime

def show():

    st.title("📊 Tesla Strategic Intelligence Dashboard")

    df = pd.read_csv("data/processed/sentiment_documents.csv")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Articles", len(df))
    c2.metric("Sources", df["source"].nunique())
    c3.metric("Topics", df["topic"].nunique())
    c4.metric("Industry", "Electric Vehicles")

    st.write("Last Updated:", datetime.now().strftime("%d-%m-%Y %H:%M"))

    st.divider()

    st.subheader("Latest Intelligence")

    st.dataframe(
        df[
            [
                "title",
                "source",
                "sentiment"
            ]
        ].head(10),
        use_container_width=True
    )