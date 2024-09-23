import pandas as pd
import numpy as np

# Mengatur random seed untuk reproducibility
np.random.seed(42)

# Membuat data
tanggal = pd.date_range(start="2023-01-01", periods=100, freq='D')
produk = [f'Produk {chr(65 + i)}' for i in range(10)]  # Produk A, B, C, ..., J
jumlah = np.random.randint(1, 20, size=100)  # Jumlah antara 1 dan 20
harga = np.random.choice([15000, 20000, 22000, 25000, 26000, 27000, 29000, 30000], size=100)

# Membuat DataFrame
data_penjualan = pd.DataFrame({
    'Tanggal': tanggal,
    'Produk': np.random.choice(produk, size=100),
    'Jumlah': jumlah,
    'Harga': harga
})

# Menyimpan DataFrame ke file CSV
file_path = "data_penjualan_besar.csv"
data_penjualan.to_csv(file_path, index=False)

print(f"Data penjualan berhasil dibuat dan disimpan di {file_path}")
