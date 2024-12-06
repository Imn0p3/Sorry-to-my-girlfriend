git add requirements.txt
git commit -m "Add streamlit-extras to requirements"
git push

import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.title("I want to say some!")

# Navigate to the next page when the button is clicked
if st.button("Next"):
    switch_page("page_1")





