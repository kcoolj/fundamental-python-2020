#tipe data skalar => tipe data sederhana
print('tipe data skalar => tipe data sederhana')
anak1 = 'Eko'
anak2 = 'Dwi'
anak3 = 'Tri'
anak4 = 'Catur'

print (anak1)
print (anak2)
print (anak3)
print (anak4)

#tipe data list/array/daftar
print('\ntipe data list/array/daftar')
anak = ['Eko', 'Dwi', 'Tri', 'Catur']
print (anak)
anak.append('Limo')
print(anak)

#sapa anak ke-2
print('\nsapa anak ke-2')
print(f'Hai {anak[1]}!')

#sapa semua anak
print('\nsapa semua anak')
for a in anak:
    print(f'Hai {a}')

#sapa semua anak: cara ribet
print('\nsapa semua anak: cara ribet')
for a in range(0,len(anak)):
    print(f'{a+1}. Hai {anak[a]}')