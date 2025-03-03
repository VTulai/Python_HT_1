import modules.file_utils as fu
import streamlit as st


todo_items = fu.get_todos()


def add_todo():
    todo = st.session_state["todo"] + '\n'
    if todo not in todo_items:
        todo_items.append(todo)
        fu.write_todos(todo_items)
    st.session_state.todo = ''


st.title("My TODO app")

for index, item in enumerate(todo_items):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todo_items.pop(index)
        fu.write_todos(todo_items)
        del st.session_state[item]
        st.rerun()

st.text_input(key="todo", label='', placeholder="Add new TODO", on_change=add_todo)

st.session_state
