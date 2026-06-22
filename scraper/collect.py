import os
import pandas as pd

from scraper.news_scraper import scrape_news
from scraper.market_scraper import scrape_market_news


def collect_all():

    print("=" * 60)
    print("Collecting Tesla News...")
    news_df = scrape_news()

    print("\nCollecting Competitor News...")
    market_df = scrape_market_news()

    # Merge all data
    all_data = pd.concat(
        [news_df, market_df],
        ignore_index=True
    )

    # Remove duplicate articles
    all_data.drop_duplicates(
        subset=["title"],
        inplace=True
    )

    # Create data/raw folder
    os.makedirs("data/raw", exist_ok=True)

    output_file = "data/raw/documents.csv"

    all_data.to_csv(output_file, index=False)

    print("\n" + "=" * 60)
    print(f"Total Articles Collected : {len(all_data)}")
    print(f"Saved to : {output_file}")

    return all_data


if __name__ == "__main__":
    collect_all()