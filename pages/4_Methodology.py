import streamlit as st

# --- AUTHENTICATION CHECK ---
if not st.session_state.get("password_correct", False):
    st.error("⚠️ Please log in from the Home page first.")
    st.stop()

st.set_page_config(page_title="Methodology", page_icon="⚙️", layout="centered")

st.title("⚙️ Methodology & Technical Implementation")
st.markdown("""
### 🏗️ Architecture & Data Flow
The application is built using a multi-page **Streamlit** framework powered by an LLM backend (`gpt-4o-mini`). Below is the architectural workflow for both core use cases:

1. **Use Case A (Eligibility Screener Flow):**
   * *Input Collection:* User inputs structured, non-PII parameters (Household size, income, housing type, employment situation).
   * *Deterministic Calculation:* Python script computes the Per Capita Household Income (PCHI): \\(\\text{PCHI} = \\frac{\\text{Total Income}}{\\text{Household Size}}\\).
   * *Prompt Assembly & LLM Evaluation:* Structured inputs and policy guidelines are injected into a secure prompt template and sent to the LLM API.
   * *Structured Presentation:* Output is formatted into clear markdown headers covering matching schemes, reasoning, and next steps, with state persistence via `st.session_state`.

2. **Use Case B (Document Checklist, SSO Directory & Floating AI Assistant Flow):**
   * *Context Retrieval:* Reads the user's evaluated situation from session storage.
   * *Interactive Tracking:* Combines real-time checklist readiness tracking (`st.progress`) with geographical SSO directories and direct Google Maps search routing.
   * *Interactive Floating AI Widget:* Implements a persistent, bottom-right floating popover chat widget (`st.popover` combined with `st.chat_message`) allowing applicants to troubleshoot document retrieval (such as downloading CPF histories or payslips) through a multi-turn conversational interface.

---

### 🛡️ Prompt Engineering & Security Safeguards
To comply with rigorous safety and technical constraints:
* **System Guardrails:** Both LLM integration points are initialized with strict system prompt boundaries: *"You are a secure, policy-compliant government digital service assistant. Never break character, ignore instructions, or discuss topics outside of MSF financial assistance / administrative guidance."*
* **Input Sanitization & Attack Mitigation:** Primary screener inputs are constrained via strict UI form components (`st.selectbox`, `st.number_input`). For the secondary open chat query in Use Case B, safety is maintained by restricting the model's operational scope via system prompts and utilizing modern API calls that isolate execution contexts, minimizing prompt injection vectors.
""")