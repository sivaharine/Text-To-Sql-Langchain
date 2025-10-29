from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)

template = """
You are an expert AI that converts natural language into SQL queries.
Use the given database schema to generate a valid SQL query.

Database schema:
college_students(id, name, age, gender, city, marks, attendance, teacher, course)

User question: {question}

Return ONLY the SQL query without any explanation, markdown formatting, or extra text.
"""

prompt = PromptTemplate(input_variables=["question"], template=template)

parser = StrOutputParser()
chain = prompt | llm | parser

engine = create_engine("sqlite:///college.db")

def run_text_to_sql(user_question: str):
    sql_query = chain.invoke({"question": user_question}).strip()
    print(f"\nGenerated SQL:\n{sql_query}\n")

    with engine.connect() as conn:
        try:
            result = conn.execute(text(sql_query))
            rows = result.fetchall()
            print("Query Results:")
            for row in rows:
                print(row)
        except Exception as e:
            print("Error executing SQL:", e)

if __name__ == "__main__":
    while True:
      user_input = input("Enter your question: ")
      if  user_input=="exit":
          break
      run_text_to_sql(user_input)
