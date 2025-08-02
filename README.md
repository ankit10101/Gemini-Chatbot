# Gemini-powered Chatbot 🤖

## Introduction

This project implements an intelligent chatbot using Google's cutting-edge Gemini 1.5 Flash model. Built with Streamlit, this web application provides an intuitive interface for users to engage in dynamic conversations with an AI-powered assistant. The chatbot leverages the advanced natural language processing capabilities of the Gemini model to generate contextually relevant and insightful responses.

## Demo

[Chatbot_Demo.webm](https://github.com/ankit10101/LLM_Chatbot/assets/40112826/1f33dd3a-5596-4a84-ba25-e0e087c12932)

## Key Features

- **Interactive Chat Interface**: A user-friendly, web-based chat interface built with Streamlit.
- **Gemini 1.5 Flash Integration**: Utilizes Google's state-of-the-art language model for generating responses.
- **Session-based Chat History**: Maintains conversation context within each user session.
- **Real-time Response Generation**: Quickly generates and displays AI responses.
- **Environment Variable Support**: Securely manages API keys using environment variables.
- **Wide-layout Design**: Optimized for a better viewing experience on larger screens.

## Technical Prerequisites

- Python 3.6 or higher
- A Google API key with access to the Gemini 1.5 Flash model
- Basic understanding of Python and web applications

## Detailed Installation Guide

1. **Clone the Repository**
   ```
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Set Up a Virtual Environment** (Optional but recommended)
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Create a file named `.env` in the project root directory and add your Google API key:
   ```
   GOOGLE_API_KEY=your_actual_api_key_here
   ```
   Ensure this file is listed in your `.gitignore` to prevent accidental exposure of your API key.

## In-depth Usage Guide

1. **Start the Streamlit Application**
   ```
   streamlit run app.py
   ```

2. **Access the Web Interface**
   Open your web browser and navigate to the URL provided in the terminal (typically `http://localhost:8501`).

3. **Interact with the Chatbot**
   - Type your message or question in the input field at the bottom of the page.
   - Press Enter or click the send button to submit your message.
   - The AI will generate and display its response in the chat interface.
   - Your conversation history will be maintained throughout the session.

## Detailed Project Structure

- `app.py`: The core application file containing:
  - Streamlit UI setup and configuration
  - Integration with the Gemini model
  - Chat history management
  - User input processing and response generation logic
- `requirements.txt`: Comprehensive list of Python package dependencies
- `.env`: Configuration file for environment variables (not included in the repository)

## Dependencies Explained

- `streamlit`: Powers the web-based user interface and handles the application's front-end.
- `google-generativeai`: Google's official Python client library for accessing Generative AI models like Gemini.
- `python-dotenv`: Facilitates the loading of environment variables from the `.env` file.

## Advanced Configuration

The application uses Streamlit's `set_page_config` to optimize the layout:
- `initial_sidebar_state='expanded'`: Ensures the sidebar is visible by default.
- `layout="wide"`: Utilizes a wide layout for better space utilization on larger screens.

## Security Considerations

- **API Key Protection**: Always store your Google API key in the `.env` file and never commit this file to version control.
- **Rate Limiting**: Be aware of any rate limits imposed by the Gemini API and implement appropriate handling if necessary.

## Potential Enhancements

1. **User Authentication**: Implement user accounts to provide personalized experiences.
2. **Conversation Persistence**: Add database integration to store chat histories beyond the current session.
3. **Multi-model Support**: Extend the application to switch between different AI models.
4. **Custom Styling**: Enhance the UI with custom CSS for a unique look and feel.
5. **Error Handling**: Implement robust error handling for API failures or rate limit exceedances.
