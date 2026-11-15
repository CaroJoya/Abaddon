import streamlit as st
from pathlib import Path

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=IM+Fell+English&family=IBM+Plex+Mono:wght@400;500&display=swap');
:root { --ink:#171512; --paper:#e8dfc9; --gold:#b69a61; --muted:#a79b84; --line:rgba(182,154,97,.25); }
.stApp { background: radial-gradient(ellipse at 15% 0%, #29241c 0%, #171512 45%, #11100e 100%); color:#e8dfc9; }
[data-testid="stSidebar"] { background:#100f0d; border-right:1px solid var(--line); }
[data-testid="stSidebar"] * { color:#d9cdb4; }
.block-container { max-width:1450px; padding-top:2.2rem; padding-bottom:4rem; }
h1,h2,h3 { font-family:'Cormorant Garamond',serif !important; color:#e9dec5 !important; letter-spacing:.02em; }
p,li,label { color:#c9bda5; }
div[data-testid="stMetric"] { background:#211d17; border:1px solid var(--line); padding:1rem; border-radius:4px; }
div[data-testid="stMetricLabel"] { color:#a99a7e; font-family:'IBM Plex Mono',monospace; }
div[data-testid="stMetricValue"] { color:#d7b978; font-family:'Cormorant Garamond',serif; }
.stButton>button { border:1px solid #8d7549; background:#211d17; color:#dfcfad; border-radius:2px; }
.stButton>button:hover { border-color:#d3b574; color:#fff0cc; background:#30271b; }
input,textarea,[data-baseweb="select"] { background:#211d17 !important; color:#e8dfc9 !important; }
hr { border-color:var(--line); }
.goetic-eyebrow { font:11px 'IBM Plex Mono',monospace; color:#b69a61; letter-spacing:.18em; text-transform:uppercase; }
.goetic-title { font: clamp(42px,5vw,72px) 'IM Fell English',serif; color:#e8dfc9; margin:.15em 0 .1em; }
.goetic-subtitle { font:17px 'Cormorant Garamond',serif; color:#a99b82; max-width:680px; }
.goetic-rule { height:1px; background:linear-gradient(90deg,#9b7d48,transparent); margin:1.5rem 0; }
.goetic-card { background:linear-gradient(145deg,#252018,#191612); border:1px solid rgba(182,154,97,.28); padding:1.2rem; border-radius:3px; min-height:150px; }
.goetic-card h3 { margin:.2rem 0 .5rem; font-size:27px; }
.goetic-card .meta { font:10px 'IBM Plex Mono',monospace; letter-spacing:.1em; color:#a58b59; text-transform:uppercase; }
.goetic-card p { font-size:15px; }
.goetic-seal { width:74px;height:74px;border:1px solid #8f7546;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#c5a66a;font:28px 'IM Fell English',serif;margin-bottom:1rem; }
.goetic-note { border-left:2px solid #9a7b46; padding:.6rem 1rem; background:#201b15; color:#bfb095; }
.small-mono { font:11px 'IBM Plex Mono',monospace;color:#8f826b; }
</style>
"""

def shell(section, subtitle):
    st.markdown(CSS, unsafe_allow_html=True)
    st.markdown(f'<div class="goetic-eyebrow">LEMEGETON · DIGITAL ARCHIVE / {section.upper()}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="goetic-title">{section}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="goetic-subtitle">{subtitle}</div>', unsafe_allow_html=True)
    st.markdown('<div class="goetic-rule"></div>', unsafe_allow_html=True)

def card(title, meta, body, symbol="✦"):
    st.markdown(f'<div class="goetic-card"><div class="goetic-seal">{symbol}</div><div class="meta">{meta}</div><h3>{title}</h3><p>{body}</p></div>', unsafe_allow_html=True)

def footer():
    st.markdown('<div class="goetic-rule"></div><div class="small-mono">ABADDON · SCHOLARLY / DESCRIPTIVE / SOURCE-AWARE</div>', unsafe_allow_html=True)
