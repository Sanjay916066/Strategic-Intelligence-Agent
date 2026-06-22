import pandas as pd
import re

print("✅ clean.py loaded")


def clean_text(text):
    if pd.isna(text):
        return ""

    text = str(text)
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def clean_dataset(input_file, output_file):

    print("📄 Reading:", input_file)

    df = pd.read_csv(input_file)

    print(f"Loaded {len(df)} rows")

    df["title"] = df["title"].apply(clean_text)
    df["summary"] = df["summary"].apply(clean_text)

    df["text"] = df["title"] + ". " + df["summary"]

    df.to_csv(output_file, index=False)

    print(f"✅ Saved to {output_file}")

    return df


if __name__ == "__main__":

    print("🚀 Running clean.py")

    clean_dataset(
        "data/raw/documents.csv",
        "data/processed/clean_documents.csv"
    )