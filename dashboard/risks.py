import streamlit as st
from intelligence.analyzer import analyze

def show():

    st.title("⚠ Risk Monitor")

    st.warning("Monitor strategic and competitive risks.")

    if st.button("Generate Risk Analysis"):

        with st.spinner("Analyzing risks..."):

            result = analyze(
                "Identify Tesla's major business risks. "
                "For each risk provide: "
                "1. Risk Title "
                "2. Risk Category "
                "3. Severity (High/Medium/Low) "
                "4. Supporting Evidence "
                "5. Confidence Score (%)"
            )

        st.success("Analysis Complete")
        st.markdown(result)