def main():
    matriksA = []
    matriksB = []

    while True:
        print("\nMENU OPERASI MATRIKS")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == '4':
            print("Program selesai. Sampai jumpa!")
            break

        if not matriksA or not matriksB:
            baris = int(input("Masukkan jumlah baris: "))
            kolom = int(input("Masukkan jumlah kolom: "))

            print("Isi Matriks A:")
            matriksA = []
            for i in range(baris):
                row = [int(input(f"A[{i+1}][{j+1}]: ")) for j in range(kolom)]
                matriksA.append(row)

            print("Isi Matriks B:")
            matriksB = []
            for i in range(baris):
                row = [int(input(f"B[{i+1}][{j+1}]: ")) for j in range(kolom)]
                matriksB.append(row)

        if pilihan == '1':
            hasil = [[matriksA[i][j] + matriksB[i][j] for j in range(len(matriksA[0]))] for i in range(len(matriksA))]
            print("Hasil Penjumlahan:")
            for r in hasil:
                print(r)

        elif pilihan == '2':
            hasil = [[matriksA[i][j] - matriksB[i][j] for j in range(len(matriksA[0]))] for i in range(len(matriksA))]
            print("Hasil Pengurangan:")
            for r in hasil:
                print(r)

        elif pilihan == '3':
            baris_a = len(matriksA)
            kolom_a = len(matriksA[0])
            baris_b = len(matriksB)
            kolom_b = len(matriksB[0])

            if kolom_a != baris_b:
                print("Perkalian tidak bisa dilakukan!")
            else:
                hasil = []
                for i in range(baris_a):
                    row_hasil = []
                    for j in range(kolom_b):
                        total = 0
                        for k in range(kolom_a):
                            total += matriksA[i][k] * matriksB[k][j]
                        row_hasil.append(total)
                    hasil.append(row_hasil)

                print("Hasil Perkalian:")
                for r in hasil:
                    print(r)
        else:
            print("Pilihan tidak valid!")

main()