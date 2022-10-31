a = input("masukkan nilai a = ")
b = input("masukkan nilai b = ")
print("nilai variabel a = ",a)
print("nilai variabel b = ",b)
print("hasil penggabungan {1}&{0}=%d".format(a,b)%(a+b))

# konversi nilai variabel
a = int(a)
b = int(b)
print("hasil penjumlahan {1}+{0}=%d".format(a,b)%(a+b))
print("hasil penjumlahan {1}/{0}=%d".format(a,b)%(a/b))