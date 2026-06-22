import pandas as pd


def remove_duplicates(input_file, output_file):

    df = pd.read_csv(input_file)

    before = len(df)

    df = df.drop_duplicates(
        subset=["title"],
        keep="first"
    )

    after = len(df)

    print(f"Removed {before - after} duplicate articles")

    df.to_csv(output_file, index=False)

    print(f"Saved to {output_file}")

    return df


if __name__ == "__main__":

    remove_duplicates(
        "data/processed/clean_documents.csv",
        "data/processed/final_documents.csv"
    )