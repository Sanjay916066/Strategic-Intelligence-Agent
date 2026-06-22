import streamlit as st
from intelligence.analyzer import analyze

def show():

    st.title("💡 Strategic Recommendations")

    if st.button("Generate Recommendations"):

        with st.spinner("Generating recommendations..."):

            result = analyze(
                "Act as Tesla's CEO advisor. "
                "Provide the Top 5 strategic recommendations. "
                "For each recommendation include: "
                "Priority (High/Medium/Low), "
                "Supporting Evidence, "
                "Expected Business Impact, "
                "Risk Level."
            )

        st.success("Recommendations Ready")
        st.markdown(result)