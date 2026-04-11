mahasiswa = {
    "2510":"mila",
    "1170":"zara",
    "0796":"maelah"
    }
nilai = {
    "2510":[50, 70, 80, 90],
    "1170":[30, 50, 70, 80] ,
    "0796":[75, 78, 85, 90]
    }
nama_MK= ["MK1", "MK2", "MK3", "MK4"]
max_rata_mhs = -1
mhs_terpintar = ""

for nim, daftar_nilai in nilai.items():
    rata_rata = sum(daftar_nilai)/len(daftar_nilai)
    if rata_rata > max_rata_mhs:
        max_rata_mhs = rata_rata
        mhs_terpintar = mahasiswa[nim]

min_rata_MK = float ('inf')
mk_terkecil = ""

for i in range(len(nama_MK)):
    total_nilai_mk = 0
    for nim in nilai:
        total_nilai_mk += nilai[nim][i]

    rata_mk = total_nilai_mk/len(nilai)

    if rata_mk < min_rata_MK:
        min_rata_MK = rata_mk
        mk_terkecil = nama_MK[i]

print(f"Mahasiswa Terpintar : {mhs_terpintar} (Nilai : {max_rata_mhs:.2f})")
print(f"Mata Kuliah Nilai Terkecil : {mk_terkecil} (Nilai : {min_rata_MK:.2f})")