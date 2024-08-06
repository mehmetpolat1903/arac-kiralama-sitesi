class Müşteri:
    def __init__(self, isim, müşteri_tipi):
        """
        Müşteri sınıfının kurucu metodu.
        Müşteri ismi ve müşteri tipi bilgilerini alır.

        Args:
            isim (str): Müşteri ismi.
            müşteri_tipi (str): Müşteri tipi (Gümüş, Altın, Platin).
        """
        self.isim = isim
        self.müşteri_tipi = müşteri_tipi

    def indirim_oranı(self, kiralanan_arac_sayisi):
        """
        Müşteri tipine göre indirim oranını hesaplar.

        Args:
            kiralanan_arac_sayisi (int): Kiralanan araç sayısı.

        Returns:
            float: İndirim oranı.
        """
        oran = 0.0
        if self.müşteri_tipi == "Gümüş":
            oran = 0.05
        elif self.müşteri_tipi == "Altın":
            oran = 0.15
        elif self.müşteri_tipi == "Platin":
            oran = 0.2

        return oran


class MüşteriListesi:
    def __init__(self):
        """
        MüşteriListesi sınıfının kurucu metodu.
        Müşteri listesini başlatır.
        """
        self.müşteriler = []

    def müşteri_ekle(self, müşteri):
        """
        Listeye yeni müşteri ekler.

        Args:
            müşteri (Müşteri): Eklenecek müşteri nesnesi.

        Returns:
            str: Başarı mesajı.
        """
        self.müşteriler.append(müşteri)
        return f"{müşteri.isim} listeye eklendi."

    def müşteri_sil(self, isim):
        """
        Listeden müşteri siler.

        Args:
            isim (str): Silinecek müşterinin ismi.

        Returns:
            str: Başarı veya hata mesajı.
        """
        for müşteri in self.müşteriler:
            if müşteri.isim == isim:
                self.müşteriler.remove(müşteri)
                return f"{isim} listeden silindi."
        return f"{isim} listede bulunamadı."
