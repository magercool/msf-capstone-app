import streamlit as st

st.set_page_config(
    page_title="MSF Assistance Companion",
    page_icon="🤝",
    layout="centered"
)

def check_password():
    """Returns True if the user entered the correct password."""
    def password_entered():
        if st.session_state["password"] == st.secrets.get("app_password", "default_fallback_pass"):
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if st.session_state.get("password_correct", False):
        return True

    st.title("🔒 Restricted Access")
    st.write("Please enter the password to access this capstone application.")
    
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    
    if "password_correct" in st.session_state and not st.session_state["password_correct"]:
        st.error("😕 Password incorrect. Please try again.")
        
    return False

# Stop execution if password is not correct
if not check_password():
    st.stop()

# ==========================================
# APP CONTENT
# ==========================================
st.title("🤝 MSF Financial Assistance Companion")
st.subheader("Your interactive guide to navigating ComCare schemes in Singapore.")

st.markdown("---")
st.subheader("Get Started")
col1, col2 = st.columns(2)

with col1:
    if st.button("💡 Open Eligibility Screener", use_container_width=True):
        st.switch_page("pages/1_Eligibility_Screener.py")
    if st.button("📋 Open Document Checklist", use_container_width=True):
        st.switch_page("pages/2_Document_Checklist.py")

with col2:
    if st.button("ℹ️ About Us", use_container_width=True):
        st.switch_page("pages/3_About_Us.py")
    if st.button("⚙️ Methodology", use_container_width=True):
        st.switch_page("pages/4_Methodology.py")

st.markdown("""
Welcome to the **MSF Financial Assistance Application Companion**, a capstone tool designed to help citizens seamlessly navigate government financial aid. 

Navigating government assistance can often feel overwhelming. This application bridges the information gap by providing transparent, structured guidance tailored to your household situation.

### 🚀 Available Features
1. **💡 Eligibility Screener:** 
   Input your household size, income, and situation to instantly evaluate which ComCare scheme you may qualify for.
2. **📋 Document Checklist Generator:** 
   Generate a custom document checklist based on your employment and medical status to prepare for your Social Service Office (SSO) appointment.

---
*Disclaimer: This is a student capstone project developed for educational purposes. For official applications, please visit [SupportGoWhere](https://supportgowhere.life.gov.sg/).*
""")

