A simple and elegant command-line News App built with Python 3.12 that fetches the latest headlines using a news API. This project uses the requests module to make API calls and stores sensitive credentials securely using a .env file.

🚀 Features
🔍 Get top headlines based on your query

🌐 Access real-time news via a public News API

🔐 API key stored securely using .env

💡 Clean, beginner-friendly code using requests module

📂 Project Structure
bash
Copy
Edit
news-app/
│
├── app.py # Main Python file
├── .env # Environment variables (API Key)
├── .gitignore # Ignore .env and other unnecessary files
├── requirements.txt # Dependencies
└── README.md # You're here!
🧰 Requirements
Python 3.12+

requests

python-dotenv

🔐 Setup Instructions

1. Clone the Repository
   bash
   Copy
   Edit
   git clone https://github.com/your-username/news-app.git
   cd news-app
2. Create and Activate Virtual Environment (Recommended)
   bash
   Copy
   Edit
   python3.12 -m venv env
   source env/bin/activate # macOS/Linux

# OR

env\Scripts\activate # Windows 3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt 4. Set up .env File
Create a .env file in the root directory:

env
Copy
Edit
API_KEY=your_news_api_key_here
⚠️ Never share your .env or API key publicly.

🧪 How to Run
bash
Copy
Edit
python app.py
Follow the prompt:

sql
Copy
Edit
What news are you interested in today? : Technology
You'll get a clean list of headlines with titles, descriptions, and URLs.

🗂️ Sample Output
markdown
Copy
Edit

1. OpenAI launches ChatGPT-5
   ChatGPT-5 brings advanced reasoning...
   https://news-source.com/article1

---

2. Google introduces new AI tools
   Google unveiled new features at I/O...
   https://news-source.com/article2
   📦 requirements.txt
   nginx
   Copy
   Edit
   requests
   python-dotenv
   You can generate this using:
   pip freeze > requirements.txt
