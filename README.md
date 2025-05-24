# Text2SQL-AI

Text2SQL-AI is an AI-powered application that allows you to generate SQL queries from natural language input, supported by powerful language models. Whether you upload a data file or simply provide a table schema, your text is converted into SQL queries, and the results are presented in a tabular format.

---

## 📸 Screenshots

* #### "Describe Data with Text" Tab
![Text2SQL-AI](https://github.com/user-attachments/assets/c33a5d56-b3c3-4adc-96d6-082d15079429)
---
* #### "Describe Data with Excel" Tab (P1)
![Text2SQL-AI](https://github.com/user-attachments/assets/bab94352-1fcf-4bc9-bc74-5cd9ae2612e2)
---
* #### "Describe Data with Excel" Tab (P2)
![Text2SQL-AI](https://github.com/user-attachments/assets/000c5681-0cf2-4ec5-b5cb-7f7f84be0951)


## 🖥️ Demo

🔗 [Text2SQL-AI](https://text2sql-ai-demo.streamlit.app)

---

## 🚀 Features

* **Text → SQL**: Converts natural language questions into SQL queries.
* **CSV/XLSX Support**: Upload your own data files and generate custom queries.
* **Query Without Sharing Full Data**: If you prefer not to share full data, you can provide just the table schema and a few sample rows.
* **Markdown-Formatted Results**: SQL queries and their outputs are displayed in markdown format, making them easy to copy and share.
* **Preview Table (for SELECT queries)**: SELECT-type queries return a visual table preview of the results.
* **Gemini & GPT Support**: Powered by Gemini or GPT-based models to ensure high-accuracy query generation.

---

## 🔧 Installation & Run

```bash
git clone https://github.com/furkankarakuz/Text2SQL-AI.git
cd Text2SQL-AI
pip install -r requirements.txt
streamlit run app/main.py
```

---

## 📄 License

This project is licensed under the Apache License 2.0
