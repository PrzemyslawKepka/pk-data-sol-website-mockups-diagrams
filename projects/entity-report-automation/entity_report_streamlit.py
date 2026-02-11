"""
Entity Report Control Panel - Streamlit Mockup
A Streamlit-based UI for the Entity Report generation process.
Shows data source validation, chart previews, and report generation.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import time

st.set_page_config(
    page_title="Entity Report - Control Panel",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .stDataFrame {
        font-size: 14px;
    }
    .status-ok {
        background-color: #c6f6d5;
        padding: 4px 8px;
        border-radius: 4px;
        color: #22543d;
    }
    .status-warn {
        background-color: #fefcbf;
        padding: 4px 8px;
        border-radius: 4px;
        color: #744210;
    }
    .status-error {
        background-color: #fed7d7;
        padding: 4px 8px;
        border-radius: 4px;
        color: #822727;
    }
    .big-font {
        font-size: 24px !important;
        font-weight: bold;
    }
    div[data-testid="stMetricValue"] {
        font-size: 28px;
    }
</style>
""", unsafe_allow_html=True)


def get_validation_data():
    """Generate mock validation data for data sources."""
    return pd.DataFrame({
        "Source": [
            "SQL - Risk Database",
            "SQL - Portfolio Database",
            "SQL - Provisions DB",
            "Excel - Market Data",
            "Excel - Manual Adjustments",
            "SharePoint - Pre-built Slides",
            "Excel - Sector Mapping",
            "SQL - Customer Data",
        ],
        "Type": [
            "Database", "Database", "Database", "File",
            "File", "SharePoint", "File", "Database"
        ],
        "Status": [
            "Available", "Available", "Available", "Available",
            "Available", "Available", "Pending Review", "Available"
        ],
        "Last Updated": [
            "2023-12-15 08:30", "2023-12-15 08:30", "2023-12-15 09:15",
            "2023-12-14 16:45", "2023-12-15 10:00", "2023-12-13 14:20",
            "2023-12-10 11:30", "2023-12-15 08:30"
        ],
        "Records": [
            "2,145", "45,892", "8,234", "156",
            "23", "12 slides", "89", "12,456"
        ],
    })


def get_portfolio_data():
    """Generate mock portfolio exposure data."""
    return pd.DataFrame({
        "Segment": ["Large Corporate", "SME", "Micro Enterprise", "Specialized", "Project Finance"],
        "Exposure": [18450, 12890, 8234, 4120, 2198],
        "NPL_Rate": [1.2, 3.8, 4.5, 2.1, 0.8],
        "Coverage": [72.5, 65.2, 58.9, 78.3, 82.1],
    })


def get_rating_data():
    """Generate mock rating distribution data."""
    return pd.DataFrame({
        "Rating": ["AAA-AA", "A", "BBB", "BB", "B & Below"],
        "Exposure": [8920, 12450, 15670, 6234, 2618],
        "Percentage": [19.4, 27.1, 34.2, 13.6, 5.7],
    })


def get_trend_data():
    """Generate mock monthly trend data."""
    return pd.DataFrame({
        "Month": ["Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "Exposure": [42890, 43120, 43567, 44230, 45120, 45892],
        "NPL": [3.1, 3.0, 2.9, 2.9, 2.8, 2.8],
    })


def style_status(val):
    """Apply color styling to status column."""
    if val == "Available":
        return 'background-color: #c6f6d5; color: #22543d'
    elif val == "Pending Review":
        return 'background-color: #fefcbf; color: #744210'
    else:
        return 'background-color: #fed7d7; color: #822727'


def main():
    # Sidebar
    with st.sidebar:
        st.image("https://via.placeholder.com/200x60?text=Entity+Report", width=200)
        st.markdown("---")
        st.markdown("### Report Settings")

        report_month = st.selectbox(
            "Reporting Period",
            ["December 2023", "November 2023", "October 2023"]
        )

        report_type = st.radio(
            "Report Type",
            ["Full Report", "Executive Summary", "Risk Appendix"]
        )

        st.markdown("---")
        st.markdown("### Generation Options")

        include_charts = st.checkbox("Include Charts", value=True)
        include_tables = st.checkbox("Include Data Tables", value=True)
        include_appendix = st.checkbox("Include Appendix", value=True)

        st.markdown("---")
        st.markdown(f"**Last Generated:** 2023-12-01")
        st.markdown(f"**Version:** v3.2.1")

    # Main content
    st.title("Entity Report Control Panel")
    st.markdown(f"**Report Period:** {report_month} | **Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")

    # Tab layout
    tab1, tab2, tab3 = st.tabs(["Data Validation", "Chart Preview", "Generate Report"])

    # ===== TAB 1: Data Validation =====
    with tab1:
        st.header("Data Source Validation")
        st.markdown("Check availability and freshness of all data sources before generating the report.")

        validation_df = get_validation_data()

        # Summary metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            available_count = len(validation_df[validation_df["Status"] == "Available"])
            st.metric("Available Sources", f"{available_count}/{len(validation_df)}")
        with col2:
            pending_count = len(validation_df[validation_df["Status"] == "Pending Review"])
            st.metric("Pending Review", pending_count)
        with col3:
            st.metric("Database Sources", len(validation_df[validation_df["Type"] == "Database"]))
        with col4:
            st.metric("File Sources", len(validation_df[validation_df["Type"] != "Database"]))

        st.markdown("---")

        # Styled validation table
        styled_df = validation_df.style.applymap(
            style_status, subset=["Status"]
        ).set_properties(**{
            'text-align': 'left',
            'font-size': '14px',
        })

        st.dataframe(
            styled_df,
            use_container_width=True,
            hide_index=True,
            height=350
        )

        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button("Refresh All Sources", type="secondary"):
                with st.spinner("Refreshing data sources..."):
                    time.sleep(1)
                st.success("All sources refreshed!")

    # ===== TAB 2: Chart Preview =====
    with tab2:
        st.header("Chart Preview")
        st.markdown("Preview charts that will be included in the final report.")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Exposure by Segment")
            portfolio_df = get_portfolio_data()
            fig_bar = px.bar(
                portfolio_df,
                x="Segment",
                y="Exposure",
                color="Segment",
                title="Portfolio Exposure by Segment (M PLN)",
                color_discrete_sequence=px.colors.qualitative.Set2
            )
            fig_bar.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig_bar, use_container_width=True)

        with col2:
            st.subheader("Rating Distribution")
            rating_df = get_rating_data()
            fig_pie = px.pie(
                rating_df,
                values="Exposure",
                names="Rating",
                title="Exposure by Risk Rating",
                color_discrete_sequence=px.colors.qualitative.Pastel
            )
            fig_pie.update_traces(textposition='inside', textinfo='percent+label')
            fig_pie.update_layout(height=400)
            st.plotly_chart(fig_pie, use_container_width=True)

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Monthly Exposure Trend")
            trend_df = get_trend_data()
            fig_line = go.Figure()
            fig_line.add_trace(go.Scatter(
                x=trend_df["Month"],
                y=trend_df["Exposure"],
                mode='lines+markers',
                name='Exposure',
                line=dict(color='#3182ce', width=3),
                marker=dict(size=8)
            ))
            fig_line.update_layout(
                title="Total Portfolio Exposure (M PLN)",
                xaxis_title="Month",
                yaxis_title="Exposure (M PLN)",
                height=350
            )
            st.plotly_chart(fig_line, use_container_width=True)

        with col2:
            st.subheader("NPL Ratio Trend")
            fig_npl = go.Figure()
            fig_npl.add_trace(go.Scatter(
                x=trend_df["Month"],
                y=trend_df["NPL"],
                mode='lines+markers',
                name='NPL Ratio',
                line=dict(color='#e53e3e', width=3),
                marker=dict(size=8),
                fill='tozeroy',
                fillcolor='rgba(229, 62, 62, 0.1)'
            ))
            fig_npl.add_hline(y=4.0, line_dash="dash", line_color="gray",
                            annotation_text="Threshold (4.0%)")
            fig_npl.update_layout(
                title="NPL Ratio (%)",
                xaxis_title="Month",
                yaxis_title="NPL Ratio (%)",
                height=350
            )
            st.plotly_chart(fig_npl, use_container_width=True)

        st.markdown("---")

        st.subheader("Segment Performance Matrix")
        portfolio_df = get_portfolio_data()
        fig_scatter = px.scatter(
            portfolio_df,
            x="NPL_Rate",
            y="Coverage",
            size="Exposure",
            color="Segment",
            title="NPL Rate vs Coverage by Segment",
            labels={"NPL_Rate": "NPL Rate (%)", "Coverage": "Coverage Ratio (%)"},
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        fig_scatter.update_layout(height=400)
        st.plotly_chart(fig_scatter, use_container_width=True)

    # ===== TAB 3: Generate Report =====
    with tab3:
        st.header("Generate Report")

        # Pre-generation checklist
        st.subheader("Pre-Generation Checklist")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Data Sources")
            st.checkbox("All SQL connections verified", value=True, disabled=True)
            st.checkbox("Excel files available", value=True, disabled=True)
            st.checkbox("SharePoint slides downloaded", value=True, disabled=True)
            st.checkbox("Manual adjustments reviewed", value=False, disabled=True)

        with col2:
            st.markdown("#### Report Components")
            st.checkbox("Executive Summary", value=include_charts, disabled=True)
            st.checkbox("Portfolio Analysis", value=include_tables, disabled=True)
            st.checkbox("Risk Indicators", value=True, disabled=True)
            st.checkbox("Appendix & Notes", value=include_appendix, disabled=True)

        st.markdown("---")

        # Generation summary
        st.subheader("Generation Summary")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info(f"**Report Type:** {report_type}")
        with col2:
            st.info(f"**Period:** {report_month}")
        with col3:
            estimated_slides = 45 if report_type == "Full Report" else 15 if report_type == "Executive Summary" else 25
            st.info(f"**Estimated Slides:** {estimated_slides}")

        st.markdown("---")

        # Generate button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("Generate Entity Report", type="primary", use_container_width=True):
                progress_bar = st.progress(0)
                status_text = st.empty()

                steps = [
                    ("Connecting to databases...", 10),
                    ("Loading portfolio data...", 25),
                    ("Processing risk metrics...", 40),
                    ("Generating charts...", 55),
                    ("Building PowerPoint slides...", 70),
                    ("Merging SharePoint content...", 85),
                    ("Finalizing report...", 95),
                    ("Complete!", 100),
                ]

                for step_text, progress in steps:
                    status_text.text(step_text)
                    progress_bar.progress(progress)
                    time.sleep(0.5)

                st.success("Report generated successfully!")
                st.balloons()

                st.markdown("---")
                st.markdown("### Generated Report")
                st.markdown(f"**Filename:** Entity_Report_{report_month.replace(' ', '_')}.pptx")
                st.markdown(f"**Size:** 12.4 MB")
                st.markdown(f"**Slides:** {estimated_slides}")

                st.download_button(
                    label="Download Report",
                    data=b"Mock PowerPoint content",
                    file_name=f"Entity_Report_{report_month.replace(' ', '_')}.pptx",
                    mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
                )


if __name__ == "__main__":
    main()
