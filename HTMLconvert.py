import streamlit as st
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# Funkce pro převod HTML textu do naformátovaného textu s podporou odrážek
def convert_html_to_text(html):
    # Použijeme markdownify k převodu HTML do Markdown, který pak Streamlit podporuje.
    markdown_text = md(html)
    return markdown_text

# Hlavní část aplikace
st.title('Převod HTML do naformátovaného textu')

html_input = st.text_area('Vložte HTML text zde', height=200)
if st.button('Převést'):
    formatted_text = convert_html_to_text(html_input)
    st.subheader('Naformátovaný text')
    st.markdown(formatted_text)

