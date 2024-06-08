###############################################
# Python Alıştırmalar
###############################################

###############################################
# GÖREV 1: Veri yapılarının tipleriniz inceleyiniz.
###############################################

x = 8


y = 3.2


z = 8j + 18


a = "Hello World"


b = True


c = 23 < 22



l = [1, 2, 3, 4,"String",3.2, False]



d = {"Name": "Jake",
     "Age": [27,56],
     "Adress": "Downtown"}


t = ("Machine Learning", "Data Science")



s = {"Python", "Machine Learning", "Data Science","Python"}

###############################################
# CEVAP 1: Veri yapılarının tipleri
###############################################
def type_of_var(var):
    print(type(var))

type_of_var(x)
type_of_var(y)
type_of_var(z)
type_of_var(a)
type_of_var(b)
type_of_var(c)
type_of_var(l)
type_of_var(d)
type_of_var(t)
type_of_var(s)


###############################################
# GÖREV 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
###############################################

text = "The goal is to turn data into information, and information into insight."

###############################################
# CEVAP 2: Harf büyütme ve nokta-virgül düzenleme
###############################################

print(text.upper().replace(","," ").replace("."," ").split())

###############################################
# GÖREV 3: Verilen liste için aşağıdaki görevleri yapınız.
###############################################

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

# Adım 1: Verilen listenin eleman sayısına bakın.


# Adım 2: Sıfırıncı ve onuncu index'teki elemanları çağırın.


# Adım 3: Verilen liste üzerinden ["D","A","T","A"] listesi oluşturun.


# Adım 4: Sekizinci index'teki elemanı silin.


# Adım 5: Yeni bir eleman ekleyin.



# Adım 6: Sekizinci index'e  "N" elemanını tekrar ekleyin.

###############################################
# CEVAP 3: Verilen liste için aşağıdaki görevleri yapınız.
###############################################

print(len(lst))
print(lst[0],lst[10])
print(lst[:4])
print(lst.pop(8))
print(lst.append("<3"))
print(lst.insert(8,"N"))

###############################################
# GÖREV 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
###############################################

dict = {'Christian': ["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}


# Adım 1: Key değerlerine erişiniz.



# Adım 2: Value'lara erişiniz.



# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.



# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.



# Adım 5: Antonio'yu dictionary'den siliniz.

###############################################
# CEVAP 5: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
###############################################

print(dict.keys())
print(dict.values())
dict["Daisy"][1] = 13
print(dict)
dict["Ahmet"] = ["Turkey",24]
print(dict)
dict.pop("Antonio")
print(dict)


###############################################
# GÖREV 5: Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atıyan ve bu listeleri return eden fonskiyon yazınız.
###############################################

l = [2,13,18,93,22]

###############################################
# GÖREV 5: Liste fonksiyonu
###############################################

def is_odd_or_even(lst):
        odd, even = [], []
        for i in lst:
                if i % 2 == 0:
                        even.append(i)
                else:
                        odd.append(i)
        return odd, even

###############################################
# GÖREV 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
###############################################

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

###############################################
# CEVAP 6: Öğrenci sıralama
###############################################

for ogrencı in enumerate(ogrenciler,1):
        if ogrencı[0] <= 3:
                print("Mühendislik Fakültesi: ", ogrencı[1])
        else:
                print("Tıp Fakültesi: ", ogrencı[1])
       


###############################################
# GÖREV 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.
###############################################

ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

###############################################
# CEVAP 7: Ders bilgileri
###############################################

for ders in zip(ders_kodu,kredi,kontenjan):
        print(ders)



###############################################
# GÖREV 8: Aşağıda 2 adet set verilmiştir.
# Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
###############################################

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

###############################################
# CEVAP 8: Küme fonksiyonu
###############################################

def is_subset(kume1,kume2):
        if kume1.issubset(kume2):
                return kume2
        else:
                return kume2.difference(kume1)



