
def gorev_ekle(gorev_listesi):
    gorev = input("Görev adı: ")
    gorev_listesi.append(gorev)
    print("Görev eklendi.")


def gorevleri_listele(gorev_listesi):
    if len(gorev_listesi) == 0:
        print("Henüz görev yok.")
    else:
        print("\nGörevler:")
        for i, gorev in enumerate(gorev_listesi, 1):
            print(f"{i}. {gorev}" + "\n")


def gorev_analizi(gorev_listesi):
    sayi = len(gorev_listesi)

    if sayi == 0:
        print("Henüz görev eklenmemiş." + "\n")
    elif 1 <= sayi <= 3:
        print("Görev durumu: Başlangıç seviyesi" + "\n")
    else:
        print("Görev durumu: Yoğun bir gün")


gorevler = []

while True:

    print("1-Görev ekle" + "\n" + 
      "2-Görevleri Listele" + "\n" +
      "3-Görev Analizi" + "\n" +
      "4-Çıkış"+ "\n" + "\n")

    secim = input("Seciminiz: ")

    if secim == "1":
        gorev_ekle(gorevler)

    elif secim == "2":
        gorevleri_listele(gorevler)

    elif secim == "3":
        gorev_analizi(gorevler)

    elif secim == "4":
        print("Programdan çıkıldı.")
        break