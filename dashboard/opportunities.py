import streamlit as st
from intelligence.analyzer import analyze

def show():

    st.title("🚀 Opportunity Monitor")

    st.info("Identify strategic opportunities for Tesla based on the latest intelligence.")

    if st.button("Generate Opportunity Analysis"):

        with st.spinner("Analyzing opportunities..."):

            result = analyze(
                "Identify the top business opportunities for Tesla. "
                "For each opportunity provide: "
                "1. Opportunity Title "
                "2. Impact Level (High/Medium/Low) "
                "3. Supporting Evidence "
                "4. Confidence Score (%)"
            )

        st.success("Analysis Complete")
        st.markdown(result)