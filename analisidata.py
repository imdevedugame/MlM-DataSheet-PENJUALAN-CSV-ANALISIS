import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def muat_data(file_path):
    """Muat data dari file CSV."""
    try:
        data = pd.read_csv(file_path)
        print("Data Berhasil Dimuat")
        return data
    except Exception as e:
        print(f"Kesalahan saat memuat data: {e}")
        return None

def analisis_data(data):
    """Lakukan analisis dasar pada data."""
    print("Tampilan Data:")
    print(data.head())
    print("\nStatistik:")
    print(data.describe())
    
    # Visualisasi
    plt.figure(figsize=(12, 8))
    sns.set(style='whitegrid', palette='pastel')

    # Grafik Pairplot
    sns.pairplot(data, hue='Produk', markers='o', height=2.5)
    plt.suptitle('Pairplot Data Penjualan', y=1.02)  # Tambahkan judul
    plt.show()
    
    # Histogram Jumlah
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Jumlah'], bins=15, kde=True, color='skyblue')
    plt.title('Distribusi Jumlah Penjualan', fontsize=16)
    plt.xlabel('Jumlah', fontsize=14)
    plt.ylabel('Frekuensi', fontsize=14)
    plt.grid(True)
    plt.show()
    
    # Grafik Boxplot untuk Harga
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Produk', y='Harga', data=data, palette='Set2')
    plt.title('Boxplot Harga per Produk', fontsize=16)
    plt.xlabel('Produk', fontsize=14)
    plt.ylabel('Harga', fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()
    
    # Analisis dan Kesimpulan
    ringkasan_data(data)


def ringkasan_data(data):
    """Ringkas data dan berikan kesimpulan."""
    ringkasan = {}
    
    # Mengambil informasi dasar
    num_rows, num_cols = data.shape
    ringkasan['Jumlah Baris'] = num_rows
    ringkasan['Jumlah Kolom'] = num_cols
    ringkasan['Kolom'] = data.columns.tolist()
    
    # Cek untuk kolom numerik dan kategorikal
    kolom_numerik = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
    kolom_kategorikal = data.select_dtypes(include=['object']).columns.tolist()
    
    ringkasan['Kolom Numerik'] = kolom_numerik
    ringkasan['Kolom Kategorikal'] = kolom_kategorikal

    # Rata-rata dan modus untuk kolom numerik
    if kolom_numerik:
        for kolom in kolom_numerik:
            nilai_rata = data[kolom].mean()
            nilai_median = data[kolom].median()
            ringkasan[f'Rata-rata {kolom}'] = nilai_rata
            ringkasan[f'Median {kolom}'] = nilai_median
            
    # Analisis untuk kolom kategorikal
    if kolom_kategorikal:
        for kolom in kolom_kategorikal:
            nilai_modus = data[kolom].mode()[0]
            ringkasan[f'Modus {kolom}'] = nilai_modus

    # Analisis penjualan
    if 'Jumlah' in data.columns and 'Harga' in data.columns:
        # Total keuntungan
        data['Keuntungan'] = data['Jumlah'] * data['Harga']
        total_keuntungan = data['Keuntungan'].sum()
        ringkasan['Total Keuntungan'] = total_keuntungan
        
        # Barang paling banyak dan paling sedikit terjual
        barang_terjual = data.groupby('Produk')['Jumlah'].sum()
        barang_paling_banyak = barang_terjual.idxmax()
        jumlah_paling_banyak = barang_terjual.max()
        
        barang_paling_sedikit = barang_terjual.idxmin()
        jumlah_paling_sedikit = barang_terjual.min()
        
        ringkasan['Barang Paling Banyak Terjual'] = barang_paling_banyak
        ringkasan['Jumlah Paling Banyak Terjual'] = jumlah_paling_banyak
        ringkasan['Barang Paling Sedikit Terjual'] = barang_paling_sedikit
        ringkasan['Jumlah Paling Sedikit Terjual'] = jumlah_paling_sedikit
    
    # Menyimpulkan analisis
    print("\nRingkasan Analisis:")
    for kunci, nilai in ringkasan.items():
        print(f"{kunci}: {nilai}")
    
    print("\nKesimpulan:")
    if kolom_numerik:
        print(f"Rata-rata nilai dari kolom numerik adalah {ringkasan[f'Rata-rata {kolom_numerik[0]}']:.2f}.")
    if kolom_kategorikal:
        print(f"Produk paling umum yang dijual adalah {ringkasan[f'Modus {kolom_kategorikal[0]}']}.")
    
    if 'Total Keuntungan' in ringkasan:
        print(f"Total keuntungan dari penjualan adalah {ringkasan['Total Keuntungan']:.2f}.")
    print(f"Barang paling banyak terjual: {ringkasan['Barang Paling Banyak Terjual']} ({ringkasan['Jumlah Paling Banyak Terjual']} unit).")
    print(f"Barang paling sedikit terjual: {ringkasan['Barang Paling Sedikit Terjual']} ({ringkasan['Jumlah Paling Sedikit Terjual']} unit).")

def main():
    file_path = input("Masukkan path ke file CSV Anda: ")
    data = muat_data(file_path)
    
    if data is not None:
        analisis_data(data)

if __name__ == "__main__":
    main()
