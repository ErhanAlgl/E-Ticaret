import getpass
import datetime
import sys

auth = {'ahmet':'sehir123', 'meryem':'4444'}

envanter = {'kuşkonmaz':[10,5],'brokoli':[15,6],'havuç':[18,7],
           'elma':[20,5],'muz':[10,8],'çilek':[30,3],
           'yumurta':[50,2],'karışık meyve suyu':[0,8],'balık kroket':[25,12],
           'dondurma':[32,6], 'elma suyu':[40,7], 'portakal suyu':[30,8],   
           'üzüm suyu':[10,9]}

sepet = {}
username = None

def login():
    global username
    print("**** Şehir Online Markete Hoşgeldiniz ****")
    print("Lütfen kullanıcı bilgilerini yazarak giriş yapın: ")
    user = input('Kullanıcı adı: ')
    password = getpass.getpass('Şifre : ')
    try:
        if auth[user] == password:
            print("Başarıyla giriş yapıldı!")
            username = user
            if username not in sepet:
                sepet[username] = {}
            return True
    except:
        print('Kullanıcı adınız ve/veya şifreniz doğru değil. Lütfen tekrar deneyin!')
        return False


def sepeti_goster():
    toplam = 0
    if sepet[username]:
        print('Sepetinizdekiler:')
        for i, j in enumerate(sepet[username]):
            print('{}.{} fiyat={} TL miktar={} toplam={} TL'.format(i + 1, j, envanter[j][0], sepet[username][j],
                                                                    envanter[j][0] * sepet[username][j]))
            toplam += envanter[j][0] * sepet[username][j]
        print("\nToplam\t{} TL".format(toplam))
    else:
        print('Sepetiniz boş. Sepetinizdeki öğelerin toplam fiyatı 0 TL')
        main()


def odeme():
    global sepet, username
    toplam = 0
    print("""
    Makbuz işleniyor...

    ******* Sehir Online Market ********
    ************************************
	        44 44 0 34
	        sehir.edu.tr
    """)
    print('-'*36)
    for i, j in enumerate(sepet[username]):
        print('{}.{} fiyat={} TL miktar={} toplam={} TL'.format(i+1, j, envanter[j][0], sepet[username][j],
                                                                envanter[j][0] * sepet[username][j]))
        toplam += envanter[j][0] * sepet[username][j]
        envanter[j][1] -= sepet[username][j]
    print('-' * 36)
    print("Toplam\t{} TL".format(toplam))
    print('-' * 36)
    print(datetime.date.today())
    print('\nBizi tercih ettiğiniz için teşekkür ederiz!')
    sepet[username].clear()



def main_menu():
    wellcome_message = """
    Lütfen aşağıdaki hizmetlerden birini seçin: 
    1. Ürün arama
    2. Sepeti göster
    3. Ödeme
    4. Hesaptan çık
    5. Kapat\n\n\n\n\n
    """
    print(wellcome_message)
    while True:
        response = input("Seçiminiz: ")
        if int(response) in [1,2,3,4,5]:
            return int(response)
        else:
            print("Geçerli olmayan bir seçenek girdiniz!")


def search(word):
    global username
    urunler = []
    for urun in envanter:
        if word.lower() in urun and envanter[urun][1] > 0:
            urunler.append(urun)
    if len(urunler) != 0:
        print(len(urunler), 'benzer ürün bulundu:')
        for i, j in enumerate(urunler):
            print(i+1, j, envanter[j][0], ' TL')
        select = input('Lütfen sepetinize eklemek istediğiniz öğeyi seçin(ana menü için 0 girin):')
        if int(select) == 0:
            print('Ana menüye dönülüyor...')
            main()
        elif int(select) > len(urunler) or int(select) < 0:
            print('Hatalı giriş yaptınız!')
        else:
            urun = urunler[int(select)-1] 
            print(urun, 'eklenecek.')
            while True:
                miktar = input('Miktarı girin:')
                print(sepet)
                if int(miktar) <= envanter[urun][1]:
                    print('Sepetinize {} {} eklendi.'.format(miktar, urun))
                    sepet[username][urun] = int(miktar)
                    main()
                    break
                else:
                    print('Üzgünüz! Miktar, limiti aşıyor. Lütfen daha az bir miktarla tekrar deneyin')

    else:
        print('Hiçbir ürün bulunamadı!')
        option1()


def option1():
    word = input("Hangi ürünü arıyorsun? ")
    if word == "0":
        main()
    urunler = []
    for urun in envanter:
        if word.lower() in urun and envanter[urun][1] > 0:
            urunler.append(urun)
    if len(urunler) != 0:
        print(len(urunler), 'benzer ürün bulundu:\n')
        for i, j in enumerate(urunler):
            print(i + 1, j, envanter[j][0], ' TL')
        select = input('Lütfen sepetinize eklemek istediğiniz öğeyi seçin(ana menü için 0 girin):')
        if int(select) == 0:
            print('Ana menüye dönülüyor...')
            main()
        elif int(select) > len(urunler) or int(select) < 0:
            print('Hatalı giriş yaptınız!')
        else:
            urun = urunler[int(select) - 1]
            print(urun, 'eklenecek.')
            while True:
                miktar = input('Miktarı girin:')
                if int(miktar) <= envanter[urun][1]:
                    print('Sepetinize {} {} eklendi.'.format(miktar, urun))
                    sepet[username][urun] = int(miktar)
                    main()
                    break
                else:
                    print('Üzgünüz! Miktar, limiti aşıyor. Lütfen daha az bir miktarla tekrar deneyin')

    else:
        print('Aramanız hiçbir öğeyle eşleşmedi. Lütfen başka bir kelime deneyin (Ana menü için 0 girin)')
        option1()


def sub_menu():
    print("""
    Lütfen bir işlem seçiniz:
	1.Ürün miktarı güncelle
	2.Bir ürünü sil
	3.Ödemeye geç
	4.Ana menüye dön
	""")
    select = input('Seçiminiz: ')
    if int(select) == 1:
        while True:
            urun_numarasi = int(input('Lütfen miktarını değiştirmek istediğiniz ürünü seçin:'))
            if 0 < int(urun_numarasi) <= len(sepet[username]):
                urun_miktari = int(input('Lütfen yeni miktarı yazın: '))
                sepet[username][list(sepet[username])[urun_numarasi-1]] = urun_miktari
                sepeti_goster()
                sub_menu()
                break
            else:
                print('Liste dışında bir giriş yaptınız!')
    elif int(select) == 2:
        urun_numarasi = int(input('Lütfen silmek istediğiniz ürünü seçin:'))
        sepet[username].pop(list(sepet[username])[urun_numarasi-1])
        sepeti_goster()
        sub_menu()
    elif int(select) == 3:
        odeme()
        main()
    elif int(select) == 4:
        main()


def option2():
    if sepet:
        sepeti_goster()
        main()
    else:
        print('Sepetiniz boş. Sepetinizdeki öğelerin toplam fiyatı 0 TL')
        main()




def optionmenu(option):
    if option == 1:
        word = input("Hangi ürünü arıyorsun? ")
        search(word)
    elif option == 2:
        if sepet[username]:
            sepeti_goster()
            sub_menu()
        else:
            print('Sepetiniz boş. Sepetinizdeki öğelerin toplam fiyatı 0 TL')
            main()
    elif option == 3:
        odeme()
    elif option == 4:
        while True:
            if login():
                break
            print('Hoşgeldin {}! Lüfen ilgili menü numarasını girerek aşağıdaki seçeneklerden birini seçin.'.format(username))
        main()
    else:
        sys.exit()



def main():
    option = main_menu()
    optionmenu(option)



if __name__ == '__main__':
    while True:
        if login():
            break
    print('Hoşgeldin {}! Lüfen ilgili menü numarasını girerek aşağıdaki seçeneklerden birini seçin.'.format(username))
    main()