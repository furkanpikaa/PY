# sehirler = ["İstanbul","Ankara","İzmir"]

# for sehir in sehirler:
#     print(sehir)

# for sayi in range(0,10,2):
#     print(sayi)


# sayac = 1
# while sayac <= 10:
#     print(sayac)
#     sayac = sayac + 1

# isim = input("Adınız: ")   #input = kullanıcıdan bilgi alma.
# print("isim: "+ isim)

sayi = int(input("Kaçın faktöriyelini hesaplayayım: "))

a = 1

if sayi < 0:
    print("negatif sayıların faktöriyeli hesaplanmaz.")
elif sayi == 0:
    print("sonuç : 1") 
else:
    for i in range(1,sayi+1): #+1 i ekledik çünkü girilen sayi da dahil olmalı!
        a = a * i
    print("Sonuç: ", a)



