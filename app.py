import streamlit as st

from dashboard.overview import show as overview_page
from dashboard.market import show as market_page
from dashboard.opportunities import show as opportunities_page
from dashboard.risks import show as risks_page
from dashboard.recommendations import show as recommendations_page
from dashboard.briefing import show as briefing_page

st.set_page_config(
    page_title="Tesla AI CEO Strategic Intelligence Agent",
    page_icon="🚗",
    layout="wide"
)

st.sidebar.title("🚗 Tesla AI CEO Agent")

page = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "Market Intelligence",
        "Opportunities",
        "Risks",
        "Recommendations",
        "CEO Briefing"
    ]
)

if page == "Overview":
    overview_page()

elif page == "Market Intelligence":
    market_page()

elif page == "Opportunities":
    opportunities_page()

elif page == "Risks":
    risks_page()

elif page == "Recommendations":
    recommendations_page()

elif page == "CEO Briefing":
    briefing_page()