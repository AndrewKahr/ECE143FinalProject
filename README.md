# Group 3: Analysis of Mental Health Trends in Tech
This repo contains our data and code to generate the visualizations in our presentation. You can view our presentation 
by looking at the `Group 19 Mental Health in Tech Slides.pdf` file.

# File structure
The `data` folder contains the csv files from 2016 to 2020 for the survey questions. There are also 5 python files that 
contain unique functions for data cleaning and plot generation. These can be found in the 
`modules` folder.

## Python Files
**clean.py:** Includes functions to clean our dataset and return a merged dataframe we can generate visualizations with  
**barplot_percentage_vs_size.py:** Includes function that graphs bar graph that represents the percentage of a certain 
column output with respect to company size  
**column_value_count_H.py:** Includes function that graphs bar graph horizontally that represents the number of each 
output in a data series  
**line_percentage_plot_vs_time.py:** Includes function that will categorize the column data with the corresponding 
value of the other column and generates lines for how categorized data and the percentage of wanted output trend over 
the time  
**util.py:**  Includes functions that can draw a single line graph and a function that can draw double line graph by 
passing in the data and title of the graphs  

The repo also contains a requirements.txt at the root of the repo to generate a compatible conda environment.

# How to run the code
First create a new conda environment with the requirements.txt file by running the following: 
`conda create --name <env_name> --file requirements.txt`. Replace `<env_name>` with the name you want to give the environment.
Then navigate to the `Group 19 Mental Health in Tech.ipynb` 
and open it with Jupyter Notebook. This notebook will call the appropriate functions and generate our data visualizations.

# Main Packages
- Numpy
- Pandas
- Matplotlib
- Seaborn
