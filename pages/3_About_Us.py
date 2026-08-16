import streamlit as st

st.set_page_config(page_title="About Us", page_icon="ℹ️", layout="centered")

st.title("ℹ️ About This Project")
st.markdown("""
### Project Overview
The **MSF Financial Assistance Application Companion** is an interactive, LLM-powered web application designed to help Singaporean citizens seamlessly navigate government financial aid schemes (specifically ComCare assistance under the Ministry of Social and Family Development). 

Navigating government assistance policies can often feel dense and overwhelming. This application bridges the information gap by providing transparent, structured guidance tailored to an individual's household situation.

### 🎯 Core Objectives & Features
1. **Consolidate Information:** Aggregate publicly available policy guidelines from official sources into a single, intuitive interface.
2. **Personalize Guidance:** Allow users to evaluate their eligibility based on non-PII metrics such as Per Capita Household Income (PCHI) and employment status.
3. **Simplify Action & Document Preparation:** Provide interactive checklist readiness tracking, a physical Social Service Office (SSO) directory with direct map links, and a **floating AI conversational assistant** to help users troubleshoot document retrieval (e.g., pulling CPF histories or payslips).

### 🏛️ Official Data Sources & References
* [MSF ComCare Official Portal](https://www.msf.gov.sg/what-we-do/comcare)
* [SupportGoWhere Digital Portal](https://supportgowhere.life.gov.sg/)

### ⚠️ Disclaimer
*This web application is developed strictly as an individual capstone project for educational evaluation. It serves as an informative assistant and does not constitute an official government assessment or binding financial aid approval. For official applications, please visit SupportGoWhere or approach your nearest Social Service Office.*
""")