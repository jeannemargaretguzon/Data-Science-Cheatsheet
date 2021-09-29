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
        st.markdown(""" <ol><li> Create a list of questions your visuals need to answer.<\li>
        <li> What feature of your questions that the visuals need to show?<\li>
        <li> Select what type of graph based on the highlighted features.<\li><\ol>
        """, unsafe_allow_html=True)
        
        col1, col2, col3= st.columns(3)
        with col1:
            st.header("Important Parts of Visualization graphs")   
            """
            * Graph
            * Graph title
            * X-label and Y-label
            """         