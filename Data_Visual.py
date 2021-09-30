from os import write
from re import T
from threading import setprofile
from types import FunctionType
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from seaborn.rcmod import set_style
from seaborn.relational import lineplot, scatterplot

import streamlit as st

def data_visual(chapter): 
    if chapter == 'Introduction':
        intro()
    elif chapter == 'Visualization Graphs':
        visual()

def intro():
    "# GENERAL GUIDES TO VISUALIZATION" 
    "*Language used: Python*"
    st.markdown(""" 
    <ol><li> Create a list of questions your visuals need to answer.
        <li> What feature of your questions that the visuals need to show?
        <li> Select what type of graph based on the highlighted features.
    """, unsafe_allow_html=True)
        
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Color Guides")
        st.write(""" 
        Be mindful of colorblindness. 
        Don't use color combinations that are hard on color blind individuals.
        """)
        # Add color combinations later
    with col2:
        st.markdown("### Font Guides")
        st.markdown("""
        <ul><li>It's recommended to use <b>San Serif
            <li>Keep the font and its sizes consistent throughout the presentation
            <li>You can change headers/title to a larger size for better readibility
        """, unsafe_allow_html=True)

def visual():
    r_step = st.selectbox('Visualization Graphs', 
                        ['Line Graph', 'Bar Graph', 'Horizontal Bar Graph', 
                        'Stacked Bar Graph', 'Box Plot',
                        'Scatter Plot', 'Bubble Plot', 'Histogram'])
    if r_step == 'Line Graph':
        lineg()
    elif r_step == 'Bar Graph':
        barg()
    elif r_step == 'Horizontal Bar Graph':
        hbarg()
    elif r_step == 'Stacked Bar Graph':
        stackedbarg()
    elif r_step == 'Box Plot':
        boxp()
    elif r_step == 'Scatter Plot':
        scatterp()
    elif r_step == 'Bubble Plot':
        bubblep()
    elif r_step == 'Histogram':
        histogram()
            
# Visualization Graphs
def lineg():
    st.header("Line Graph")
    st.write("Recommended for tracking changes over periods of time")
    st.text("Importing data...")
            
    with st.echo():
        flights = sns.load_dataset('flights') # Example dataset from Seaborn 
        sns.set_style('whitegrid')

    st.markdown("### Using Matplotlib")
    with st.echo():
        fig1 = plt.figure(figsize=(20, 6))
        ax = plt.plot(flights['year'], flights['passengers'], marker='s', c='red', linewidth=2, markersize=12)
        plt.title('Passenger Count every year', fontweight = 'demibold', fontsize = 17)
        plt.xlabel('Month', fontsize = 12)
        plt.ylabel('Passenger Count', fontsize = 12)
        plt.show()
    st.pyplot(fig1)

    st.markdown("### Using Seaborn")
    with st.echo():
        fig2 = plt.figure(figsize=(20, 6))
        ax = sns.lineplot(x = "year", y = "passengers", data = flights, marker='s', color='red', linewidth=2, markersize=12) 
        ax.set_title('Passenger Count every year', fontweight = 'demibold', fontsize = 17)
        ax.set_xlabel('Month', fontsize = 12)
        ax.set_ylabel('Passenger Count', fontsize = 12)
    st.pyplot(fig2)
def barg():
    st.header("Bar Graph")
    st.write("Recommended for showing rankings")
    st.text("Importing data...")
            
    with st.echo():
        penguin = sns.load_dataset('penguins') # Example dataset from Seaborn
        sns.set_style('whitegrid')

    st.markdown("### Using Matplotlib")
    with st.echo():
        fig1 = plt.figure(figsize=(20, 6))

        ax = plt.bar(penguin['species'], penguin['flipper_length_mm'], color ='#FFEB3B')
        plt.title('Which Penguin Species has longer flipper?', fontweight = 'demibold', fontsize = 17)
        plt.xlabel('Body Mass (in g)', fontsize = 12)
        plt.ylabel('Flipper Length (in mm)', fontsize = 12)
    st.pyplot(fig1)

    st.markdown("### Using Seaborn")
    with st.echo():
        fig2 = plt.figure(figsize=(20, 6))

        ax = sns.barplot(x = 'species', y = 'flipper_length_mm', data = penguin, ci = None, color ='#FFEB3B')
        ax.set_title('Which Penguin Species has longer flipper?', fontweight = 'demibold', fontsize = 17)
        ax.set_xlabel('Body Mass (in g)', fontsize = 12)
        ax.set_ylabel('Flipper Length (in mm)', fontsize = 12)
    st.pyplot(fig2)
def hbarg():
    st.header("Horizontal Bar Graph")
    st.markdown(""" ## Recommended for: 
    <ul><li>Showing rankings
    <li>Especially if the labels are long
    <li>The items in the chart have over 5 categories
    """, unsafe_allow_html=True)
    
    st.text("Importing data...")
            
    with st.echo():
        flights = sns.load_dataset('flights') # Example dataset from Seaborn 
        sns.set_style('whitegrid')

    st.markdown("### Using Matplotlib")
    with st.echo():
        fig1 = plt.figure(figsize=(20, 6))

        ax = plt.barh(flights['month'], flights['passengers'])
        plt.title('Passenger Count every month', fontweight = 'demibold', fontsize = 17)
        plt.xlabel('Passenger Count', fontsize = 12)
        plt.ylabel('Month', fontsize = 12)
    st.pyplot(fig1)

    st.markdown("### Using Seaborn")
    with st.echo():
        fig2 = plt.figure(figsize=(20, 6))

        ax = sns.barplot(x = 'passengers', y = 'month', orient = 'h', data = flights, ci = None)
        ax.set_title('Passenger Count every month', fontweight = 'demibold', fontsize = 17)
        ax.set_xlabel('Passenger Count', fontsize = 12)
        ax.set_ylabel('Month', fontsize = 12)
    st.pyplot(fig2)
def stackedbarg():    
    st.header("Stacked Bar Graph")
    st.write("Comparing parts of the items to the its total")
    
    st.text("Importing data...")        
    with st.echo():
        penguin = sns.load_dataset('penguins') # Example dataset from Seaborn
        sns.set_style('whitegrid')
        penguin_sex = penguin.groupby(by = 'sex').size() # Grouping the penguin sex column  

    st.markdown("### Using Matplotlib")
    with st.echo():    
        fig1, ax = plt.subplots(figsize=(20, 10))

        ax.bar(penguin.species, penguin_sex['Male'], color = '#90CAF9', label = 'Male')
        ax.bar(penguin.species, penguin_sex['Female'], bottom = penguin_sex['Male'], color = '#EF5350', label = 'Female')

        plt.title('Penguin Population and Gender Per Species', fontweight = 'bold', fontsize = 20) 
        plt.xlabel('Species', fontsize = 15)
        plt.ylabel('Population by Gender', fontsize = 15)
        plt.legend()
    st.pyplot(fig1)

    # st.markdown("### Using Seaborn")
    # graph
def boxp():
    st.header("Box Plot")
    st.markdown("""
    ## Recommended for:
    <ul><li>Showing the: 
    <ul><li>Lowest data point
        <li>Largest data point
        <li>Middle data point
        <li>Median of the lower half of the dataset
        <li>Median of the lower half of the dataset""", unsafe_allow_html=True)
    st.text("Importing data...")
            
    with st.echo():
        flights = sns.load_dataset('flights') # Example dataset from Seaborn 
        sns.set_style('whitegrid')

    # st.markdown("### Using Matplotlib")

    st.markdown("### Using Seaborn")
    with st.echo():
        fig2 = plt.figure(figsize=(20, 6))
        
        ax=sns.boxplot(data = flights, x = 'month', y = 'passengers')
        ax.set_title('Passenger Count every month', fontweight = 'demibold', fontsize = 17)
        ax.set_xlabel('Passenger Count', fontsize = 12)
        ax.set_ylabel('Month', fontsize = 12)
    st.pyplot(fig2)
def scatterp():
    st.header("Scatter Plot")
    st.write("Recommended for observing relationships between variables")
    st.markdown("""
    ### Take Note of the Patterns
    <ul><li>Strong Positive Linear
        <li>Moderate Negative Linear
        <li>Null / No Relationship
        <li>Strong Non linear
    """, unsafe_allow_html=True)

    st.text("Importing data...")
            
    with st.echo():
        penguin = sns.load_dataset('penguins') # Example dataset from Seaborn
        sns.set_style('whitegrid')

    st.markdown("### Using Matplotlib")
    with st.echo():
        fig1 = plt.figure(figsize=(5, 2.5))

        ax = plt.scatter(penguin["flipper_length_mm"], penguin["bill_length_mm"], color = '#194A8D', sizes = (50, 100))
        plt.title('Flipper Length and Bill Length of Penguinn', fontweight = 'demibold', fontsize = 17)
        plt.xlabel('Flipper Length', fontsize = 12)
        plt.ylabel('Bill Length', fontsize = 12)
    st.pyplot(fig1)

    st.markdown("### Using Seaborn")
    with st.echo():
        fig2 = plt.figure(figsize=(5, 2.5))
                
        ax = sns.scatterplot( data = penguin, x = "flipper_length_mm", y = "bill_length_mm", color = '#194A8D',legend = False, sizes = (50, 100))
        ax.set_title('Flipper Length and Bill Length of Penguinn', fontweight = 'demibold', fontsize = 17)
        ax.set_xlabel('Flipper Length', fontsize = 12)
        ax.set_ylabel('Bill Length', fontsize = 12)
    st.pyplot(fig2)    
def bubblep():
    st.header("Bubble Plot")
    st.write("Recommended for comparisons of three variables")
    st.markdown("""
    ### Take Note of the Patterns
    <ul><li>Strong Positive Linear
        <li>Moderate Negative Linear
        <li>Null / No Relationship
        <li>Strong Non linear
    """, unsafe_allow_html=True)

    st.text("Importing data...")
            
    with st.echo():
        penguin = sns.load_dataset('penguins') # Example dataset from Seaborn
        sns.set_style('whitegrid')

    st.markdown("### Using Matplotlib")
    with st.echo():
        fig1 = plt.figure(figsize=(5, 2.5))

        ax = plt.scatter(penguin["flipper_length_mm"], penguin["bill_length_mm"], s=penguin['body_mass_g'], color = '#194A8D', alpha=0.8, sizes = (50, 100))
        plt.title('Flipper Length and Bill Length of Penguinn', fontweight = 'demibold', fontsize = 17)
        plt.xlabel('Flipper Length', fontsize = 12)
        plt.ylabel('Bill Length', fontsize = 12)
    st.pyplot(fig1)

    st.markdown("### Using Seaborn")
    with st.echo():
        fig2 = plt.figure(figsize=(5, 2.5))
                
        ax = sns.scatterplot( data = penguin, x = "flipper_length_mm", y = "bill_length_mm", size = 'body_mass_g', color = '#194A8D',legend = False, alpha=0.8, sizes = (50, 100))
        ax.set_title('Flipper Length, Bill Length, and Body Mass of Penguin', fontweight = 'demibold', fontsize = 17)
        ax.set_xlabel('Flipper Length', fontsize = 12)
        ax.set_ylabel('Bill Length', fontsize = 12) 
    st.pyplot(fig2)    
def histogram():
    st.header("Histogram")
    st.write("Recommended for comparisons of three variables")
    st.markdown("""
    ## Recommended for:
    <ul><li>Items that have continous measurement
        <li>Showing distribution of values among the items
        <li>Showing the center of the data
    """, unsafe_allow_html=True)

    st.text("Importing data...")
            
    with st.echo():
        penguin = sns.load_dataset('penguins') # Example dataset from Seaborn
        sns.set_style('whitegrid')

    st.markdown("### Using Matplotlib")
    with st.echo():
        fig1 = plt.figure(figsize=(5, 2.5))

        ax = plt.hist(x = 'island', data = penguin)
        plt.title('Penguin Living Spaces', fontweight = 'demibold', fontsize = 17)
        plt.xlabel('Living Spaces')
        plt.ylabel('Penguin Population')
    st.pyplot(fig1)

    st.markdown("### Using Seaborn")
    with st.echo():
        fig2 = plt.figure(figsize=(5, 2.5))
                
        ax = sns.histplot(x = 'island', data = penguin)
        ax.set_title('Penguin Living Spaces', fontweight = 'demibold', fontsize = 17)
        ax.set(xlabel='Living Spaces', ylabel='Penguin Population') 
    st.pyplot(fig2)        