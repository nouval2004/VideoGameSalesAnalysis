# Video Game Sales Analysis With Phyton

This repository contains a comprehensive analysis and visualization of video game sales data. The project aims to provide insights into global sales trends, popular platforms, genres, and top publishers. By leveraging Python libraries such as pandas, matplotlib, and seaborn, we perform data cleaning, descriptive analysis, deep analysis, and create various visualizations to understand the video game market better.


# Table of Contents

1.Data Loading and Cleaning

2.Descriptive Analysis

3.Deep Analysis

4.Data Visualization



# Data Loading and Cleaning

The data_preprocessing.py script handles loading and cleaning the dataset. It includes functions for loading data, displaying basic information, and cleaning the data by removing missing values.

Explanation:

1.Loading Data: The load_data function reads the CSV file and loads it into a pandas DataFrame.

2.Displaying Data Information: The show_data_info function prints the first few rows, info, and descriptive statistics of the data.

3.Cleaning Data: The clean_data function checks for and removes any missing values from the data.

4.Saving Cleaned Data: The cleaned data is saved to a new CSV file.


# Descriptive Analysis

The analysis.py script performs descriptive analysis on the video game sales data. It calculates total global sales based on different categories such as platform, genre, and publisher.

Explanation:

1.Descriptive Analysis: The descriptive_analysis function groups the data by platform, genre, and publisher to calculate and print total global sales for each category.

2.Deep Analysis: The deep_analysis function calculates total global sales per year, regional sales distribution, and prints the correlation matrix of the dataset.


# Data Visualization

The visualisation.py script creates visualizations to better understand the video game sales data. It includes bar plots, line plots, and a heatmap.

Explanation:

1.Visualizing Sales by Platform: A bar plot showing total global sales by different platforms.

2.Visualizing Sales by Genre: A bar plot showing total global sales by different genres.

3.Top 10 Publishers by Sales: A bar plot showing the top 10 publishers by global sales.

4.Sales Trend Over the Years: A line plot showing the trend of global sales over the years.

# How to Use:

1. Run Data Preprocessing:

python data_preprocessing.py


2. Run Descriptive and Deep Analysis:

python analysis.py


3. Run Visualization:

python visualisation.py


By following these steps, you will be able to explore the video game sales data and gain valuable insights into the market trends and patterns.



5.Regional Sales Distribution: A bar plot showing the distribution of sales across different regions.

6.Correlation Matrix: A heatmap showing the correlation between different numerical variables in the dataset.

