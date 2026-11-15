import streamlit as st
from utils.goetic_ui import shell, card
shell("Symbolarium","A visual index of seals, symbols, terms, and attributed correspondences.")
tabs=st.tabs(["Seals & sigils","Terminology","Correspondences"])
with tabs[0]:
    st.caption("SEAL INDEX · PLACEHOLDER ARTWORK")
    cols=st.columns(3)
    for i,name in enumerate(["Bael","Paimon","Astaroth","Buer","Stolas","Belial"]):
        with cols[i%3]: card(name,"GOETIC SEAL","Add the sourced seal image and edition attribution here.","☉")
with tabs[1]:
    st.markdown("### Glossary")
    for term,desc in [("Legion","A military unit; counts are reported as given in a particular text."),("Goetia","A term associated with magic/spirits; meanings vary by historical context."),("Lemegeton","The title commonly used for the Lesser Key of Solomon.")]:
        st.markdown(f"**{term}** — {desc}")
with tabs[2]:
    st.markdown("### Correspondence tables")
    st.info("Keep correspondences edition-specific and clearly label later occult additions.")
