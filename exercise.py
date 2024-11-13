nama = (input('nama mahasiswa :'))
umur = int(input('umur :'))
pekerjaan = (input('pekerjaan orang tua :'))
gaji = int(input('gaji orang tua :'))  
ipk = float(input('masukan ipk :'))

daftar_pekerjaan  = ['dokter' , 'tni' , 'pns']
if(umur < 25) and (pekerjaan is not  daftar_pekerjaan ) and (gaji >= 1000000) and (ipk >= 2.7):
    hasil = "mendapat beasiswa"
else:
    hasil = "mendapat beasiswa"

print ('nama : ' , nama) 
print ('umur : ' , umur)  
print('pekerjaan :' , pekerjaan)
print('gaji orang tua :' , gaji)
print("ipk :" , ipk)
print(hasil)