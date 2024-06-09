

##################################################
# Pandas Alıştırmalar
##################################################

import numpy as np
import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

#########################################
# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
#########################################

titanic = sns.load_dataset("titanic")

#########################################
# Görev 2: Yukarıda tanımlanan Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
#########################################

print(titanic["sex"].count())
print(titanic["sex"].value_counts())

#########################################
# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
#########################################

print(titanic.nunique())

#########################################
# Görev 4: pclass değişkeninin unique değerleri bulunuz.
#########################################

print(titanic["pclass"].unique())


#########################################
# Görev 5:  pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
#########################################

print(titanic[["pclass", "parch"]].nunique())

#########################################
# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz. Tekrar tipini kontrol ediniz.
#########################################

print(titanic["embarked"].dtypes)
titanic["embarked"] = titanic["embarked"].astype("category")
print(titanic["embarked"].dtypes)
titanic["embarked"] = titanic["embarked"].cat.codes

#########################################
# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
#########################################

print(titanic["embarked"].unique())
print(titanic["embarked"] == 0)
print(titanic[titanic["embarked"] == 0])


#########################################
# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
#########################################

print(titanic[titanic["embarked"] != 1])


#########################################
# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
#########################################

print(titanic[(titanic["age"] < 30) & (titanic["sex"] == "female")])

#########################################
# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
#########################################

print(titanic[(titanic["fare"] > 500) | (titanic["age"] > 70)])

#########################################
# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
#########################################

print(titanic.isnull().sum())


#########################################
# Görev 12: who değişkenini dataframe'den düşürün.
#########################################

print(titanic.drop("who", axis=1, inplace=False))

#########################################
# Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
#########################################

print(titanic["deck"].fillna(titanic["deck"].mode()[0], inplace=False))

#########################################
# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurun.
#########################################

print(titanic["age"].fillna(titanic["age"].median(), inplace=False))

#########################################
# Görev 15: survived değişkeninin Pclass ve Cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
#########################################

print(titanic["survived"].groupby([titanic["pclass"], titanic["sex"]]).agg(["sum", "count", "mean"]))   

#########################################
# Görev 16:  30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazınız.
# Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
#########################################

titanic["age_flag"] = titanic["age"].apply(lambda x: 1 if x < 30 else 0)

#########################################
# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
#########################################

tips = sns.load_dataset("tips")
print(tips.head())


#########################################
# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill  değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################

print(tips.groupby("time")["total_bill"].agg(["sum", "min", "max", "mean"]))

#########################################
# Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################

print(tips.groupby(["day", "time"])["total_bill"].agg(["sum", "min", "max", "mean"]))

#########################################
# Görev 20:Lunch zamanına ve kadın müşterilere ait total_bill ve tip  değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.
#########################################

print(tips[(tips["time"] == "Lunch") & (tips["sex"] == "Female")].groupby("day")[["total_bill", "tip"]].agg(["sum", "min", "max", "mean"]))

#########################################
# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir?
#########################################

fltrd_tips = tips.loc[(tips["size"] < 3) & (tips["total_bill"] > 10)]
print(fltrd_tips.mean(numeric_only=True))

#########################################
# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturun. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
#########################################

tips["total_bill_tip_sum"] = tips["total_bill"] + tips["tip"]

#########################################
# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
#########################################

new_df = tips.sort_values("total_bill_tip_sum", ascending=False).head(30)