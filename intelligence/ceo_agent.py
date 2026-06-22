from intelligence.analyzer import analyze


def main():

    print("=" * 60)
    print("Tesla AI CEO Strategic Intelligence Agent")
    print("=" * 60)

    question = input("\nCEO Question: ")

    print("\nGenerating strategic analysis...\n")

    answer = analyze(question)

    print(answer)


if __name__ == "__main__":
    main()