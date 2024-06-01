import pandas as pd
from data_preprocessing import load_data, clean_data

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Muat dan bersihkan data
file_path = 'data/vgsales.csv'
data = load_data(file_path)
data = clean_data(data)

# Analisis Deskriptif
def descriptive_analysis(data):
    platform_sales = data.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False)
    print(platform_sales)

    genre_sales = data.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)
    print(genre_sales)

    publisher_sales = data.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False)
    print(publisher_sales)

# Analisis Mendalam
def deep_analysis(data):
    year_sales = data.groupby('Year')['Global_Sales'].sum()
    print(year_sales)
    
    regional_sales = data[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].sum()
    print(regional_sales)
    
    correlation_matrix = data.corr()
    print(correlation_matrix)

if __name__ == "__main__":
    descriptive_analysis(data)
    deep_analysis(data)
