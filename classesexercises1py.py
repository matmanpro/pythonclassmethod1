class calisan:
    zam_orani = 1.05
    per_say = 0
    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.eposta = self.ad+self.soyad+'@sirket.com'
        calisan.per_say = calisan.per_say + 1
    def tamad(self):
        return 'adi: {}  soyadi: {}'.format(self.ad, self.soyad)

    def arttir(self):
        self.maas = (self.maas * self.zam_orani)

personel1 = calisan('Ali','Demir',2500)
print(calisan.per_say)
print(personel1.maas)
personel1.arttir()
print(personel1.maas)
personel2 = calisan('Alperen','Yigit',3200)
print(calisan.per_say)

# print(personel1)
# print(personel1.ad, personel1.soyad, personel1.eposta)
# print(personel1.tamad())
# print(calisan.per_say)

# print(personel2)
# print(personel2.ad, personel2.soyad)

# print(calisan.tamad(personel1))
