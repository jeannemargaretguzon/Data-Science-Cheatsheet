from re import T
from threading import setprofile
from types import FunctionType

import streamlit as st
import Data_Visual as dv

st.set_page_config(layout="wide")

st.sidebar.markdown("""
    <h1 style=><b>DATA SCIENCE CHEATSHEET<b></h1>
    <small><i>A notebook for data analytics</i></small>
    <hr>
""", unsafe_allow_html=True)

option = st.sidebar.radio('Topics', 
                        ['Data Visualization', 'Data Cleaning'])

if option == 'Data Visualization':
    chapter = st.selectbox("Table of Contents",
                    ['Introduction', 'Visualization Graphs', 'Subplotting'])
dv.data_visual(chapter) # Data_Visual.py