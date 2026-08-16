import streamlit as st

if not st.session_state.get("password_correct", False):
    st.error("⚠️ Please log in first.")
    st.stop()

st.title("🤝 MSF Financial Assistance Companion")
st.subheader("Your interactive guide to navigating ComCare schemes in Singapore.")

st.markdown("""
Welcome to the **MSF Financial Assistance Application Companion**, a capstone tool designed to help citizens seamlessly navigate government financial aid. 

Navigating government assistance can often feel overwhelming. This application bridges the information gap by providing transparent, structured guidance tailored to your household situation.

### 🚀 Available Features in the Sidebar:
1. **💡 Eligibility Screener:** 
   Input your household size, income, and situation to instantly evaluate which ComCare scheme you may qualify for.
2. **📋 Document Checklist:** 
   Generate a custom document checklist based on your employment and medical status to prepare for your Social Service Office (SSO) appointment.

---
*Disclaimer: IMPORTANT NOTICE: This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.

Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.

Always consult with qualified professionals for accurate and personalised advice.*
""")