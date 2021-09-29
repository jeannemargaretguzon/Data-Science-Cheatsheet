            

            with st.echo():

                fig = plt.figure(figsize=(20, 6))
                
                ax = sns.lineplot(x = "year", y = "passengers", data = flights, marker='s') 
                ax.set_title('Passenger Count every year', fontweight = 'demibold', fontsize = 17)
                ax.set_xlabel('Month', fontsize = 12)
                ax.set_ylabel('Passenger Count', fontsize = 12)
            st.pyplot(fig)    
        elif r_step == 'Bar Graph':
            st.markdown("""
                # Bar Graph
                ## **Recommended for: **
                <ul><li>Showing rankings
                ## **Tips: **
                <hr>
            """, unsafe_allow_html=True)
            
            "### *Example*: "
            "Using Seaborn: "
            with st.echo():
                penguin = sns.load_dataset('penguins') # Example dataset from Seaborn
                sns.set_style('whitegrid')

                fig = plt.figure(figsize=(20, 6))

                ax = sns.barplot(x = 'species', y = 'flipper_length_mm', data = penguin, ci = None, color ='#FFEB3B')
                ax.set_title('Which Penguin Species has longer flipper?', fontweight = 'demibold', fontsize = 17)
                ax.set_xlabel('Body Mass (in g)', fontsize = 12)
                ax.set_ylabel('Flipper Length (in mm)', fontsize = 12)
            st.pyplot(fig)       
        
        elif r_step == 'Horizontal Bar Graph':
            st.markdown("""
                # Horizontal Bar Graph
                ## Recommended for: 
                <ul><li>Showing rankings
                    <li>Especially if the labels are long
                    <li>The items in the chart have over 5 categories
            """, unsafe_allow_html=True)
            
            "### *Example*: "
            "Using Seaborn: "
            with st.echo():
                flights = sns.load_dataset('flights') # Example dataset from Seaborn 
                sns.set_style('whitegrid')

                fig = plt.figure(figsize=(20, 6))

                ax = sns.barplot(x = 'passengers', y = 'month', orient = 'h',data = flights, ci = None)
                ax.set_title('Passenger Count every month', fontweight = 'demibold', fontsize = 17)
                ax.set_xlabel('Passenger Count', fontsize = 12)
                ax.set_ylabel('Month', fontsize = 12)
            st.pyplot(fig)

        elif r_step == 'Stacked Bar Graph':
            st.markdown("""
                # Stacked Bar Graph
                ## Recommended for: 
                <ul><li>Comparing parts of the items to the its total
            """, unsafe_allow_html=True)
            
            "### *Example*: "
            "Using Seaborn: "
            with st.echo():
                penguin = sns.load_dataset('penguins') # Example dataset from Seaborn

                sns.set(style = "ticks")

                penguin_sex = penguin.groupby(by = 'sex').size() # Grouping the penguin sex column  

                fig, ax = plt.subplots(figsize=(20, 10))

                ax.bar(penguin.species, penguin_sex['Male'], color = '#90CAF9', label = 'Male')
                ax.bar(penguin.species, penguin_sex['Female'], bottom = penguin_sex['Male'], color = '#EF5350', label = 'Female')

                ax.set_title('Penguin Population and Gender Per Species', fontweight = 'bold', fontsize = 20) 
                ax.set_xlabel('Species', fontsize = 15)
                ax.set_ylabel('Population by Gender', fontsize = 15)
                ax.legend()
            st.pyplot(fig)

        elif r_step == 'Scatter Plot':
            st.markdown("""
                # Scatter Plot
                ## Recommended for: 
                <ul><li>Observing relationships between variables

                ### Take Note of the Patterns
                <ul><li>Strong Positive Linear
                    <li>Moderate Negative Linear
                    <li>Null / No Relationship
                    <li>Strong Non linear
            """, unsafe_allow_html=True)
            
            "### *Example*: "
            "Using Seaborn: "
            with st.echo():
                penguin = sns.load_dataset('penguins') # Example dataset from Seaborn
                sns.set(style = "ticks")
                fig = plt.figure(figsize=(5, 2.5))
                
                ax = sns.scatterplot( data = penguin, x = "flipper_length_mm", y = "bill_length_mm", color = '#194A8D',legend = False, sizes = (50, 100))
                ax.set_title('Flipper Length and Bill Length of Penguinn', fontweight = 'demibold', fontsize = 17)
                ax.set_xlabel('Flipper Length', fontsize = 12)
                ax.set_ylabel('Bill Length', fontsize = 12)
            st.pyplot(fig)

        elif r_step == 'Box Plot':
            st.markdown("""
                # Scatter Plot
                ## Recommended for:
                <ul><li>Showing the: 
                    <ul><li>Lowest data point
                    <li>Largest data point
                    <li>Middle data point
                    <li>Median of the lower half of the dataset
                    <li>Median of the lower half of the dataset
            """, unsafe_allow_html=True)
            
            "### *Example*: "
            "Using Seaborn: "
            with st.echo():
                flights = sns.load_dataset('flights') # Example dataset from Seaborn 
                sns.set_style('whitegrid')

                fig = plt.figure(figsize=(20, 6))

                ax=sns.boxplot(data = flights, x = 'month', y = 'passengers')
                ax.set_title('Passenger Count every month', fontweight = 'demibold', fontsize = 17)
                ax.set_xlabel('Passenger Count', fontsize = 12)
                ax.set_ylabel('Month', fontsize = 12)
            st.pyplot(fig)                

        elif r_step == 'Bubble Plot':
            st.markdown("""
                # Scatter Plot
                ## Recommended for:
                <ul><li>Comparisons of three variables

                ### Take Note of the Patterns
                <ul><li>Strong Positive Linear
                    <li>Moderate Negative Linear
                    <li>Null / No Relationship
                    <li>Strong Non linear
            """, unsafe_allow_html=True)
            
            "### *Example*: "
            "Using Seaborn: "
            with st.echo():
                penguin = sns.load_dataset('penguins') # Example dataset from Seaborn
                sns.set(style = "ticks")
                fig = plt.figure(figsize=(5, 2.5))
                
                ax = sns.scatterplot( data = penguin, x = "flipper_length_mm", y = "bill_length_mm", size = 'body_mass_g', color = '#194A8D',legend = False, alpha=0.8, sizes = (50, 100))
                ax.set_title('Flipper Length, Bill Length, and Body Mass of Penguin', fontweight = 'demibold', fontsize = 17)
                ax.set_xlabel('Flipper Length', fontsize = 12)
                ax.set_ylabel('Bill Length', fontsize = 12) 
            st.pyplot(fig)        

        elif r_step == 'Histogram':
            st.markdown("""
                # Histogram
                ## Recommended for:
                <ul><li>Items that have continous measurement
                    <li>Showing distribution of values among the items
                    <li>Showing the center of the data

            """, unsafe_allow_html=True)
            
            "### *Example*: "
            "Using Seaborn: "
            with st.echo():
                penguin = sns.load_dataset('penguins') # Example dataset from Seaborn
                sns.set(style = "ticks")
                fig = plt.figure(figsize=(20, 6))
                
                ax = sns.histplot(x = 'island', data = penguin)
                ax.set_title('Penguin Living Spaces', fontweight = 'demibold', fontsize = 17)
                ax.set(xlabel='Living Spaces', ylabel='Penguin Population') 
            st.pyplot(fig)
    elif chapter == 'Subplotting':
        "Nothing"           