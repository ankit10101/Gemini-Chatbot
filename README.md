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

---

## Run with Docker 🐳

### 1. **Build the Docker Image**
```bash
docker build -t gemini-chatbot .
```

### 2. **Run the Container**
Pass your Google API key as an environment variable:
```bash
docker run -p 8501:8501 -e GOOGLE_API_KEY=your_actual_api_key_here gemini-chatbot
```

### 3. **Open in Browser**
Visit [http://localhost:8501](http://localhost:8501) to access the chatbot interface.

---

## Technical Prerequisites (Non-Docker Usage)

- Python 3.6 or higher
- A Google API key with access to the Gemini 1.5 Flash model
- Basic understanding of Python and web applications

---

## Local Installation Guide (Optional)

If you prefer not to use Docker:

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Create a `.env` file and add your key:
   ```env
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

5. **Run the Application**
   ```bash
   streamlit run app.py
   ```

---

## Project Structure

- `app.py`: Core Streamlit app logic
- `requirements.txt`: Python dependencies
- `.env`: Environment variable config (excluded from version control)

---

## Dependencies

- `streamlit`: Front-end framework
- `google-generativeai`: Gemini API integration
- `python-dotenv`: Loads environment variables

---

## Advanced Configuration

The app uses `streamlit.set_page_config` to improve layout:
- `initial_sidebar_state='expanded'`
- `layout='wide'`

---

## Security Notes

- **API Key Protection**: Always pass API keys via environment variables or `.env` (never hard-code them).
- **Rate Limits**: Monitor Gemini API limits and implement retry or fallback logic as needed.

---

## Future Enhancements

- User authentication
- Persistent chat history (e.g., using SQLite or Firebase)
- Multi-model selection
- Theming & custom CSS
- Comprehensive error handling
