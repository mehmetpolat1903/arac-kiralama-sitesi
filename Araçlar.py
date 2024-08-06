class Araç:
    def __init__(self, stok, marka, model, fiyat):
        """
        Araç sınıfının kurucu metodu.
        Araç stok, marka, model ve fiyat bilgilerini alır.

        Args:
            stok (int): Araç stok adedi.
            marka (str): Araç markası.
            model (str): Araç modeli.
            fiyat (int): Araç kiralama fiyatı.
        """
        self.stok = stok
        self.marka = marka
        self.model = model
        self.fiyat = fiyat

    def anlık_stok_görüntüle(self):
        """
        Mevcut stok durumunu gösterir.

        Returns:
            str: Araç marka, model ve stok bilgisi.
        """
        return f"{self.marka} {self.model} - Stok: {self.stok}"

    def kirala(self, adet, süre):
        """
        Araç kiralama işlemi gerçekleştirir.
        Stok kontrolü yapar ve yeterli stok varsa kiralama işlemi yapılır.

        Args:
            adet (int): Kiralanacak araç adedi.
            süre (int): Kiralama süresi (saat, gün, hafta).

        Returns:
            int: Toplam kiralama maliyeti.

        Raises:
            ValueError: Yeterli stok olmadığında hata fırlatır.
        """
        if adet > self.stok:
            raise ValueError(f"Yeterli stok yok. En kısa sürede araç temin edilecektir. (Mevcut stok: {self.stok})")
        self.stok -= adet
        return adet * süre * self.fiyat

    def kritik_stok(self):
        """
        Stok durumunun kritik seviyede olup olmadığını kontrol eder.

        Returns:
            bool: Stok %25'in altındaysa True, değilse False.
        """
        return self.stok < (25 * 0.25)

    def teklif_hazırla(self, adet, süre):
        """
        Stok yetersizse alternatif teklif sunar.

        Args:
            adet (int): İstenen araç adedi.
            süre (int): Kiralama süresi.

        Returns:
            str: Teklif mesajı.
        """
        if adet > self.stok:
            gerekli_adet = adet - self.stok
            return f"Şu anda {adet} adet araç yok. {self.stok} adet mevcut. Geriye kalan {gerekli_adet} adet araç en kısa sürede temin edilecektir."
        return "Stokta yeterli araç mevcut."

    def gecikme_cezasi_hesapla(self, toplam_fatura, gecikme_süresi):
        """
        Gecikme cezasını hesaplar ve toplam fatura tutarına ekler.

        Args:
            toplam_fatura (float): Kiralama için ödenecek toplam tutar.
            gecikme_süresi (int): Gecikme süresi (gün olarak).

        Returns:
            float: Gecikme cezası eklenmiş toplam tutar.
        """
        gecikme_cezasi = toplam_fatura * 0.2
        return toplam_fatura + gecikme_cezasi


class Otomobil(Araç):
    """
    Otomobil sınıfı, Araç sınıfından türetilmiştir.
    Otomobillere özel işlemler için kullanılabilir.
    """
    pass


class Motosiklet(Araç):
    """
    Motosiklet sınıfı, Araç sınıfından türetilmiştir.
    Motosikletlere özel işlemler için kullanılabilir.
    """
    pass


class Karavan(Araç):
    """
    Karavan sınıfı, Araç sınıfından türetilmiştir.
    Karavanlara özel işlemler için kullanılabilir.
    """
    pass
