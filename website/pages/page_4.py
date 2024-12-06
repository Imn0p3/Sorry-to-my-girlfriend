import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# Fourd Page
st.title("💐💐💐💐💐💐💐💐")

# Navigate to the next page when the button is clicked
if st.button("Next"):
    switch_page("page_5")

if st.button("Back"):
    switch_page("page_3")