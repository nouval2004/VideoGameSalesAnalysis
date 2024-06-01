import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_preprocessing import load_data, clean_data

    
# Muat dan bersihkan data
file_path = 'data/cleaned_vgsales.csv'
data = load_data(file_path)
data = clean_data(data)

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Visualisasi
def visualize_data(data):
    # Visualisasi penjualan global berdasarkan platform
    platform_sales = data.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    platform_sales.plot(kind='bar')
    plt.title('Total Global Sales by Platform')
    plt.xlabel('Platform')
    plt.ylabel('Global Sales (in millions)')
    plt.show()

    # Visualisasi penjualan global berdasarkan genre
    genre_sales = data.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    genre_sales.plot(kind='bar')
    plt.title('Total Global Sales by Genre')
    plt.xlabel('Genre')
    plt.ylabel('Global Sales (in millions)')
    plt.show()


    # Visualisasi penjualan global berdasarkan penerbit (top 10)
    publisher_sales = data.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False)
    top_publishers = publisher_sales.head(10)
    plt.figure(figsize=(10, 6))
    top_publishers.plot(kind='bar')
    plt.title('Top 10 Publishers by Global Sales')
    plt.xlabel('Publisher')
    plt.ylabel('Global Sales (in millions)')
    plt.show()

    # Visualisasi tren penjualan berdasarkan tahun
    year_sales = data.groupby('Year')['Global_Sales'].sum()
    plt.figure(figsize=(10, 6))
    year_sales.plot()
    plt.title('Global Sales Trend Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Global Sales (in millions)')
    plt.show()

    # Visualisasi penjualan regional
    regional_sales = data[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].sum()
    plt.figure(figsize=(10, 6))
    regional_sales[:-1].plot(kind='bar')
    plt.title('Regional Sales Distribution')
    plt.xlabel('Region')
    plt.ylabel('Sales (in millions)')
    plt.show()

    # Visualisasi matriks korelasi
    correlation_matrix = data.corr()
    plt.figure(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()

if __name__ == "__main__":
    visualize_data(data)
