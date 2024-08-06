from Araçlar import Otomobil, Motosiklet, Karavan
from Müşteriler import Müşteri, MüşteriListesi

# Araç listeleri
otomobil_listesi = [
    Otomobil(25, "BMW", "3.20", 200),
    Otomobil(25, "Audi", "A4", 180),
    Otomobil(25, "Mercedes", "C200", 220),
    Otomobil(25, "Volkswagen", "Passat", 190),
    Otomobil(25, "Toyota", "Corolla", 160),
    Otomobil(25, "Honda", "Civic", 170),
    Otomobil(25, "Ford", "Focus", 175),
    Otomobil(25, "Renault", "Megane", 165),
    Otomobil(25, "Peugeot", "308", 155),
    Otomobil(25, "Skoda", "Octavia", 185)
]

motosiklet_listesi = [
    Motosiklet(25, "Yamaha", "MT-07", 100),
    Motosiklet(25, "Honda", "CBR600RR", 150),
    Motosiklet(25, "Suzuki", "GSX-R600", 140),
    Motosiklet(25, "Kawasaki", "Ninja ZX-6R", 145),
    Motosiklet(25, "Ducati", "Monster 821", 160),
    Motosiklet(25, "BMW", "S1000RR", 200),
    Motosiklet(25, "Triumph", "Street Triple", 170),
    Motosiklet(25, "Harley-Davidson", "Iron 883", 180),
    Motosiklet(25, "KTM", "Duke 390", 130),
    Motosiklet(25, "Aprilia", "RS 660", 155)
]

karavan_listesi = [
    Karavan(25, "Volkswagen", "California", 300),
    Karavan(25, "Mercedes", "Marco Polo", 350),
    Karavan(25, "Ford", "Transit Custom Nugget", 320),
    Karavan(25, "Renault", "Trafic SpaceNomad", 310),
    Karavan(25, "Peugeot", "Traveller", 330),
    Karavan(25, "Citroen", "Spacetourer", 340),
    Karavan(25, "Opel", "Zafira Life", 315),
    Karavan(25, "Toyota", "Proace Verso", 325),
    Karavan(25, "Nissan", "NV300", 335),
    Karavan(25, "Hyundai", "H-1", 310)
]

# Müşteri listesi
müşteri_listesi = MüşteriListesi()
müşteri_listesi.müşteri_ekle(Müşteri("Ali", "Gümüş"))
müşteri_listesi.müşteri_ekle(Müşteri("Ayşe", "Gümüş"))
müşteri_listesi.müşteri_ekle(Müşteri("Mert", "Gümüş"))
müşteri_listesi.müşteri_ekle(Müşteri("Zeynep", "Altın"))
müşteri_listesi.müşteri_ekle(Müşteri("Aslı", "Altın"))
müşteri_listesi.müşteri_ekle(Müşteri("Polat", "Platin"))
müşteri_listesi.müşteri_ekle(Müşteri("Mehmet", "Platin"))
müşteri_listesi.müşteri_ekle(Müşteri("Yavuz", "Platin"))

def araç_seçimi(araç_listesi):
    """Kullanıcıdan araç seçimini alır."""
    for i, araç in enumerate(araç_listesi, start=1):
        print(f"{i}. {araç.marka} {araç.model} - Stok: {araç.stok} - Fiyat: {araç.fiyat} TL")
    seçim = int(input("İstediğiniz aracın numarasını girin: ")) - 1
    return araç_listesi[seçim]

def müşteri_seçimi():
    """Kullanıcıdan müşteri seçimini alır."""
    for i, müşteri in enumerate(müşteri_listesi.müşteriler, start=1):
        print(f"{i}. {müşteri.isim} - Tip: {müşteri.müşteri_tipi}")
    seçim = int(input("Müşteri numarasını girin: ")) - 1
    return müşteri_listesi.müşteriler[seçim]

def ana_menu():
    """Ana menüyü gösterir ve kullanıcıdan seçim alır."""
    ana_menü = True
    while True:
        if ana_menü:
            print("""
            ***** Araç Kiralama Sistemi *****
            A. Otomobil Kiralama
            B. Motosiklet Kiralama
            C. Karavan Kiralama
            D. Müşteri Ekleme/Silme
            E. Araç Marka-Model Ekleme/Silme
            Q. Çıkış
            """)
            ana_menü = False
            seçim = input("İstenilen menüdeki harfi girin: ").upper()

            if seçim == "A":
                while True:
                    print("""
                    ****** Otomobil Kiralama ******
                    1. Otomobil stoğunu göster
                    2. Saatlik Kiralama
                    3. Günlük Kiralama
                    4. Haftalık Kiralama
                    5. Ana Menüye Dön
                    6. Çıkış
                    """)
                    alt_seçim = input("Seçiminizi yapın: ")
                    if alt_seçim == "1":
                        for araç in otomobil_listesi:
                            print(araç.anlık_stok_görüntüle())
                    elif alt_seçim in ["2", "3", "4"]:
                        araç = araç_seçimi(otomobil_listesi)
                        müşteri = müşteri_seçimi()
                        adet = int(input("Kiralanacak araç adedini girin: "))
                        süre = int(input("Kiralanacak süreyi girin: "))
                        try:
                            teklif = araç.teklif_hazırla(adet, süre)
                            print(teklif)
                            if "en kısa sürede temin edilecektir" not in teklif:
                                indirim = müşteri.indirim_oranı(adet)
                                ''' 3'ten fazla araç kiralanırsa indirim oranına
                                 ek miktar indirim (İndirimi 1.5 katına çıkarır.)yapılmiştir '''
                                if adet > 3:
                                    indirim += indirim
                                toplam_fiyat = araç.kirala(adet, süre) * (1 - indirim)
                                gecikme = input("Araçları zamanında teslim edecek misiniz? (Evet/Hayır): ").lower()
                                if gecikme == "hayır":
                                    gecikme_süresi = int(input("Kaç gün gecikme olacak?: "))
                                    toplam_fiyat = araç.gecikme_cezasi_hesapla(toplam_fiyat, gecikme_süresi)
                                print(f"Toplam fiyat: {toplam_fiyat:.2f} TL, Uygulanan indirim: {indirim*75:.2f}%")
                                if araç.kritik_stok():
                                    print("Uyarı: Araç stoğu kritik seviyede!")
                        except ValueError as e:
                            print(e)
                    elif alt_seçim == "5":
                        ana_menü = True
                        break
                    elif alt_seçim == "6":
                        print("Çıkış yapılıyor...")
                        return
                    else:
                        print("Geçersiz seçim, tekrar deneyin.")
            elif seçim == "B":
                while True:
                    print("""
                    ****** Motosiklet Kiralama ******
                    1. Motosiklet stoğunu göster
                    2. Saatlik Kiralama
                    3. Günlük Kiralama
                    4. Haftalık Kiralama
                    5. Ana Menüye Dön
                    6. Çıkış
                    """)
                    alt_seçim = input("Seçiminizi yapın: ")
                    if alt_seçim == "1":
                        for araç in motosiklet_listesi:
                            print(araç.anlık_stok_görüntüle())
                    elif alt_seçim in ["2", "3", "4"]:
                        araç = araç_seçimi(motosiklet_listesi)
                        müşteri = müşteri_seçimi()
                        adet = int(input("Kiralanacak araç adedini girin: "))
                        süre = int(input("Kiralanacak süreyi girin: "))
                        try:
                            teklif = araç.teklif_hazırla(adet, süre)
                            print(teklif)
                            if "en kısa sürede temin edilecektir" not in teklif:
                                indirim = müşteri.indirim_oranı(adet)
                                ''' 3'ten fazla araç kiralanırsa indirim oranına
                                 ek miktar indirim (İndirimi 1.5 katına çıkarır.)yapılmiştir '''
                                if adet > 3:
                                    indirim += indirim
                                toplam_fiyat = araç.kirala(adet, süre) * (1 - indirim)
                                gecikme = input("Araçları zamanında teslim edecek misiniz? (Evet/Hayır): ").lower()
                                if gecikme == "hayır":
                                    gecikme_süresi = int(input("Kaç gün gecikme olacak?: "))
                                    toplam_fiyat = araç.gecikme_cezasi_hesapla(toplam_fiyat, gecikme_süresi)
                                print(f"Toplam fiyat: {toplam_fiyat:.2f} TL, Uygulanan indirim: {indirim*75:.2f}%")
                                if araç.kritik_stok():
                                    print("Uyarı: Araç stoğu kritik seviyede!")
                        except ValueError as e:
                            print(e)
                    elif alt_seçim == "5":
                        ana_menü = True
                        break
                    elif alt_seçim == "6":
                        print("Çıkış yapılıyor...")
                        return
                    else:
                        print("Geçersiz seçim, tekrar deneyin.")
            elif seçim == "C":
                while True:
                    print("""
                    ****** Karavan Kiralama ******
                    1. Karavan stoğunu göster
                    2. Saatlik Kiralama
                    3. Günlük Kiralama
                    4. Haftalık Kiralama
                    5. Ana Menüye Dön
                    6. Çıkış
                    """)
                    alt_seçim = input("Seçiminizi yapın: ")
                    if alt_seçim == "1":
                        for araç in karavan_listesi:
                            print(araç.anlık_stok_görüntüle())
                    elif alt_seçim in ["2", "3", "4"]:
                        araç = araç_seçimi(karavan_listesi)
                        müşteri = müşteri_seçimi()
                        adet = int(input("Kiralanacak araç adedini girin: "))
                        süre = int(input("Kiralanacak süreyi girin: "))
                        try:
                            teklif = araç.teklif_hazırla(adet, süre)
                            print(teklif)
                            if "en kısa sürede temin edilecektir" not in teklif:
                                indirim = müşteri.indirim_oranı(adet)
                                if adet > 3:
                                    ''' 3'ten fazla araç kiralanırsa indirim oranına
                                     ek miktar indirim (İndirimi 1.5 katına çıkarır.)yapılmiştir '''
                                    indirim += indirim
                                toplam_fiyat = araç.kirala(adet, süre) * (1 - indirim)
                                gecikme = input("Araçları zamanında teslim edecek misiniz? (Evet/Hayır): ").lower()
                                if gecikme == "hayır":
                                    gecikme_süresi = int(input("Kaç gün gecikme olacak?: "))
                                    toplam_fiyat = araç.gecikme_cezasi_hesapla(toplam_fiyat, gecikme_süresi)
                                print(f"Toplam fiyat: {toplam_fiyat:.2f} TL, Uygulanan indirim: {indirim*75:.2f}%")
                                if araç.kritik_stok():
                                    print("Uyarı: Araç stoğu kritik seviyede!")
                        except ValueError as e:
                            print(e)
                    elif alt_seçim == "5":
                        ana_menü = True
                        break
                    elif alt_seçim == "6":
                        print("Çıkış yapılıyor...")
                        return
                    else:
                        print("Geçersiz seçim, tekrar deneyin.")
            elif seçim == "D":
                while True:
                    print("""
                    ****** Kullanıcı İşlemleri ******
                    1. Kullanıcı Ekle
                    2. Kullanıcı Sil
                    3. Ana Menüye Dön
                    6. Çıkış
                    """)
                    alt_seçim = input("Seçiminizi yapın: ")
                    if alt_seçim == "1":
                        isim = input("Kullanıcı ismini girin: ")
                        tip = input("Kullanıcı tipini girin (Gümüş/Altın/Platin): ")
                        yeni_kullanıcı = Müşteri(isim, tip)
                        print(müşteri_listesi.müşteri_ekle(yeni_kullanıcı))
                    elif alt_seçim == "2":
                        isim = input("Silmek istediğiniz kullanıcı ismini girin: ")
                        print(müşteri_listesi.müşteri_sil(isim))
                    elif alt_seçim == "3":
                        ana_menü = True
                        break
                    elif alt_seçim == "6":
                        print("Çıkış yapılıyor...")
                        return
                    else:
                        print("Geçersiz seçim, tekrar deneyin.")
            elif seçim == "E":
                print("Bu özellik henüz mevcut değil.")
            elif seçim == "Q":
                print("Çıkış yapılıyor...")
                break
            else:
                print("Geçersiz seçim, tekrar deneyin.")

if __name__ == "__main__":
    ana_menu()
