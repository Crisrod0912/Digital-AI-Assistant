# 🤖 Intelligent Productivity Assistant

This project consists of the design and implementation of a digital assistant based on an existing AI, capable of analyzing textual information from the user and offering personalized suggestions to improve their productivity.

## 🚀 Features

- 🔌 Integration with an existing artificial intelligence API.
- 💬 Web-based interaction interface (chat).
- 📦 Functions for AI to process user input such as to-do lists, goals, or emails.
- 🧠 Natural language responses including summaries, reminders, and action plans.

## 🧰 Technologies Used

- 🎨 **Frontend**: HTML, CSS, JavaScript
- 🐍 **Backend**: Python
- 🤖 **AI Model**: OpenAI (gpt-4o-mini)

## 🛠️ Installation

### 📋 Prerequisites

Make sure you have the following tools installed:

- 🐍 [Python](https://www.python.org/) (recommended: Python 3.10 or higher)
- 💻 [Visual Studio Code](https://code.visualstudio.com/)
- 🤖 OpenAI API access (API Key required)

### 🔧 Setup

Follow these steps to correctly configure and run the project:

1. 📥 **Clone the repository**

   ```bash
   git clone https://github.com/Halcyon09/Digital-AI-Assistant.git
   ```

2. 📂 **Open the project folder in VS Code**

   ```bash
   cd Digital-AI-Assistant
   ```

3. 🧪 **Create a virtual environment**

   ```bash
   python -m venv .venv
   ```

4. ▶️ **Activate the virtual environment (Windows PowerShell)**

   ```bash
   .\.venv\Scripts\activate
   ```

5. 📦 **Install required dependencies**

   ```bash
   pip install fastapi uvicorn python-dotenv openai
   ```

6. ⚙️ **Configure environment variables**

   Create a `.env` file in the root directory and add your OpenAI API key:

   ```env
   OPENAI_API_KEY=your_api_key_here
   ```

7. 🚀 **Run the backend server**

   ```bash
   python -m uvicorn app.main:app
   ```

8. 🌐 **Access the frontend**

   Open the `index.html` file located in the frontend folder using your web browser.
