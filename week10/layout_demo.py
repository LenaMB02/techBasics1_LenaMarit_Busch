import streamlit as st

# For more references on Layout, check: https://docs.streamlit.io/develop/api-reference/layout

st.title("Layout Demo")


st.subheader("Container")
# Simple Container
container = st.container(border=True,
                         height=200) # change border=False to hide the border
with container:
    st.write("HI! I am in the container")

st.write("THIS IS NOT IN THE CONTAINER")
st.write("---")

# Using Container for simple layout
container2 = st.container(border=False, horizontal=True, horizontal_alignment="center", vertical_alignment="bottom", gap="medium")
with container2:
    st.write("item1")
    st.write("item2")
    st.write("item3")
st.write("---")
# Columns
st.subheader("Columns")

col1, col2, col3 = st.columns(3, gap="medium") # default gap:small
col1.image("https://static.streamlit.io/examples/cat.jpg")
col2.image("https://static.streamlit.io/examples/dog.jpg")
col3.image("https://static.streamlit.io/examples/owl.jpg")
st.write("---")

# Grid
st.subheader("Grid")
row1 = st.columns(2)
row2 = st.columns(3)

# we can create tiles and place a balloon in it
for col in row1 + row2:
    tile = col.container(height=120)
    tile.title(":balloon:")
st.write("---")

# Tabs
st.subheader("Tabs")
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

# Sidebar
with st.sidebar:
    st.write("Everything inside this with block is inside the sidebar")

# Footer
with st.bottom:
    st.caption("Tech Basics I, 2026SS")