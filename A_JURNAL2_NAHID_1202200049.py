print("===================")


class Kubus1():
    def __init__(self,K1):
        self.sisi = K1
    def show1(self):
        print("===================")
        print("Kubus 1")         
    def volume(self):
        print("volume\t\t=", self.sisi**3,"cm^3")
    def luas_permukaan(self):
        print ("luas permukaan\t=", self.sisi**2*6,"cm^2")
    def keliling(self):
        print("Keliling\t=",self.sisi*12,"cm")

class Kubus2():
    def __init__(self,K2):
        self.sisi = K2
    def show2(self):
        print("===================")
        print("Kubus 2")        
    def volume(self):
        print("volume\t\t=", self.sisi**3,"cm^3")
    def luas_permukaan(self):
        print ("luas permukaan\t=", self.sisi**2*6,"cm^2")
    def keliling(self):
        print("Keliling\t=",self.sisi*12,"cm")
        print("===================")
K1=int(input("Masukkan Sisi Kubus 1 :"))
K2=int(input("Masukkan Sisi Kubus 2 :"))
Kubus1=Kubus1(K1)
Kubus1.show1()
Kubus1.volume()
Kubus1.luas_permukaan()
Kubus1.keliling()

Kubus2=Kubus2(K2)
Kubus2.show2()
Kubus2.volume()
Kubus2.luas_permukaan()
Kubus2.keliling()