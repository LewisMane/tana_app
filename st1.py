import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(page_title='Tana Web GIS', layout='wide', page_icon=":shark:")

# loading the png image
img = Image.open("./img/tana.png")

# removing menu and footer note
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden; }
    footer {visibility: hidden; }
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.image(img, width=700)

st.write("""
####         A map displaying Water Service Providers under TWWDA coverage area

*Select an option in the select box below to view your desired WSP*
""")

HtmlFile = open("./maps/compiled.html", 'r')
Tana_map = HtmlFile.read()
components.html(Tana_map, height=700)
