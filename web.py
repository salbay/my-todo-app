import streamlit as st
import streamlit.errors
import functions

todos = functions.get_todos()
st.set_page_config(layout="wide")

def add_todo():
    todo = st.session_state["chat_input"]
    todos = functions.get_todos()
    new_todo = todo + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)
    st.session_state["chat_input"] = ""


st.title("Benim To-do Uygulamam")
st.subheader("Meslinama..")
st.write("(**Kutucuğu işaretlersen görev silinir.**)")
st.write("This app is to increase your <b>productivity.</b>",unsafe_allow_html=True)

st.text_input(label="",placeholder="Add new todo..",key="chat_input",on_change=add_todo)


for todo in todos:
    try:
        st.checkbox(todo,key=todo)
    except streamlit.errors.DuplicateWidgetID:
        st.warning("Aynı madde..")
    if st.session_state[todo]:
        functions.delete_todos(todo)
        #del st.session_state[todo]
        st.experimental_rerun()

