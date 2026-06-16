import streamlit as st

if 'todo_list' not in st.session_state:
    st.session_state.todo_list = ["Grocery Shopping","Breakfast","Tech Basics 1"]

def update_todo():
    if user_input != "":
        st.session_state.todo_list.append(user_input)

st.set_page_config(
    page_title="To-do List",
    page_icon="🌙")
st.title("To-do List")
st.write("---")

container = st.container(border=False, gap="medium", horizontal=True, vertical_alignment="bottom")
with container:
    user_input = st.text_input(label="Add something to your to-do list!")
    st.button("+ Add to List", on_click=update_todo)

for i in range(len(st.session_state.todo_list)):
    st.checkbox(st.session_state.todo_list[i], key=i)
