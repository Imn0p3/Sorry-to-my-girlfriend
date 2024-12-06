import streamlit as st
from streamlit_extras.switch_page_button import switch_page


#vid
video_url = "https://youtu.be/T_8IwhXD-8s"
st.video(video_url)

# Fourd Page
st.title("How are you feel✨")

score = st.slider("Slide your mood", 0, 10)

def score_evaluation(score):
    if 1 <= score <= 3:
        st.write("ดีกันน้าา🙇‍♂️")
    elif 4 <= score <= 6:
        st.write("ขอกอดคนสวยหน่อยน้าา🫂")
    elif 7 <= score <= 8:
        st.write("ขอจุ้บคนเก่งง😽")
    else:
        st.write("ขอบคุณที่ยังอยู่กับเค้านะคะ✨")

# Call the function with the current score
score_evaluation(score)

# Navigate to the next page when the button is clicked

if st.button("Back"):
    switch_page("page_5")