import os
import groq
from typing import Dict, Any
import json

class BusinessAIEngine:
    def __init__(self):
        self.client = groq.Groq(api_key=os.getenv('GROQ_API_KEY'))
        self.model = "llama3-70b-8192"
    
    def generate_insights(self, query: str, analysis_type: str, additional_context: str = "", prompt_template: str = "") -> Dict[str, Any]:
        """
        Generate business insights using the Groq API.
        
        Args:
            query (str): The user's business query
            analysis_type (str): Type of analysis requested
            additional_context (str): Any additional context provided
            prompt_template (str): The template to structure the response
        
        Returns:
            Dict[str, Any]: Structured response containing summary and detailed analysis
        """
        # Construct the full prompt
        full_prompt = f"""You are an expert business analyst and strategic advisor. 
        Analysis Type: {analysis_type}
        Business Query: {query}
        Additional Context: {additional_context}

        {prompt_template}

        Please provide a comprehensive analysis that includes:
        1. Executive Summary
        2. Detailed Analysis
        3. Key Insights and Recommendations
        4. Action Items
        5. Potential Risks and Mitigation Strategies

        Format the response in a clear, professional structure using markdown formatting.
        """

        try:
            # Generate completion using Groq
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a professional business analyst providing strategic insights."},
                    {"role": "user", "content": full_prompt}
                ],
                temperature=0.7,
                max_tokens=4000
            )

            # Extract and structure the response
            response_text = completion.choices[0].message.content
            
            # Split the response into summary and detailed analysis
            sections = self._parse_response(response_text)
            
            return {
                "summary": sections.get("Executive Summary", ""),
                "detailed_analysis": response_text,
                "key_insights": sections.get("Key Insights and Recommendations", ""),
                "action_items": sections.get("Action Items", ""),
                "risks": sections.get("Potential Risks and Mitigation Strategies", "")
            }

        except Exception as e:
            return {
                "summary": f"Error generating insights: {str(e)}",
                "detailed_analysis": "An error occurred while processing your request.",
                "key_insights": "",
                "action_items": "",
                "risks": ""
            }

    def _parse_response(self, response_text: str) -> Dict[str, str]:
        """
        Parse the response text into sections.
        
        Args:
            response_text (str): The full response text
            
        Returns:
            Dict[str, str]: Dictionary containing different sections of the response
        """
        sections = {}
        current_section = ""
        current_content = []

        for line in response_text.split('\n'):
            if line.strip().startswith('#') or any(section in line for section in ["Executive Summary", "Detailed Analysis", "Key Insights", "Action Items", "Potential Risks"]):
                if current_section and current_content:
                    sections[current_section] = '\n'.join(current_content)
                current_section = line.strip('# ').split(':')[0]
                current_content = []
            else:
                current_content.append(line)

        if current_section and current_content:
            sections[current_section] = '\n'.join(current_content)

        return sections 