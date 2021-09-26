from threading import setprofile
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from seaborn.rcmod import set_style
from seaborn.relational import lineplot

import streamlit as st

def data_visual(): 
    st.write("""# Visualization Graphs""")
    st.sidebar.write(
    """
        ---
        ## Visualization Guide
        1. Create a list of questions your visuals need to answer.
        2. What feature of your questions that the visuals need to show?
        3. Select what type of graph based on the highlighted features.
    """
    )
    
    r_step = st.selectbox('', 
                            ['Line Graph', 'Pie Graph', 'Bar Graph', 
                            'Area Graph', 'Bar Graph', 'H-Bar Graph', 
                            'Stacked Bar Graph', 'Scatter Plot', 'Bubble Plot', 
                            'Histogram'])

    if r_step == 'Line Graph':
        # Importing penguin.csv example dataset 
        st.markdown('<h2 style="color:red"> hello world</h2>', unsafe_allow_html=True)
        
        with st.echo():
            flights = sns.load_dataset('flights')
            
            fig_1 = plt.figure(figsize=(20, 6))

            sns.set_style('whitegrid')
            ax = sns.lineplot(x = "year", y = "passengers", data = flights, marker='s') 
            ax.set_title('Passenger Count every year', fontweight = 'demibold', fontsize = 17)
            ax.set_xlabel('Month', fontsize = 12)
            ax.set_ylabel('Passenger Count', fontsize = 12)
            st.pyplot(fig_1)

# Main
st.sidebar.write('*A cheatsheet for data analytics*')
sb_step = st.sidebar.radio('', 
                        ['Data Visualization', 'Data Extraction',
                        'Data Cleaning', 'Data Wrangling'])

if sb_step == 'Data Visualization':
     data_visual()