🏷️ Project Title: Text2SQL Assistant – Natural Language to SQL Query Generator
📖 Description:

Text2SQL Assistant is an AI-powered tool that converts natural language questions into executable SQL queries using LangChain and Google Gemini 2.5 Flash.
The model understands the user’s intent, generates the corresponding SQL query based on the provided database schema, and executes it directly on a SQLite database.
This project demonstrates the practical use of LLM-based query generation, LangChain prompt chaining, and SQLAlchemy for real-time database interaction — making it ideal for intelligent database assistants or query automation tools.

⚙️ Features:

🧠 Converts natural language to SQL using Gemini LLM

🧩 Uses LangChain PromptTemplate and OutputParser for structured query generation

💾 Connects seamlessly to SQLite via SQLAlchemy

⚡ Real-time query execution and result display

🔐 Environment variable management with .env

🚀 How to Run:
1️⃣ Clone the repository
git clone https://github.com/your-username/text2sql-assistant.git
cd text2sql-assistant

2️⃣ Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate     # for Windows
# OR
source venv/bin/activate  # for macOS/Linux

3️⃣ Install dependencies
pip install -r requirements.txt


(Your requirements.txt should include: langchain, langchain-google-genai, sqlalchemy, python-dotenv)

4️⃣ Set up .env file

Create a .env file and add your Gemini API key:

GOOGLE_API_KEY=your_api_key_here

5️⃣ Run the application
python text2sql_app.py

6️⃣ Ask natural language queries

Example inputs:

Enter your question: Show all students with marks above 80
Enter your question: List names and cities of students taught by 'Mr. Ravi'


Type exit to quit the program.

🏁 Outcome:

Built an intelligent LLM-powered Text2SQL system that translates natural language queries into executable SQL, bridging the gap between users and databases.
