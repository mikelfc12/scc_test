import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit Deployment Test")

st.write("If you can see this, your GitHub → Streamlit Cloud connection works!")

# simple slider
number = st.slider("Pick a number", 0, 100, 25)

st.write("You selected:", number)

# generate dummy data
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

st.line_chart(data)

# button
if st.button("Click me"):
    st.success("Button works! 🎉")
