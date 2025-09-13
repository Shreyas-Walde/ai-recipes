# AI Recipes

A collection of practical AI applications and tools built with Python.

## Projects

- **Resume Critiquer**: AI-powered resume analysis and feedback tool using Gemini API
- **Image Classifier**: Computer vision application for identifying objects in images using MobileNetV2
- **AI Agents**: Framework for building LangChain-based AI agents (in development)

## Setup

```bash
# Clone the repository
git clone https://github.com/Shreyas-Walde/applied-ai-examples.git
cd applied-ai-examples

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up API keys
# Create a .env file with your API keys
# GOOGLE_API_KEY=your_api_key_here
```

## Usage

Each project can be run independently:

```bash
# Resume Critiquer
cd resume-critiquer
streamlit run resume.py

# Image Classifier
cd image_classifer
streamlit run img_cls.py
```

## Requirements

- Python 3.12+
- See requirements.txt for package dependencies