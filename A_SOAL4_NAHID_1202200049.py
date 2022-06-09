class celana():
    def abaka(self):
        print("Celana tahan air")
    def pandan(self):
        print("Menghasilkan efek harum")
    def batu(self):
        print("Menghasilkan perlindungan maksimal")

b = input("Masukan Bahan : ")
if b == "abaka":
        a=celana()
        a.abaka()
elif b == "pandan":
        a=celana()
        a.pandan()
elif b == "batu":
        a=celana()
        a.batu()
else:
    print("Bahan tidak diketahui")