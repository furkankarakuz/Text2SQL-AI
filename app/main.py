import os
import sys
import streamlit as st
from utils import init_session_state, widget_control
from components.sidebar import sidebar_block

process_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

if process_dir not in sys.path:
    sys.path.append(process_dir)

from process.rag_process import Text2SQL


st.set_page_config(page_title="Text2SQL-AI", page_icon="app/images/icon.png")

st.image("app/images/banner.png", use_container_width=True)
st.divider()

init_session_state()


with st.sidebar:
    model_info = sidebar_block()

text_tab, excel_tab = st.tabs(["Describe Data with Text", "Describe Data with Excel"])


with text_tab:
    st.subheader("Data & Question :books: :thought_balloon:")
    st.html("<br>")

    data_info = st.text_area("Describe Your Data", key="text_tab_info")
    question_text = st.text_area("Write Your Question", key="text_tab_question")
    ask_button = st.button("Ask", key="text_tab_button")

    if ask_button:
        if (message := widget_control("control_type")):
            st.toast(message, icon="⚠️")
        else:
            text2sql = Text2SQL(model_info, question_text)
            query = text2sql.get_answer(data_info)

            st.html("<br>")

            if "don't" in query:
                st.markdown(f"\n{query}\n")
            else:
                st.subheader("SQL Code :pencil:")
                st.markdown(f"```sql\n{query}\n```")


with excel_tab:
    st.subheader("Data & Question :books: :thought_balloon:")
    st.html("<br>")

    files = st.file_uploader("Uploda File(s)", type=["csv", "xlsx"], accept_multiple_files=True)
    st.session_state["excel_tab_files"] = files

    question_text = st.text_area("Write Your Question", key="excel_tab_question")
    ask_button = st.button("Ask", key="excel_tab_button")

    if ask_button:
        if (message := widget_control("excel_tab_control")):
            st.toast(message, icon="⚠️")
        else:
            text2sql = Text2SQL(model_info, question_text)
            query = text2sql.init_db(files)
            st.html("<br>")

            if "don't" in query:
                st.markdown(query)
            else:
                st.subheader("SQL Code :pencil:")
                st.markdown(f"```sql\n{query}\n```")

                if query.lower().startswith("select"):
                    st.html("<br>")
                    st.subheader("Preview :mag:")
                    st.write(text2sql.run_query(query))
