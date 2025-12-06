from streamlit import streamlit as st
import pandas as pd
import numpy as np

st.title("Learning streamlit ")
st.write("This is simple paragraph")


dataFrame = pd.DataFrame(
    {"f_col": [1, 2, 3, 4], "l_col": ["sujan", "Elon", "sujan", "sujan"]}
)

st.write(dataFrame)


st.line_chart(dataFrame)

char_data = pd.DataFrame(np.random.randn(20, 4), columns=["a", "b", "c", "d"])

st.line_chart(char_data)
