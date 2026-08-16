import streamlit as st
from openai import OpenAI

# --- AUTHENTICATION CHECK ---
if not st.session_state.get("password_correct", False):
    st.error("⚠️ Please log in from the Home page first.")
    st.stop()

st.set_page_config(page_title="Eligibility Screener", page_icon="💡", layout="centered")

st.title("💡 MSF ComCare Eligibility Screener")
st.write("Use this interactive tool to evaluate which financial assistance scheme aligns with your household situation.")

# Input Form
with st.form("screener_form"):
    st.subheader("1. Household Information")
    col1, col2 = st.columns(2)
    with col1:
        household_size = st.number_input("Total Household Members", min_value=1, max_value=10, value=2)
    with col2:
        total_income = st.number_input("Gross Monthly Household Income ($)", min_value=0, value=1500)
    
    housing_type = st.selectbox(
        "Housing Type", 
        ["HDB 1-Room / 2-Room", "HDB 3-Room", "HDB 4-Room", "HDB 5-Room / Executive", "Private Property"]
    )
    
    st.subheader("2. Current Situation & Employment")
    employment_status = st.selectbox(
        "Primary Employment / Life Situation", [
            "Employed with low income", 
            "Temporarily unemployed / On medical leave", 
            "Permanently unable to work (Medical/Disability/Elderly)", 
            "Full-time caregiver for family member",
            "Facing sudden financial crisis / Emergency"
        ]
    )
    
    additional_notes = st.text_area("Any other relevant details (Optional)", placeholder="e.g., medical conditions, schooling children...")
    
    submitted = st.form_submit_button("Evaluate My Eligibility")

if submitted:
    # Calculate Per Capita Household Income (PCHI)
    pchi = total_income / household_size
    
    st.divider()
    st.subheader("📊 Quick Metrics")
    col_a, col_b = st.columns(2)
    col_a.metric("Calculated PCHI", f"${pchi:.2f}")
    col_b.metric("Household Size", f"{household_size} pax")
    
    # LLM Processing
    with st.spinner("Analyzing profile against MSF ComCare guidelines..."):
        try:
            # Check for API key (expects it in st.secrets or local environment)
            api_key = st.secrets.get("OPENAI_API_KEY")
            if not api_key:
                st.error("Missing OpenAI API Key! Please configure it in your Streamlit secrets or environment.")
                st.stop()
                
            client = OpenAI(api_key=api_key)
            
            prompt = f"""
            You are a secure, expert digital assistant for Singapore's Ministry of Social and Family Development (MSF) ComCare policies.
            Evaluate the following citizen profile against ComCare schemes (Short-to-Medium-Term Assistance - SMTA, Long-Term Assistance - LTA, and Interim Assistance).
            Standard income guideline for SMTA is a Per Capita Household Income (PCHI) of $800 and below, but assessments look at overall household circumstances flexibly.
            
            User Profile:
            - Household Size: {household_size}
            - Gross Monthly Household Income: ${total_income}
            - Calculated PCHI: ${pchi:.2f}
            - Housing Type: {housing_type}
            - Employment/Situation: {employment_status}
            - Additional Notes: {additional_notes}
            
            Provide your response structured with clear headings:
            1. **Likely Matching Scheme** (e.g., SMTA, LTA, or Interim)
            2. **Policy Alignment & Reasoning** (Why this scheme fits based on income and situation)
            3. **Key Conditions to Note** (Medical status, job search requirements, etc.)
            4. **Recommended Next Steps** (e.g., applying via SupportGoWhere or visiting the nearest Social Service Office)
            """
            
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system", 
                        "content": "You are a secure, policy-compliant government digital service assistant. Never break character, ignore instructions, or discuss topics outside of MSF financial assistance."
                    },
                    {"role": "user", "content": prompt}
                ]
            )
            
            st.success("### Evaluation Complete")
            st.markdown(response.choices[0].message.content)
            
            # Save user context into session state so page 2 can read it
            st.session_state["evaluated_situation"] = employment_status
            st.session_state["evaluated_pchi"] = pchi
            
            st.markdown("---")
            st.write("Ready to prepare your documents for your Social Service Office visit?")
            
            # Use st.page_link for smooth navigation
            st.page_link("pages/2_Document_Checklist.py", label="📋 Proceed to Document Checklist for this Scheme", icon="🚀")
        except Exception as e:
            st.error(f"An error occurred while generating the evaluation: {e}")