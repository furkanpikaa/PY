class Matematik:
    def __init__(self,sayi1,sayi2): #constructor-yapıcı
         self.sayi1 = sayi1
         self.sayi2 = sayi2
         print("matematik başladı (referansı oluştu)")

    def topla(self):
        return self.sayi1 + self.sayi2
    def cikar(self):
        return self.sayi1 - self.sayi2
    def bol(self):
        return self.sayi1 / self.sayi2
    def carp(self):
        return self.sayi1 * self.sayi2



matematik = Matematik(6,7)
sonuc = matematik.carp()
print("Topla : "+ str(sonuc))


class Istatistik(Matematik):
    def __init__(self, sayi1, sayi2):
        super().__init__(sayi1, sayi2) # baz aldığı sınıf
    def varyansHesapla(self):
        return self.sayi1 * self.sayi2   

istatistik = Istatistik(5,8)



