import streamlit as st
from utils.goetic_ui import shell, card
shell("The Archive","A catalog of the seventy-two spirits traditionally listed in the Ars Goetia.")
st.caption("ARCHIVE INDEX · SEARCH / FILTER / DISCOVER")
q=st.text_input("Search the archive",placeholder="Name, rank, alias, attributed office…")
c1,c2,c3=st.columns(3)
with c1: rank=st.selectbox("Rank",["All ranks","King","Duke","Prince","Marquis","President","Earl","Knight"])
with c2: sort=st.selectbox("Order",["Traditional order","Alphabetical"])
with c3: view=st.selectbox("View",["Cards","Compact list"])
# Replace this sample with your loaded get_demons() data.
sample=[("01","Bael","King","First spirit in the traditional sequence; attributed command over sixty-six legions."),
("02","Agares","Duke","A duke associated in the text with thirty legions."),
("03","Vassago","Prince","A prince described as revealing hidden or lost things."),
("04","Samigina","Marquis","A marquis associated with knowledge and the dead."),
("05","Marbas","President","A president attributed with knowledge of arts and diseases."),
("06","Valefor","Duke","A duke associated with thirty-six legions.")]
st.info("UI preview uses sample entries. Connect the cards to your existing knowledge loader.")
cols=st.columns(3)
for i,(num,name,r,desc) in enumerate(sample):
    with cols[i%3]:
        card(f"{num} · {name}",r,desc,"✧")
