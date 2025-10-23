import pandas as pd

# Membaca data dari file CSV
data = pd.read_csv("calon_tni.csv")

print("=== Data Calon TNI ===")
print(data.to_string(index=False))

# Statistik dasar tinggi badan
print("\n=== Statistik Dasar Tinggi Badan ===")
stats = data["tinggi"].describe()
print(stats)

mean_tinggi = round(stats["mean"], 2)
max_tinggi = stats["max"]
min_tinggi = stats["min"]
median_tinggi = data["tinggi"].median()

print(f"\nRata-rata tinggi : {mean_tinggi} cm")
print(f"Tertinggi        : {max_tinggi} cm")
print(f"Terendah         : {min_tinggi} cm")
print(f"Median           : {median_tinggi} cm")

# Calon dengan tinggi di atas rata-rata
print("\n=== Calon di atas rata-rata tinggi ===")
di_atas_rata = data[data["tinggi"] > mean_tinggi]
print(di_atas_rata.to_string(index=False))

# Urutan dari tertinggi ke terendah
print("\n=== Urutan dari Tertinggi ke Terendah ===")
urut = data.sort_values(by="tinggi", ascending=False)
print(urut.to_string(index=False))

# Menambahkan kategori tinggi badan
def kategori_tinggi(t):
    if t >= 180:
        return "Tinggi"
    elif t >= 170:
        return "Sedang"
    else:
        return "Pendek"

data["kategori"] = data["tinggi"].apply(kategori_tinggi)
print("\n=== Data dengan Kategori ===")
print(data.to_string(index=False))

# Jumlah calon per kategori
print("\n=== Jumlah Calon per Kategori ===")
print(data["kategori"].value_counts())

# Statistik lanjutan
print("\n=== Statistik Lanjutan ===")
std = round(data["tinggi"].std(), 2)
var = round(data["tinggi"].var(), 2)
print(f"Standar Deviasi : {std}")
print(f"Variansi        : {var}")

# Calon dengan tinggi badan tertinggi
print("\n=== Calon dengan Tinggi Badan Tertinggi ===")
tertinggi = data[data["tinggi"] == data["tinggi"].max()].iloc[0]
print(f"Nama    : {tertinggi['nama']}")
print(f"Alamat  : {tertinggi['alamat']}")
print(f"Tinggi  : {tertinggi['tinggi']} cm")
