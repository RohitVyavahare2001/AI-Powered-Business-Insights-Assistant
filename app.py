import streamlit as st
import os
from dotenv import load_dotenv
from backend.ai_engine import BusinessAIEngine
from backend.report_generator import ReportGenerator
from utils.prompt_templates import get_prompt_template

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Business Insights Assistant",
    page_icon="📊",
    layout="wide"
)

# Initialize AI Engine
ai_engine = BusinessAIEngine()
report_generator = ReportGenerator()

def main():
    st.title("AI Business Insights Assistant")
    
    # Sidebar for analysis type selection
    with st.sidebar:
        st.header("Analysis Options")
        analysis_type = st.selectbox(
            "Select Analysis Type",
            ["Competitive Analysis", "Trend Forecasting", "Market Research", "Strategic Planning"]
        )
        
        st.markdown("---")
        st.markdown("""
        ### About
        This AI-powered assistant helps in:
        - Competitive Analysis
        - Trend Forecasting
        - Strategic Decision Making
        - Market Research
        """)

    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Business Query Input")
        user_query = st.text_area(
            "Enter your business question or analysis request",
            height=100,
            placeholder="e.g., Analyze the competitive landscape of the electric vehicle market and identify key opportunities for growth"
        )
        
        additional_context = st.text_area(
            "Additional Context (Optional)",
            height=75,
            placeholder="Add any specific context, industry focus, or constraints..."
        )
        
        if st.button("Generate Insights", type="primary"):
            if user_query:
                with st.spinner("Analyzing your request..."):
                    # Get appropriate prompt template
                    prompt = get_prompt_template(analysis_type)
                    
                    # Generate insights
                    response = ai_engine.generate_insights(
                        query=user_query,
                        analysis_type=analysis_type,
                        additional_context=additional_context,
                        prompt_template=prompt
                    )
                    
                    # Display results
                    st.markdown("### Analysis Results")
                    st.markdown(response['summary'])
                    
                    # Display structured insights
                    with st.expander("Detailed Insights", expanded=True):
                        st.markdown(response['detailed_analysis'])
                    
                    # Generate and offer report download
                    report = report_generator.create_report(
                        analysis_type=analysis_type,
                        query=user_query,
                        insights=response
                    )
                    
                    st.download_button(
                        label="Download Report",
                        data=report,
                        file_name=f"business_insights_{analysis_type.lower().replace(' ', '_')}.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
            else:
                st.warning("Please enter a business query to analyze.")

    with col2:
        st.subheader("Quick Tips")
        st.info("""
        **For best results:**
        - Be specific about your industry
        - Include relevant timeframes
        - Specify geographic focus
        - Mention target market segments
        """)
        
        st.subheader("Analysis Metrics")
        st.metric(label="Business Relevance Score", value="92%")
        st.metric(label="Response Consistency", value="88%")
        st.metric(label="User Satisfaction", value="4.5/5")

if __name__ == "__main__":
    main() 