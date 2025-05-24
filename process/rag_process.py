
import re
import pandas as pd
from process.prompt_process import prompt
from sqlalchemy import create_engine
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain_google_genai import ChatGoogleGenerativeAI


def clean_sql(sql_code):
    clean_sql_code = re.sub(r"```(?:sqlite|sql)?\n(.*?)\n```", r"\1", sql_code, flags=re.DOTALL).strip()
    return clean_sql_code


class Text2SQL():
    def __init__(self, model_info, question="Get all row?"):
        self.model = {"Gemini": lambda: ChatGoogleGenerativeAI(model=model_info["model_name"], google_api_key=model_info["api_key"]), "GPT": lambda: ChatOpenAI(model=model_info["model_name"], api_key=model_info["api_key"])}[model_info["model_type"]]
        self.question = question

    def init_db(self, data_files):
        self.engine = create_engine("sqlite:///:memory:")

        for data_file in data_files:
            table_name, extension = data_file.name.split(".")

            if extension == "csv":
                df = pd.read_csv(data_file)
            else:
                df = pd.read_excel(data_file)

            df.to_sql(table_name, self.engine, if_exists="replace", index=False)

        db = SQLDatabase(self.engine)
        return self.get_answer(db.get_table_info())

    def get_answer(self, data_info):
        chain = prompt | self.model()
        response = chain.invoke({"table_info": data_info, "query": self.question})

        return clean_sql(response.content)

    def run_query(self, query):
        with self.engine.connect() as conn:
            get_data = pd.read_sql(query, conn)

        return get_data
