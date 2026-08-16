import streamlit as st
from openai import OpenAI

# --- AUTHENTICATION CHECK ---
if not st.session_state.get("password_correct", False):
    st.error("⚠️ Please log in from the Home page first.")
    st.stop()

st.set_page_config(page_title="Document Checklist & AI Guide", page_icon="📋", layout="centered")

st.title("📋 Document Checklist & SSO Directory")
st.write("Prepare your required paperwork, track your readiness, and locate your nearest Social Service Office (SSO).")

# Check if data was passed from the screener
if "evaluated_situation" in st.session_state:
    st.success(f"📌 **Tailored Profile:** {st.session_state['evaluated_situation']} (PCHI: ${st.session_state.get('evaluated_pchi', 0):.2f})")
else:
    st.info("💡 Tip: Complete the **Eligibility Screener** first for a tailored profile checklist!")

st.markdown("---")

# Interactive Progress Tracker
st.subheader("✅ Document Readiness Tracker")
col1, col2 = st.columns(2)
with col1:
    doc1 = st.checkbox("NRIC / Birth Certificates")
    doc2 = st.checkbox("Proof of Residence")
    doc3 = st.checkbox("Latest 3-6 Months Bank Statements")
with col2:
    doc4 = st.checkbox("Payslips / CPF History")
    doc5 = st.checkbox("Medical Certificates / Memos")
    doc6 = st.checkbox("Financial Declaration Forms")

completed_count = sum([doc1, doc2, doc3, doc4, doc5, doc6])
st.progress(completed_count / 6, text=f"Preparation Progress: {completed_count}/6 items ready")

st.markdown("---")

# Situation-Specific Guidance
situation = st.session_state.get("evaluated_situation", "Employed with low income")
st.subheader("📂 Requirements for Your Situation")
if "Employed" in situation:
    st.markdown("- **Payslips:** Last 3 months for all working household members.")
    st.markdown("- **CPF Statement:** Past 12 months CPF contribution history.")
elif "unemployed" in situation or "Medical" in situation:
    st.markdown("- **Medical Documentation:** Doctor memos or MCs stating unfitness for work.")
    st.markdown("- **Exit Proof:** Resignation letter or termination notice.")
elif "Caregiver" in situation:
    st.markdown("- **Care Documentation:** Medical reports of the care recipient.")
else:
    st.markdown("- **Income Declarations:** Notice of Assessment or supporting letters.")

st.markdown("---")

# Actionable SSO Directory with Google Maps integration links
st.subheader("📍 Social Service Office (SSO) Directory")
st.write("Select your region to view office addresses, operating contacts, and direct map links:")

region = st.selectbox("Select Region:", [
    "-- Choose Region --", 
    "North (Yishun / Woodlands)", 
    "South / Central (Toa Payoh / Queenstown)", 
    "East (Tampines / Bedok)", 
    "West (Chua Chu Kang / Jurong East)"
])

if region == "North (Yishun / Woodlands)":
    st.markdown("""
    *   **SSO @ Yishun**  
        📍 746 Yishun Street 72, #01-127, Singapore 760746  
        🗺️ [Open in Google Maps](https://maps.google.com/?q=SSO+@+Yishun)
    *   **SSO @ Woodlands**  
        📍 Blk 852 Woodlands Street 83, #01-1, Singapore 730852  
        🗺️ [Open in Google Maps](https://maps.google.com/?q=SSO+@+Woodlands)
    """)
elif region == "South / Central (Toa Payoh / Queenstown)":
    st.markdown("""
    *   **SSO @ Toa Payoh**  
        📍 490 Lorong 6 Toa Payoh, HDB Hub Bizthree, #07-11, Singapore 310490  
        🗺️ [Open in Google Maps](https://maps.google.com/?q=SSO+@+Toa+Payoh)
    *   **SSO @ Queenstown**  
        📍 Blk 168 Stirling Road, #01-1144, Singapore 140168  
        🗺️ [Open in Google Maps](https://maps.google.com/?q=SSO+@+Queenstown)
    """)
elif region == "East (Tampines / Bedok)":
    st.markdown("""
    *   **SSO @ Tampines**  
        📍 Blk 103 Tampines Street 11, #01-193, Singapore 521103  
        🗺️ [Open in Google Maps](https://maps.google.com/?q=SSO+@+Tampines)
    *   **SSO @ Bedok**  
        📍 Blk 418 Bedok North Ave 2, #01-95, Singapore 460418  
        🗺️ [Open in Google Maps](https://maps.google.com/?q=SSO+@+Bedok)
    """)
elif region == "West (Chua Chu Kang / Jurong East)":
    st.markdown("""
    *   **SSO @ Chua Chu Kang**  
        📍 8A Teck Whye Lane, Singapore 681008  
        🗺️ [Open in Google Maps](https://maps.google.com/?q=SSO+@+Chua+Chu+Kang)
    *   **SSO @ Jurong East**  
        📍 Blk 249 Jurong East Street 24, #01-209, Singapore 600249  
        🗺️ [Open in Google Maps](https://maps.google.com/?q=SSO+@+Jurong+East)
    """)

if region != "-- Choose Region --":
    st.info("📞 **ComCare General Hotline:** 1800-111-2222 (7 AM – 12 Midnight daily)")

st.markdown("---")

# --- FLOATING BOTTOM-RIGHT CHAT WIDGET ---
st.markdown("""
<style>
/* Pin the popover element securely to the bottom right */
[data-testid="stPopover"] {
    position: fixed !important;
    bottom: 20px !important;
    right: 20px !important;
    z-index: 999999 !important;
    width: auto !important;
}

/* Style the trigger button to look like a neat floating action button */
[data-testid="stPopover"] > button {
    background-color: #ff4b4b !important;
    color: white !important;
    border-radius: 28px !important;
    padding: 0.5rem 1rem !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.2) !important;
    border: none !important;
}

[data-testid="stPopover"] > button:hover {
    background-color: #ff2b2b !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

with st.popover("🤖 Need Help?"):
    st.write("### AI Document Assistant")
    st.write("Ask how to download CPF statements, secure payslips, or retrieve medical records.")
    
    if "doc_chat_history" not in st.session_state:
        st.session_state.doc_chat_history = [
            {"role": "assistant", "content": "Hello! How can I help you gather your documents today?"}
        ]
        
    for message in st.session_state.doc_chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
    user_query = st.chat_input("Ask a document question...", key="floating_popover_input")
    
    if user_query:
        st.session_state.doc_chat_history.append({"role": "user", "content": user_query})
        with st.chat_message("user"):
            st.markdown(user_query)
            
        with st.chat_message("assistant"):
            with st.spinner("Checking official guidelines..."):
                try:
                    api_key = st.secrets.get("OPENAI_API_KEY")
                    client = OpenAI(api_key=api_key)
                    
                    prompt = f"""
                    You are a helpful, warm, and clear digital assistant for Singapore's Ministry of Social and Family Development (MSF).
                    A citizen applying for ComCare financial assistance needs help obtaining a document.
                    
                    Citizen's Question: "{user_query}"
                    Their Profile Situation: {situation}
                    
                    Provide simple, step-by-step instructions on how they can retrieve this document online (via Singpass, CPF portal, IRAS, etc.) or offline. Keep the language very simple, reassuring, and practical, avoiding complex tech jargon.
                    """
                    
                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[
                            {"role": "system", "content": "You are a secure, policy-compliant government digital service assistant. Always respond using simple, reassuring, and clear English."},
                            {"role": "user", "content": prompt}
                        ]
                    )
                    
                    ai_reply = response.choices[0].message.content
                    st.markdown(ai_reply)
                    st.session_state.doc_chat_history.append({"role": "assistant", "content": ai_reply})
                except Exception as e:
                    error_msg = f"Error connecting to AI service: {e}"
                    st.error(error_msg)