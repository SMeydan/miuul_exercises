
#############################################
# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama
#############################################

#############################################
# İş Problemi
#############################################
# Bir oyun şirketi müşterilerinin bazı özelliklerini kullanarak seviye tabanlı (level based) yeni müşteri tanımları (persona)
# oluşturmak ve bu yeni müşteri tanımlarına göre segmentler oluşturup bu segmentlere göre yeni gelebilecek müşterilerin şirkete
# ortalama ne kadar kazandırabileceğini tahmin etmek istemektedir.

# Örneğin: Türkiye’den IOS kullanıcısı olan 25 yaşındaki bir erkek kullanıcının ortalama ne kadar kazandırabileceği belirlenmek isteniyor.


#############################################
# Veri Seti Hikayesi
#############################################
# Persona.csv veri seti uluslararası bir oyun şirketinin sattığı ürünlerin fiyatlarını ve bu ürünleri satın alan kullanıcıların bazı
# demografik bilgilerini barındırmaktadır. Veri seti her satış işleminde oluşan kayıtlardan meydana gelmektedir. Bunun anlamı tablo
# tekilleştirilmemiştir. Diğer bir ifade ile belirli demografik özelliklere sahip bir kullanıcı birden fazla alışveriş yapmış olabilir.

# Price: Müşterinin harcama tutarı
# Source: Müşterinin bağlandığı cihaz türü
# Sex: Müşterinin cinsiyeti
# Country: Müşterinin ülkesi
# Age: Müşterinin yaşı

################# Uygulama Öncesi #####################

#    PRICE   SOURCE   SEX COUNTRY  AGE
# 0     39  android  male     bra   17
# 1     39  android  male     bra   17
# 2     49  android  male     bra   17
# 3     29  android  male     tur   17
# 4     49  android  male     tur   17

################# Uygulama Sonrası #####################

#       customers_level_based        PRICE SEGMENT
# 0   BRA_ANDROID_FEMALE_0_18  1139.800000       A
# 1  BRA_ANDROID_FEMALE_19_23  1070.600000       A
# 2  BRA_ANDROID_FEMALE_24_30   508.142857       A
# 3  BRA_ANDROID_FEMALE_31_40   233.166667       C
# 4  BRA_ANDROID_FEMALE_41_66   236.666667       C


#############################################
# PROJE GÖREVLERİ
#############################################

#############################################
# GÖREV 1: Aşağıdaki soruları yanıtlayınız.
#############################################

# Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.

import pandas as pd

persona = pd.read_csv("persona.csv")

persona.head()
persona.info()
persona.describe().T

# Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?

print(persona["SOURCE"].nunique())

# Soru 3: Kaç unique PRICE vardır?

print(persona["PRICE"].nunique())

# Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?

print(persona["PRICE"].value_counts())

# Soru 5: Hangi ülkeden kaçar tane satış olmuş?

print(persona["PRICE"].groupby(persona["COUNTRY"]).agg("count"))    

# Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?

print(persona["PRICE"].groupby(persona["COUNTRY"]).agg("sum"))

# Soru 7: SOURCE türlerine göre göre satış sayıları nedir?

print(persona["PRICE"].groupby(persona["SOURCE"]).agg("count"))

# Soru 8: Ülkelere göre PRICE ortalamaları nedir?

print(persona["PRICE"].groupby(persona["COUNTRY"]).agg("mean"))

# Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?

print(persona["PRICE"].groupby(persona["SOURCE"]).agg("mean"))

# Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?

print(persona["PRICE"].groupby([persona["COUNTRY"], persona["SOURCE"]]).agg("mean"))

#############################################
# GÖREV 2: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
#############################################

print(persona["PRICE"].groupby([persona["COUNTRY"], persona["SOURCE"], persona["SEX"], persona["AGE"]]).agg("mean"))

#############################################
# GÖREV 3: Çıktıyı PRICE'a göre sıralayınız.
#############################################
# Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE'a uygulayınız.
# Çıktıyı agg_df olarak kaydediniz.

agg_df = persona["PRICE"].groupby([persona["COUNTRY"], persona["SOURCE"], persona["SEX"], persona["AGE"]]).agg("mean")
print(agg_df.sort_values(ascending=False))

#############################################
# GÖREV 4: Indekste yer alan isimleri değişken ismine çeviriniz.
#############################################
# Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir.
# Bu isimleri değişken isimlerine çeviriniz.
# İpucu: reset_index()
# agg_df.reset_index(inplace=True)

agg_df = agg_df.reset_index()
print(agg_df)

#############################################
# GÖREV 5: AGE değişkenini kategorik değişkene çeviriniz ve agg_df'e ekleyiniz.
#############################################
# Age sayısal değişkenini kategorik değişkene çeviriniz.
# Aralıkları ikna edici olacağını düşündüğünüz şekilde oluşturunuz.
# Örneğin: '0_18', '19_23', '24_30', '31_40', '41_70'

bins = [0, 18, 23, 30, 40, 70]
labels = ['0_18', '19_23', '24_30', '31_40', '41_70']

agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], bins=bins, labels=labels)
print(agg_df)

#############################################
# GÖREV 6: Yeni level based müşterileri tanımlayınız ve veri setine değişken olarak ekleyiniz.
#############################################
# customers_level_based adında bir değişken tanımlayınız ve veri setine bu değişkeni ekleyiniz.
# Dikkat!
# list comp ile customers_level_based değerleri oluşturulduktan sonra bu değerlerin tekilleştirilmesi gerekmektedir.
# Örneğin birden fazla şu ifadeden olabilir: USA_ANDROID_MALE_0_18
# Bunları groupby'a alıp price ortalamalarını almak gerekmektedir.

agg_df["customers_level_based"] = [agg_df["COUNTRY"][i].upper() + "_" + agg_df["SOURCE"][i].upper() + "_" + agg_df["SEX"][i].upper() + "_" + agg_df["AGE_CAT"][i].upper() for i in range(len(agg_df))]
print(agg_df)

new_agg_df = agg_df[["PRICE", "customers_level_based"]]
new_agg_df = new_agg_df["PRICE"].groupby(new_agg_df["customers_level_based"]).agg("mean")
print(new_agg_df)

#############################################
# GÖREV 7: Yeni müşterileri (USA_ANDROID_MALE_0_18) segmentlere ayırınız.
#############################################
# PRICE'a göre segmentlere ayırınız,
# segmentleri "SEGMENT" isimlendirmesi ile agg_df'e ekleyiniz,
# segmentleri betimleyiniz,

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
print(agg_df)

#############################################
# GÖREV 8: Yeni gelen müşterileri sınıflandırınız ne kadar gelir getirebileceğini tahmin ediniz.
#############################################
# 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?

unq_country = persona["COUNTRY"].unique()
print(unq_country)

predict = agg_df[agg_df["customers_level_based"] == "TUR_ANDROID_FEMALE_31_40"]
print(predict)

average_price = predict["PRICE"].mean()
segment = predict["SEGMENT"].values[0] if not predict.empty else None
print(average_price)
print(segment)

# 35 yaşında IOS kullanan bir Fransız kadını hangi segmente ve ortalama ne kadar gelir kazandırması beklenir?

predict = agg_df[agg_df["customers_level_based"] == "FRA_IOS_FEMALE_31_40"]
print(predict)

average_price = predict["PRICE"].mean()
segment = predict["SEGMENT"].values[0] if not predict.empty else None
print(average_price)
print(segment)

