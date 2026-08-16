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

if not check_password():
    st.stop()

# --- DEFINE CUSTOM MULTI-PAGE NAVIGATION ---
pg = st.navigation({
    "Navigation": [
        st.Page("main.py", title="Home", icon="🏠"),
        st.Page("pages/1_Eligibility_Screener.py", title="Eligibility Screener", icon="💡"),
        st.Page("pages/2_Document_Checklist.py", title="Document Checklist", icon="📋"),
        st.Page("pages/3_About_Us.py", title="About Us", icon="ℹ️"),
        st.Page("pages/4_Methodology.py", title="Methodology", icon="⚙️"),
    ]
})

# Run the selected page
pg.run()