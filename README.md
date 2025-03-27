# AI-Powered Business Insights Assistant

A sophisticated AI-powered business analysis tool that leverages Groq's LLM capabilities to provide strategic insights and recommendations for business decision-making.

## Demo
https://youtu.be/NbM4aQAieJQ

## Features

- **Competitive Analysis**: Detailed analysis of market competitors, strengths, weaknesses, and strategic positioning
- **Trend Forecasting**: AI-driven predictions of market trends and industry developments
- **Market Research**: Comprehensive market analysis with actionable insights
- **Strategic Planning**: Data-driven strategic recommendations and implementation plans
- **Report Generation**: Automated generation of professional business reports in DOCX format

## Installation

1. Clone the repository:
```bash
git clone https://github.com/RohitVyavahare2001/AI-Powered-Business-Insights-Assistant
cd ai-business-insights
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the root directory with your Groq API key:
```
GROQ_API_KEY=your_api_key_here
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided URL (typically http://localhost:8501)

3. Select the type of analysis you want to perform from the sidebar

4. Enter your business query and any additional context

5. Click "Generate Insights" to receive AI-powered analysis

6. Download the generated report in DOCX format

## Project Structure

```
.
├── app.py                 # Main Streamlit application
├── backend/
│   ├── ai_engine.py      # AI processing logic using Groq
│   └── report_generator.py # Report generation functionality
├── utils/
│   └── prompt_templates.py # Analysis-specific prompt templates
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```

## Dependencies

- Python 3.8+
- Streamlit
- Groq API
- python-docx
- python-dotenv
- Other dependencies listed in requirements.txt


