# Personal AI Assistant

A Streamlit-based AI assistant that can handle various types of queries including travel, events, news, and sports information.

## Features

- 🤖 Smart intent detection using AWS Bedrock
- 🌍 Travel information and recommendations
- 🎫 Local events discovery
- 📰 Latest news updates
- 🏅 Sports updates and scores
- 💬 User-friendly chat interface with category buttons

## Prerequisites

- Python 3.10 or higher
- AWS Bedrock access (for intent detection)
- API endpoints for various services (travel, events, news, sports)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd PersonalAIPrototype
```

2. Create and activate a virtual environment:
```bash
python3.10 -m venv personalAI
source personalAI/bin/activate
```

3. Install the package in editable mode:
```bash
pip install -e .
```

## Configuration

1. Set up AWS credentials for Bedrock:
   - Create or use an existing AWS profile named "ogokmen_bedrock"
   - Ensure the profile has access to AWS Bedrock services

2. Configure API endpoints in `src/constants.py`:
   - TRAVEL_API_URL
   - EVENTS_API_URL
   - NEWS_API_URL
   - SPORTS_API_URL

## Usage

1. Start the Streamlit app:
```bash
streamlit run src/app.py
```

2. Open your browser and navigate to:
   - Local URL: http://localhost:8501
   - Network URL: http://<your-ip>:8501

3. Use the interface:
   - Type your question in the text input
   - Or click one of the category buttons (Travel, Events, News, Sports)
   - The AI will detect the intent and route your query to the appropriate service

## Project Structure

```
PersonalAIPrototype/
├── src/
│   ├── __init__.py
│   ├── app.py              # Main Streamlit application
│   ├── intent.py           # Intent detection using AWS Bedrock
│   ├── constants.py        # API endpoints and configuration
│   └── routers/
│       ├── __init__.py
│       ├── travel_proxy.py
│       ├── events_proxy.py
│       ├── news_proxy.py
│       └── sports_proxy.py
├── personalAI/            # Virtual environment
├── setup.py              # Package configuration
└── requirements.txt      # Project dependencies
```

## Dependencies

- streamlit>=1.32.0
- python-dotenv>=1.0.0
- requests>=2.31.0
- boto3>=1.34.0
- botocore>=1.34.0

## Development

The project is set up in editable mode, which means:
- Changes to source code are reflected immediately
- No need to reinstall the package after modifications
- Easy to test and debug

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Add your license information here]