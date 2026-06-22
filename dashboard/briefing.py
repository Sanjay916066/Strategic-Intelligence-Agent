import streamlit as st
from intelligence.analyzer import analyze

def show():

    st.title("👔 CEO Briefing")

    question = st.text_input(
        "Ask a strategic business question"
    )

    if st.button("Generate Briefing"):

        if not question.strip():
            st.warning("Please enter a question.")
            return

        with st.spinner("Preparing Executive Briefing..."):

            result = analyze(
                f"""
                CEO Question:

                {question}

                Produce:

                1. Executive Summary

                2. Why It Matters

                3. Recommended Actions

                4. Supporting Evidence

                5. Expected Business Impact
                """
            )

        st.success("Executive Briefing Ready")

        st.markdown(result)