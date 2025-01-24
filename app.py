import streamlit as st

st.write('Welcome to my app')


st.markdown('# Batch 1911 is hosting this one')

spell = st.secrets['spell']
key = st.secrets.some_magic_api.key

st.write(spell)
st.write(key)
