#KONSTRUKSI DASAR PYTHON
#SEQUENTIAL: Eksekusi berurutan
print('Hello world!')
print('by KJ')
print('tanggal 21 April 2021')
print('-'*10)

#PERCABANGAN: Eksekusi Terpilih
ingin_cepat = False
if ingin_cepat:
    print('Jalan lurus aja ya!')
else:
    print('Jalan lain')
#PERCABANGAN: Pilihan Lebih dari 2
ingin_balik = True


#PERULANGAN
jumlah_anak = 4
for index_anak in range(1, jumlah_anak+1):   #jumlah perulangan = 5 - 1 = 4
    print(f'Halo anak #{index_anak}')