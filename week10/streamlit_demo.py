# import the streamlit library
import streamlit as st

# Streamlit Variable
if 'click_count' not in st.session_state:
    st.session_state.click_count = 0 # start value

# You can define functions as usual
def update_count():
    st.session_state.click_count += 1

# Browser Tab Display
st.set_page_config(
    page_title="Streamlit Demo",
    page_icon="🌙")

# Title of your streamlit app
st.title("Streamlit Demo")

# Add a dash
st.write("---")
# Display some text
st.write("HELLO WORLD!:laughing:")

# Add a header
st.header("THIS IS A HEADER")
# Add a subheader
st.subheader("This is a subheader")

# Useful Widgets
# User Input
newItem = st.text_input("Username:", "user", key="user_name") # key sets user name
# fstring works as well!
st.write(f"Hi {st.session_state.user_name}!")

# numerical input
num = st.number_input(label="Enter a number:",
                       step=1,
                       value=0)
st.write(f"Number entered: {num}!")

# Button
st.button("Button", on_click=update_count, help="Try to click!")
st.write(f"Button click count: {st.session_state.click_count}!")

# Badges

st.badge("ToDo")
st.badge("Done", icon=":material/check:", color="green")
# Badges side by side
st.markdown(
    ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Urgent] :gray-badge[Done]"
)

# Selection
option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Message", "Phone Call"),
)
st.write("You selected:", option)

# Radio Buttons
options = ["Email", "Message", "Phone Call"]
operator = st.radio("How would you like to be contacted?", options)

# Checkbox
opt1 = st.checkbox("Option 1")
st.write(f"Checkbox returns: {opt1}!")

# Slider
rating = st.slider("RATE HOW MUCH YOU LOVE PYTHON",
          min_value=1,
          max_value=5,
          # this is what the user sees when the app launches
          value=3)
st.write(f"Python Rating: {rating}!")

# Fancier slider
rating2 = st.select_slider("Rate how much you love Python",
          ["🤮", "😭", "😑", "😊", "😍"],
         value="😍")