ogrenciler = []

def ogrenci_ekle(ad_soyad):
    ogrenciler.append(ad_soyad)
    numara = ogrenciler.index(ad_soyad)
    print(f"{ad_soyad} adlı öğrenci eklendi. Numarası: {numara}")

def ogrenci_sil(num_silinecek):
    silinecekler = []
    for i in range(num_silinecek):
        num = int(input(f"Silmek istediğiniz {i+1}. öğrencinin numarasını giriniz: "))
        if num in range(len(ogrenciler)):
            silinecekler.append(num)
        else:
            print("Geçersiz numara!")
    if silinecekler:
        silinecekler.sort(reverse=True)
        for num in silinecekler:
            ogrenciler.pop(num)
        print(f"{len(silinecekler)} öğrenci silindi.")
    else:
        print("Hiçbir öğrenci silinmedi.")
            
def ogrenci_listele():
    print("Öğrenci Listesi:")
    for i, ogrenci in enumerate(ogrenciler):
        print(f"{i}. {ogrenci}")

while True:
    print("\nSeçenekler:")
    print("1- Öğrenci Ekle")
    print("2- Öğrenci Sil")
    print("3- Öğrenci Listele")
    print("4- Çıkış")
    secim = int(input("Seçiminiz: "))
    
    if secim == 1:
        ad_soyad = input("Öğrencinin adı soyadı: ")
        ogrenci_ekle(ad_soyad)
    elif secim == 2:
        num_silinecek = int(input("Kaç öğrenci silmek istiyorsunuz? "))
        ogrenci_sil(num_silinecek)
    elif secim == 3:
        ogrenci_listele()
    elif secim == 4:
        print("Program sonlandırılıyor...")
        break
    else:
        print("Geçersiz seçim!")
