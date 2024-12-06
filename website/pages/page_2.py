import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# Third Page
st.title("ให้ดอกไม้ทั้งสวนเลยย 🌼🌼🌼🌼🌼")

# Navigate to the next page when the button is clicked
if st.button("Next"):
    switch_page("page_3")

if st.button("Back"):
    switch_page("page_1")