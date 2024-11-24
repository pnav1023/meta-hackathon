import streamlit as st
from assess_image import assess_image

uploaded_file = st.file_uploader("Choose an image...", type=["heic", "jpg", "jpeg", "png"])
if uploaded_file is not None:
    # st.image(uploaded_file, caption='Uploaded Image.')
    if st.button('Assess Image'):
        st.write(assess_image(uploaded_file))
        



