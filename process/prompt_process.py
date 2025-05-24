from langchain_core.prompts import ChatPromptTemplate

template = """
You are a SQL query generator\n
Given a database schema and a natural language question, generate only the corresponding SQL statement—nothing else.\n
If the question cannot be converted into a valid SQL query or is unrelated to the provided schema, respond with exactly: "I don't know".\n\n

Table Info: {table_info}\n\n
User question: {query}\n\n
Output (SQL only):
"""
prompt = ChatPromptTemplate.from_template(template)
