import feedparser
import pandas as pd
from urllib.parse import quote_plus
from datetime import datetime
from config import COMPETITORS


def scrape_market_news(max_articles=20):

    articles = []

    for company in COMPETITORS:

        print(f"Collecting competitor: {company}")

        query = quote_plus(company)

        url = f"https://news.google.com/rss/search?q={query}"

        feed = feedparser.parse(url)

        for entry in feed.entries[:max_articles]:

            articles.append({

                "title": entry.get("title", ""),

                "summary": entry.get("summary", ""),

                "link": entry.get("link", ""),

                "published": entry.get("published", ""),

                "source": "Competitor News",

                "topic": company,

                "collected_at": datetime.now().isoformat()

            })

    df = pd.DataFrame(articles)

    print(f"\nCollected {len(df)} competitor articles")

    return df


if __name__ == "__main__":

    df = scrape_market_news()

    print(df.head())