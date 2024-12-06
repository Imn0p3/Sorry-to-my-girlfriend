import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# Third Page
st.title("ยังไม่หมด")

# Navigate to the next page when the button is clicked
if st.button("Next"):
    switch_page("page_4")

if st.button("Back"):
    switch_page("page_2")