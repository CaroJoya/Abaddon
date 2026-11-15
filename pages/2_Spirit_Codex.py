import streamlit as st
from utils.goetic_ui import shell, card
shell("Spirit Codex","A close-reading profile for one entry in the Goetic catalog.")
names=["Bael","Agares","Vassago","Samigina","Marbas","Valefor","Amon","Barbatos"]
selected=st.selectbox("Choose an entry",names)
st.markdown(f"## {selected}")
st.markdown('<div class="goetic-note">PROFILE TEMPLATE · connect this selector to your 72-spirit dataset.</div>',unsafe_allow_html=True)
a,b,c=st.columns([1,1,1])
a.metric("Traditional number","01" if selected=="Bael" else "—")
b.metric("Rank","King" if selected=="Bael" else "—")
c.metric("Legions","66" if selected=="Bael" else "—")
st.markdown("### Description")
st.write("Insert the entry’s attributed appearance and description here, preserving the wording and edition attribution.")
st.markdown("### Offices & attributed powers")
st.write("Structured list of offices or abilities described in the selected source.")
left,right=st.columns(2)
with left: card("Source notes","TEXTUAL HISTORY","Edition, translation, spelling, and variant readings.","⌘")
with right: card("Related entries","CROSS-REFERENCES","Related ranks, names, or concepts in the archive.","∞")
st.markdown("### Ask about this entry")
question=st.text_input("Research question",placeholder=f"What does the source say about {selected}?")
if st.button("Send to Research Desk"):
    st.session_state["codex_question"]=f"About {selected}: {question}"
    st.switch_page("pages/4_Research_Desk.py")
