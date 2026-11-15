import streamlit as st
from utils.goetic_ui import shell, card
shell("Hierarchy","Explore the ranks and offices used in the traditional Goetic catalog.")
st.markdown("### The offices")
st.caption("A navigable classification—not a claim that every historical source uses identical hierarchy.")
ranks=[
("Kings","Royal office","Bael · Paimon · Beleth · Asmoday · Vine · Balam · Zagan · Belial"),
("Dukes","Ducal office","Agares · Valefor · Astaroth · Bathin · Gusion · Eligos · etc."),
("Princes","Princely office","Vassago · Sitri · Ipos · Stolas · Seere"),
("Marquises","Marquisate","Samigina · Amon · Leraje · Naberius · etc."),
("Presidents","Presidential office","Marbas · Buer · Botis · Morax · Glasya-Labolas · etc."),
("Earls / Counts","Comital office","Furfur · Raum · Bifrons · Andromalius"),
("Knights","Knightly office","Furcas")]
for row in ranks:
    card(row[0],row[1].upper(),row[2],"♜")
st.markdown("### Reading the hierarchy")
st.markdown('<div class="goetic-note">Rank labels and counts can vary across editions and transcriptions. Keep source attribution visible in every detail view.</div>',unsafe_allow_html=True)
