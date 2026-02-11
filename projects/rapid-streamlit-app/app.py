"""
Rapid Production Streamlit App - Mockup
A client-facing application for bank tellers to check customer eligibility.
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Client Eligibility Check",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS for status indicators
st.markdown(
    """
<style>
    .status-ok {
        background-color: #28a745;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        font-weight: bold;
        font-size: 18px;
        text-align: center;
    }
    .status-not-ok {
        background-color: #dc3545;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        font-weight: bold;
        font-size: 18px;
        text-align: center;
    }
    .info-box {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 5px;
        border-left: 4px solid #007bff;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Sidebar
with st.sidebar:
    st.header("Navigation")
    st.markdown("""
    - **Home** - Client Lookup
    - **Admin Panel** - Usage Statistics
    - **Reports** - Generate Reports
    """)
    st.divider()
    st.caption("User: J.Smith")
    st.caption("Branch: London Central")

# Main content
st.title("🏦 Client Eligibility Check")
st.markdown("Enter client ID to verify eligibility for financial products.")

st.divider()

# Client ID input form
with st.form("client_lookup"):
    client_id = st.text_input(
        "Client ID",
        placeholder="Enter 11-digit client ID (e.g., 12345678901)",
        max_chars=11,
        help="Enter the client's unique identifier",
    )

    col1, col2 = st.columns([3, 1])
    with col1:
        submitted = st.form_submit_button(
            "🔍 Check Eligibility", use_container_width=True, type="primary"
        )
    with col2:
        clear = st.form_submit_button("Clear", use_container_width=True)

# Display results when form is submitted
if submitted and client_id:
    with st.spinner("Checking eligibility..."):
        # Simulate database lookup delay
        import time

        time.sleep(0.5)

    # Mock client data (always same regardless of input)
    st.success("Client found in database")

    st.subheader("📋 Client Information")

    # Client details in a table
    client_data = {
        "Field": [
            "Client ID",
            "Customer Since",
            "Segment",
            "Risk Category",
            "Last Activity",
        ],
        "Value": [
            client_id if client_id else "12345678901",
            "2019-03-15",
            "Premium",
            "Low",
            "2024-01-18",
        ],
    }

    df_client = pd.DataFrame(client_data)
    st.table(df_client)

    st.divider()

    # Eligibility results
    st.subheader("📊 Product Eligibility")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Cash Loan**")
        st.markdown('<div class="status-ok">✓ ELIGIBLE</div>', unsafe_allow_html=True)
        st.caption("Max amount: 50,000 PLN")

    with col2:
        st.markdown("**Credit Card**")
        st.markdown('<div class="status-ok">✓ ELIGIBLE</div>', unsafe_allow_html=True)
        st.caption("Limit: 15,000 PLN")

    st.markdown("")  # Spacer

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("**Mortgage Refinancing**")
        st.markdown(
            '<div class="status-not-ok">✗ NOT ELIGIBLE</div>', unsafe_allow_html=True
        )
        st.caption("Reason: No active mortgage")

    with col4:
        st.markdown("**Investment Products**")
        st.markdown('<div class="status-ok">✓ ELIGIBLE</div>', unsafe_allow_html=True)
        st.caption("All categories available")

    st.divider()

    # Timestamp and audit info
    st.caption(f"Query timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    st.caption("This query has been logged for audit purposes.")

elif submitted and not client_id:
    st.error("Please enter a valid Client ID")

# Footer
st.divider()
st.caption("Internal use only. All queries are logged and monitored.")
