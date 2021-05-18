"""
Tipe data dictionary sekdedar menghubungkan antara KEY dan VALUE
KVP = Key Value Pair
dictionary = kamus
"""
kamus_ind_eng = {'anak': 'son', 'istri': 'wife', 'ayah': 'father', 'ibu': 'mother'}
print(kamus_ind_eng)
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['ibu'])
print('Data ini dikirimkan oleh server Gojek untuk memberikan info driver di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal': '2021-5-18',
    'driver_list': [
        {'Nama':'Eko', 'jarak': 10},
        {'Nama':'Dwi','Jarak': 30},
        {'Nama':'Tri', 'Jarak':50},
        {'Nama':'Catur','Jarak': 100}
                    ]
}
print(data_dari_server_gojek)
print(f"\nDriver di sekitar sini: {data_dari_server_gojek['driver_list']}")
print(f"Driver #1: {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver #4: {data_dari_server_gojek['driver_list'][3]}")
print(f"\nDriver terdekat berjarak: {data_dari_server_gojek['driver_list'][0]['jarak']} meter")