#Kullanıcıdan bir dik üçgenin a ve b kenarlarını alıp c kenarını yani hipotenüsünü hesaplamak!
#Kenarları a ve b olan hipotenüsü c olan bir dik üçgen olsun.

def hipotenus_hesap():
    # Kullanıcıdan kenar uzunluklarını alıyoruz.
    a = int(input("Dik Üçgenin Birinci Kenarını Giriniz: "))
    b = int(input("Dik Üçgenin İkinci  Kenarını Giriniz: "))

    # Hipotenüs hesaplama formülü
    c= (a ** 2 + b ** 2)** 0.5  # Karekökü almak için üs kullanıyoruz.

    # Sonucu yazdırıyoruz
    print("Hipotenüs:", c)

hipotenus_hesap() #Fonksiyonu Hipotenüs için kullabilirsin.
