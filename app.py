from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="VikasAI",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      .block-container { max-width: 100%; padding: 0; }
      header[data-testid="stHeader"], footer { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).resolve().parent / "index.html"
components.html(html_path.read_text(encoding="utf-8"), height=1000, scrolling=True)