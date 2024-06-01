import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def show_data_info(data):
    print(data.head())
    print(data.info())
    print(data.describe())

def clean_data(data):
    # Cek nilai yang hilang
    missing_values = data.isnull().sum()
    print(missing_values)
    
    # Menghapus nilai yang hilang
    data = data.dropna()
    return data

if __name__ == "__main__":
    file_path = 'data/vgsales.csv'
    data = load_data(file_path)
    show_data_info(data)
    data = clean_data(data)
    # Simpan data yang sudah dibersihkan jika perlu
    data.to_csv('data/cleaned_vgsales.csv', index=False)
