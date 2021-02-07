import streamlit as st
from PIL import Image

st.title("Hello World")
img = Image.open("img.jpg")
st.image(img,caption="Sravi", use_column_width=True)
