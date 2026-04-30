jarak_rumah = int(input("Masukan Jarak rumah (dalam satuan km): ") )

jarak = jarak_rumah * 1000

if jarak < 3000 :
 print ("Jarak Aman") 
else:
 print ("Jarak Terlalu Jauh")