import streamlit as st
from PIL import Image

st.title("Sravi I Love You")
img = Image.open("img.jpg")
st.image(img,caption="Sravi", use_column_width=True)