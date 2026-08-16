import streamlit as st

st.set_page_config(
    page_title="MSF Assistance Companion",
    page_icon="🤝",
    layout="centered",
    initial_sidebar_state="expanded"
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
# NAVIGATION SETUP
# ==========================================
pg = st.navigation({
    "Main Menu": [
        st.Page("main.py", title="Home", icon="🏠"),
    ],
    "Capstone Modules": [
        st.Page("pages/1_Eligibility_Screener.py", title="Eligibility Screener", icon="💡"),
        st.Page("pages/2_Document_Checklist.py", title="Document Checklist", icon="📋"),
    ],
    "Documentation": [
        st.Page("pages/3_About_Us.py", title="About Us", icon="ℹ️"),
        st.Page("pages/4_Methodology.py", title="Methodology", icon="⚙️"),
    ]
})

# ==========================================
# HOME PAGE CONTENT
# ==========================================
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
👉 **Please use the left sidebar menu to navigate between the application modules.**

---
*Disclaimer: This is a student capstone project developed for educational purposes. For official applications, please visit [SupportGoWhere](https://supportgowhere.life.gov.sg/).*
""")

# Run the navigation manager at the very end
pg.run()