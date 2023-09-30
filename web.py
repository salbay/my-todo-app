import streamlit as st
import streamlit.errors
import functions

def add_todo():
    todo = st.session_state["chat_input"]
    todos = functions.get_todos()
    new_todo = todo + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)
    print(todo)


st.title("Benim To-do Uygulamam")
st.subheader("Meslinacığıma..")
st.write("(**Kutucuğu işaretlersen görev silinir.**)")
st.write("This app is to increase your productivity.")

todos = functions.get_todos()
for todo in st.session_state:
    if st.session_state[todo]:
        functions.delete_todos(todo)
        #del st.session_state[todo]
        st.experimental_rerun()


st.chat_input("Your New Todo..",key="chat_input",on_submit=add_todo)

for todo in todos:
    try:
        st.checkbox(todo,key=todo)
    except streamlit.errors.DuplicateWidgetID:
        st.warning("Aynı madde..")

#st.session_state

#st.balloons()
#st.text_input("",placeholder="Your New Todo",key="text_input",on_change=add_todo)


