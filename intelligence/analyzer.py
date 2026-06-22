from database.retrieval import search
from intelligence.llm import generate


def analyze(question):

    # Retrieve the top 5 relevant documents
    results = search(question, n_results=5)

    # Combine all retrieved documents into one context
    context = "\n\n".join(results["documents"][0])

    prompt = f"""
You are Tesla's AI Strategic Intelligence Advisor.

Use ONLY the evidence provided below to answer the question.

Question:
{question}

Evidence:
{context}

Return your answer in the following format:

# Executive Summary

# Opportunities

# Risks

# Competitor Analysis

# Strategic Recommendations

For every recommendation include:
- Priority (High/Medium/Low)
- Supporting Evidence
- Expected Business Impact
- Risk Level

If the evidence is insufficient, clearly state that.
"""

    return generate(prompt)