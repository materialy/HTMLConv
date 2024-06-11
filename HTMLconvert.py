import streamlit as st
from bs4 import BeautifulSoup
import html

# Funkce pro převod HTML textu do Markdown
def convert_html_to_markdown(html_content):
    # Decode HTML entities
    decoded_html = html.unescape(html_content)
    
    soup = BeautifulSoup(decoded_html, 'html.parser')
    
    # Převedení tagů <b> na Markdown bold
    for bold in soup.find_all('b'):
        bold.insert_before('**')
        bold.insert_after('**')
    
    # Převedení tagů <strong> na normální text
    for strong in soup.find_all('strong'):
        strong.unwrap()
    
    # Převedení tagů <em>, <i> na Markdown italic
    for italic in soup.find_all(['em', 'i']):
        italic.insert_before('_')
        italic.insert_after('_')
    
    # Převedení tagů <a> na Markdown odkazy
    for a in soup.find_all('a'):
        href = a.get('href')
        text = a.text
        a.replace_with(f'[{text}]({href})')
    
    # Převedení tagů <ul> a <ol>
    for ul in soup.find_all('ul'):
        for li in ul.find_all('li'):
            li.insert_before('- ')
            li.insert_after('\n')
        ul.unwrap()
    
    for ol in soup.find_all('ol'):
        for index, li in enumerate(ol.find_all('li'), start=1):
            li.insert_before(f'{index}. ')
            li.insert_after('\n')
        ol.unwrap()
    
    # Převedení tagů <p> na nové řádky
    for p in soup.find_all('p'):
        p.insert_before('\n\n')
        p.insert_after('\n\n')
    
    # Extrakce textu
    return soup.get_text()

# Hlavní část aplikace
st.title('Převod HTML do naformátovaného textu')

html_input = st.text_area('Vložte HTML text zde', height=200)
if st.button('Převést'):
    formatted_text = convert_html_to_markdown(html_input)
    st.subheader('Naformátovaný text')
    st.markdown(formatted_text)

