import streamlit as st
from utils.goetic_ui import shell
shell("Research Desk","Ask source-aware questions. Treat generated responses as research assistance, not primary evidence.")
st.markdown('<div class="goetic-note">The assistant should distinguish textual evidence, historical context, and uncertainty.</div>',unsafe_allow_html=True)
if "desk_history" not in st.session_state: st.session_state.desk_history=[]
for msg in st.session_state.desk_history:
    with st.chat_message(msg["role"]): st.markdown(msg["content"])
prefill=st.session_state.pop("codex_question","")
prompt=st.chat_input("Ask about a spirit, passage, rank, or source…")
if prefill and not prompt: prompt=prefill
if prompt:
    st.session_state.desk_history.append({"role":"user","content":prompt})
    with st.chat_message("user"): st.markdown(prompt)
    # Connect your existing utils.llm.answer(prompt) here.
    try:
        from utils.llm import answer
        response=answer(prompt)
    except Exception as e:
        response=f"Backend connection placeholder: connect your existing answer function. ({e})"
    st.session_state.desk_history.append({"role":"assistant","content":str(response)})
    with st.chat_message("assistant"): st.markdown(str(response))
