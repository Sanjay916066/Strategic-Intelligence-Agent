import pandas as pd


def chunk_text(text, chunk_size=250):
    words = str(text).split()

    return [
        " ".join(words[i:i + chunk_size])
        for i in range(0, len(words), chunk_size)
    ]


def create_chunks(input_file, output_file):

    df = pd.read_csv(input_file)

    chunks = []

    for _, row in df.iterrows():

        text = row.get("text", "")

        if pd.isna(text):
            continue

        for chunk in chunk_text(text):

            chunks.append({
                "title": row["title"],
                "text": chunk,
                "source": row["source"],
                "link": row["link"]
            })

    chunk_df = pd.DataFrame(chunks)

    chunk_df.to_csv(output_file, index=False)

    print(f"Created {len(chunk_df)} chunks")

    return chunk_df


if __name__ == "__main__":

    create_chunks(
        "data/processed/final_documents.csv",
        "data/processed/chunks.csv"
    )