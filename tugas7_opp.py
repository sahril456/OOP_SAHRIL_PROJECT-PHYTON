kbps =int(input("kategori kecepatan internet (mbps): "))
mbps =kbps/1000
if mbps > 50:
   kategori ="Sangat Cepat"
elif mbps > 20:
   kategori="Cepat"
elif mbps > 5:
   kategori="Sedang"
else:
   kategori="Lambat"
print("Kecepatan:",mbps,"Mbps")
print("Kategori:", kategori)