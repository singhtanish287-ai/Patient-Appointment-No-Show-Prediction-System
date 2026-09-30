"""
app.py — Main entry point for the Healthcare Appointment Management System.
Run with:  streamlit run app.py
"""

import streamlit as st
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from utils.database import init_db, get_dashboard_stats

st.set_page_config(
    page_title="HealthCare Portal",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_db()

st.title("🏥 HealthCare Appointment Management System")
st.markdown("**AI-Powered Healthcare Portal** — Built with Streamlit • Gemini 2.5 Flash • Scikit-learn")
st.divider()

stats = get_dashboard_stats()
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("👤 Registered Patients",   stats["total_patients"])
with c2:
    st.metric("📅 Total Appointments",    stats["total_appointments"])
with c3:
    st.metric("✅ Completed Visits",      stats["completed"])
with c4:
    st.metric("⚠️ No-Show Count",        stats["no_shows"])

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("📅 Book Appointment")
    st.markdown("""
                ### 📅 Book Appointment
                Schedule a visit with any of our specialist doctors.
                Register as a new patient or look up your existing record.
                View your complete appointment history.

                **👈 Use the sidebar to navigate to *Book Appointment*.**
                """)

with col2:
    st.markdown("""
                ### 📊 Admin Dashboard
                Full operational overview for clinic staff.
                Manage appointment statuses, view KPI metrics,
                and explore Plotly charts.

                **👈 Navigate to *Admin Dashboard* (password: admin123).**
                """)

with col3:
    st.markdown("""
                ### 🤖 No-Show Risk Predictor
                Random Forest ML model trained on real appointment history.
                Predict risk for individual patients or run batch scoring
                across all upcoming appointments.

                **👈 Navigate to *Risk Predictor*.**
                """)

with col4:
    st.markdown("""
                ### 🤖 AI Health Assistant
                Multi-turn conversational assistant powered by
                **Gemini 2.5 Flash**. Ask health questions, get
                appointment summaries, and receive personalised guidance.

                **👈 Navigate to *AI Assistant* (API key required).**
                """)

st.divider()

t1, t2, t3, t4, t5 = st.columns(5)
with t1:
    st.info("**Streamlit 1.64**\nFull-stack Python web UI")
with t2:
    st.info("**Gemini 2.5 Flash**\nGoogle AI multi-turn LLM")
with t3:
    st.info("**Scikit-learn**\nRandom Forest classifier")
with t4:
    st.info("**Plotly**\nInteractive charts & gauges")
with t5:
    st.info("**SQLite**\nEmbedded relational database")

st.caption(
    "⚠️ This is a demonstration system. Patient data is synthetic. "
    "Always consult a real healthcare professional for medical advice. "
    "| HealthCare Portal v1.0"
)
