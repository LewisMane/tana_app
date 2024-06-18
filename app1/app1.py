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
####  A map displaying projects undertaken by TWWDA

*click on a marker to view project details*
""")

HtmlFile = open("./maps/tana_map1.html", 'r')
Tana_map = HtmlFile.read()
components.html(Tana_map, height=700)

st.subheader("Map Legend 🗺")

col1, col2, col3 = st.columns([2, 2, 2])
col1.markdown("""
<span style='color:blue;'>
. ADB_H2O 
</span>=
<span style='color:brown;'>
Africa Development Bank Water Project
</span><br>
<span style='color:blue;'>
. Cc_Ws 
</span>=
<span style='color:brown;'>
Crosscounty Water Supply
</span><br>
<span style='color:blue;'>
. Bh_Eq 
</span>=
<span style='color:brown;'>
Borehole Equipping
</span><br>
<span style='color:blue;'>
. Complete_BH 
</span>=
<span style='color:brown;'>
Complete BoreHole Projects
</span>

""",
              unsafe_allow_html=True)

col2.markdown("""
<span style='color:blue;'>
. ADB_Swg
</span>=
<span style='color:brown;'>
Africa Development Bank Sewerage Project
</span><br>
<span style='color:blue;'>
. Cc_ws 
</span> =
<span style='color:brown;'>
Crosscounty Water Supply
</span><br>
<span style='color:blue;'>
. Bh_Dr 
</span>=
<span style='color:brown;'>
Borehole Drilling
</span>

""",
              unsafe_allow_html=True)

col3.markdown("""
<span style='color:green;'>
. Plan & Des 
</span> =
<span style='color:green;'>
Planning and Design stage 
</span><br>
""",
              unsafe_allow_html=True)
