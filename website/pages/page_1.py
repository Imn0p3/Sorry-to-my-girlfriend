import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# Second Page
st.title("เค้าขอโทษน้าา ที่หายไปทั้งวันเลย🙇‍♂️")

# Navigate to the next page when the button is clicked
if st.button("Next"):
    switch_page("page_2")

if st.button("Back"):
    switch_page("srry_home")