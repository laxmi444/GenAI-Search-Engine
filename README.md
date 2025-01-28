# AI Search Engine with LangChain and Groq

A powerful search engine that combines multiple data sources (DuckDuckGo, arXiv, and Wikipedia) with Groq's LLM capabilities to provide comprehensive and intelligent search results. Built using Streamlit for a clean, interactive web interface.

## Features

- Multi-source search integration:
  - DuckDuckGo web search
  - arXiv academic papers
  - Wikipedia articles
- Streaming responses with real-time display of AI thoughts and actions
- Interactive chat interface
- Secure API key handling
- Session state management for conversation history

## Prerequisites

- Python 3.8+
- Groq API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/laxmi444/GenAI-Search-Engine.git
cd GenAI-Search-Engine/SearchEngineGENAI
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your Groq API key:
```bash
GROQ_API_KEY=your_api_key_here
```

## Usage

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Enter your Groq API key in the sidebar
3. Start chatting with the AI search engine

## How It Works

The application uses LangChain's agent framework to:
1. Process user queries
2. Search across multiple sources (DuckDuckGo, arXiv, Wikipedia)
3. Generate comprehensive responses using Groq's LLM
4. Display results in a conversational format

## Component Overview

- `ChatGroq`: Handles communication with Groq's LLM
- `ArxivAPIWrapper`: Interfaces with arXiv for academic paper searches
- `WikipediaAPIWrapper`: Manages Wikipedia queries
- `DuckDuckGoSearchRun`: Performs web searches
- `StreamlitCallbackHandler`: Manages UI updates and streaming responses

## Configuration

The following parameters can be adjusted:
- `top_k_results`: Number of results to fetch from each source (default: 1)
- `doc_content_chars_max`: Maximum character length for document content (default: 250)
- `model_name`: Currently using "llama3-8b-8192"

## Security Notes

- API keys are handled securely through environment variables and password-protected input
- Session state ensures conversation persistence
- Error handling is implemented for API failures and parsing errors

