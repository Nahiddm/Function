class Kalkulator :
    def Pertambahan(self,x,y,z) :
        a = x + y + z
        return a

    def Pengurangan(self,x,y,z) :
        a = x - y - z
        return a

    def Perkalian(self,x,y,z) :
        a = x * y * z
        return a

    def Pembagian(self,x,y,z) :
        a = x / y /z
        return a

objek = Kalkulator()

x = int(input("Masukkan Bil1 : "))
y = int(input("Masukkan Bil2 : "))
z = int(input("Masukkan Bil3 :"))
print("Hasil Pertambahan ketiga bilangan bulat\t=",objek.Pertambahan(x,y,z))
print("Hasil Perkurangan ketiga bilangan bulat\t=",objek.Pengurangan(x,y,z))
print("Hasil Perkalian ketiga bilangan bulat\t=",objek.Perkalian(x,y,z))
print("Hasil Pembagian ketiga bilangan bulat\t=",objek.Pembagian(x,y,z))
