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
*Disclaimer: This is a student capstone project developed for educational purposes. For official applications, please visit [SupportGoWhere](https://supportgowhere.life.gov.sg/).*
""")