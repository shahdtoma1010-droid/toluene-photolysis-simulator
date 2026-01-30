import streamlit as st

st.set_page_config(
    page_title="Physics Graduation Project 2026",
    layout="wide"
)

st.title("Physics Graduation Project 2026")
st.subheader("Faculty of Science – Physics Department")

st.markdown("""
### Simulation of UV254-Induced Toluene Photolysis

**Student:** Shahd Toma  
**Degree:** B.Sc. in Physics  
**Academic Year:** 2025–2026

---
""")

st.components.v1.iframe(
    "https://shahdtoma1010-droid.github.io/photolysis-sim/",
    height=900,
    scrolling=True
)
