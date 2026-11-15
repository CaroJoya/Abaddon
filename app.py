import streamlit as st
from utils.llm import answer

st.title("Ars Goetia — Educational Assistant")
st.caption("Descriptive study aid. Not ritual instruction.")

if "history" not in st.session_state:
    st.session_state.history = []

q = st.chat_input("Ask about a spirit, rank, symbol, or source…")
if q:
    st.session_state.history.append(("user", q))
    reply = answer(q)
    st.session_state.history.append(("assistant", reply))

for role, msg in st.session_state.history:
    with st.chat_message(role):
        st.markdown(msg)