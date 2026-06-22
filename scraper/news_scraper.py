import feedparser
import pandas as pd
from urllib.parse import quote_plus
from datetime import datetime
from config import GOOGLE_NEWS_TOPICS


def scrape_news(max_articles=20):
    articles = []

    for topic in GOOGLE_NEWS_TOPICS:

        print(f"Collecting {topic}...")

        query = quote_plus(topic)

        url = f"https://news.google.com/rss/search?q={query}"

        feed = feedparser.parse(url)

        for entry in feed.entries[:max_articles]:
            articles.append({
                "title": entry.get("title", ""),
                "summary": entry.get("summary", ""),
                "link": entry.get("link", ""),
                "published": entry.get("published", ""),
                "source": "Google News",
                "topic": topic,
                "collected_at": datetime.now().isoformat()
            })

    df = pd.DataFrame(articles)

    print(f"\nCollected {len(df)} articles")

    return df


if __name__ == "__main__":

    news = scrape_news()

    print(news.head())