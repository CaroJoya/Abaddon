import streamlit as st
from utils.goetic_ui import shell, card
shell("Library","Editions, manuscripts, bibliographic references, and research notes.")
st.markdown("### Shelf")
cols=st.columns(3)
with cols[0]: card("Primary text","EDITION","The edition used for the archive’s spirit-entry transcription.","Ⅰ")
with cols[1]: card("Manuscript context","HISTORY","Compilation, transmission, and manuscript background.","Ⅱ")
with cols[2]: card("Modern scholarship","COMMENTARY","Secondary sources and scholarly discussion.","Ⅲ")
st.markdown("### Source register")
st.caption("Use this table as a starting UI; populate from your knowledge/research JSON.")
st.dataframe([{"ID":"SRC-001","Title":"The Goetia","Type":"Primary text","Used for":"Spirit entries"},{"ID":"SRC-002","Title":"Historical commentary","Type":"Secondary","Used for":"Context"}],use_container_width=True,hide_index=True)
st.markdown("### Research notes")
st.text_area("Private working notes",placeholder="Keep your own observations and unresolved questions here…")
