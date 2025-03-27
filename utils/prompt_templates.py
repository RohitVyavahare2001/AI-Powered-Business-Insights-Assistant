def get_prompt_template(analysis_type: str) -> str:
    """
    Get the appropriate prompt template based on the analysis type.
    
    Args:
        analysis_type (str): The type of analysis requested
        
    Returns:
        str: The prompt template for the specified analysis type
    """
    templates = {
        "Competitive Analysis": """
        Please conduct a thorough competitive analysis that includes:
        1. Industry Overview
        2. Key Competitors Analysis
           - Market share
           - Strengths and weaknesses
           - Unique value propositions
        3. Competitive Advantages and Disadvantages
        4. Market Positioning
        5. Strategic Recommendations
        
        Focus on actionable insights and data-driven conclusions.
        """,
        
        "Trend Forecasting": """
        Please provide a comprehensive trend forecast that covers:
        1. Current Market Trends
        2. Emerging Technologies and Innovations
        3. Consumer Behavior Shifts
        4. Market Growth Projections
        5. Industry Disruption Potential
        6. Future Scenarios and Their Implications
        
        Base predictions on current data and historical patterns where applicable.
        """,
        
        "Market Research": """
        Please conduct detailed market research that includes:
        1. Market Size and Growth Potential
        2. Target Customer Segments
        3. Market Drivers and Restraints
        4. Distribution Channels
        5. Pricing Analysis
        6. Market Entry Barriers
        7. Regulatory Environment
        
        Provide specific, actionable insights for business decision-making.
        """,
        
        "Strategic Planning": """
        Please develop a strategic plan that addresses:
        1. Current Position Analysis
        2. Strategic Objectives
        3. Resource Requirements
        4. Implementation Timeline
        5. Success Metrics
        6. Risk Assessment
        7. Contingency Plans
        
        Focus on practical, achievable recommendations with clear implementation steps.
        """
    }
    
    return templates.get(analysis_type, """
    Please provide a comprehensive business analysis that includes:
    1. Situation Overview
    2. Key Findings
    3. Recommendations
    4. Implementation Steps
    5. Risk Assessment
    
    Focus on providing actionable insights and clear recommendations.
    """) 