from re import T
from threading import setprofile
from types import FunctionType
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from seaborn.rcmod import set_style
from seaborn.relational import lineplot

import streamlit as st

def data_visual(chapter): 
    if chapter == 'Introduction':
        "# GENERAL GUIDES TO VISUALIZATION" 
        "*Language used: Python*"
        st.markdown(""" <ol><li> Create a list of questions your visuals need to answer.<\li>
        <li> What feature of your questions that the visuals need to show?<\li>
        <li> Select what type of graph based on the highlighted features.
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Color Guides")
            """ Be mindful of colorblindness. 
            Don't use color combinations that are hard on color blind individuals.
            """
            # Add color combinations later
        with col2:
            st.markdown("### Font Guides")
            """" * It's recommended to use **San Serif** 
            * Keep the font and its sizes consistent throughout the presentation
            * You can change headers/title to a larger size for better readibility
            """
            
    elif chapter == 'Visualization Graphs':
        r_step = st.selectbox('Visualization Graphs', 
                            ['Line Graph', 'Bar Graph', 'Horizontal Bar Graph', 
                            'Stacked Bar Graph', 'Box Plot',
                            'Scatter Plot', 'Bubble Plot', 'Histogram'])    
    