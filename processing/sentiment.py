import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


def get_sentiment(text):
    score = analyzer.polarity_scores(str(text))["compound"]

    if score >= 0.05:
        return "Positive"

    elif score <= -0.05:
        return "Negative"

    return "Neutral"


def analyze_sentiment():

    df = pd.read_csv("data/processed/final_documents.csv")

    df["sentiment"] = df["text"].apply(get_sentiment)

    df.to_csv(
        "data/processed/sentiment_documents.csv",
        index=False
    )

    print("Sentiment analysis completed!")
    print(df["sentiment"].value_counts())


if __name__ == "__main__":
    analyze_sentiment()