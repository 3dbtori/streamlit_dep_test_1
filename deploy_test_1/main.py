import streamlit as st

# 画像表示
st.write('Display Image')

# ボタンで画像表示、非表示
if st.checkbox('show?'):
    st.write('success')