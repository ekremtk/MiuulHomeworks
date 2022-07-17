# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("titanic")
df.head()
df.info()

# Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.

print("Number of Male Passengers: ", df["sex"].value_counts()[0])
print("Number of Female Passengers: ", df["sex"].value_counts()[1])

# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.

i = len(df.columns)
a = i

for col in df.columns:
    print("Column Name: ", df.columns[i - a], " - Number of Unique Values: ", df[col].nunique())
    a -= 1
    print("*******************************************************************************")

# Görev 4: pclass değişkeninin unique değerlerinin sayısını bulunuz.
print("Number of Unique Values: ", df["pclass"].nunique())

# Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
listToSearch = ["pclass", "parch"]
df[listToSearch].nunique()

# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.
print("Type of 'embarked' object is: ", df["embarked"].dtype)
df["embarked"] = df["embarked"].astype('category')
print("Type of 'embarked' object is: ", df["embarked"].dtype)

# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
print("Embarked değeri C olanların tüm bilgileri")
df[df["embarked"] == "C"]

# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
print("Embarked değeri S olmayanların tüm bilgileri")
df[df["embarked"] != "S"]

# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
print("Yaşı 30'dan büyük olan ve kadın olan yolcuların tüm bilgileri")
df[(df["age"] > 30) & (df["sex"] == "female")]

# Görev 10: Fare'i 500'den büyük veya yaşı 70’den büyük yolcuların bilgilerini gösteriniz.
print("Fare değeri 500'den büyük olan veya yaşı 70'den büyük olan yolcuların tüm bilgileri")
df[(df["fare"] > 500) | (df["age"] > 70)]

# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
print(df.isnull().sum())

# Görev 12: who değişkenini dataframe’den çıkarınız.
df.drop("who", axis=1)

# Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
df["deck"].fillna(df["deck"].mode().iloc[0], inplace=True)

# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurunuz.
df["age"].fillna(df["age"].median(), inplace=True)

# Görev 15: survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
df.groupby(["pclass", "sex"]).agg({"survived": ["sum", "count", "mean"]})

# Görev 16: 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 verecek bir fonksiyon yazın.
#               Yazdığınız fonksiyonu kullanarak titanik veri
#                   setinde age_flag adında bir değişken oluşturunuz oluşturunuz.
#                   (apply ve lambda yapılarını kullanınız)
age_col = df["age"].apply(lambda x: 1 if x < 30 else 0)
df["age_col"] = age_col
df.head()

# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
df2 = sns.load_dataset("tips")
df2.head()

# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerinin sum, min, max ve mean değerlerini bulunuz.
df2.groupby(["time"]).agg({"total_bill": ["sum", "min", "max"]})

# Görev 19: Day ve time’a göre total_bill değerlerinin sum, min, max ve mean değerlerini bulunuz.
df2.groupby(["day", "time"]).agg({"total_bill": ["sum", "min", "max"]})

# Görev 20: Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre sum, min, max ve mean değerlerini bulunuz.
df2[(df2["time"] == "Lunch") & (df2["sex"] == "Female")].groupby(["day"]).agg(
    {"total_bill": ["sum", "min", "max", "mean"],
     "tip": ["sum", "min", "max", "mean"]})

# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)
df2.loc[(df2["size"] < 3) & (df2["total_bill"] > 10)].mean()

# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
df2["total_bill_tip_sum"] = df2["total_bill"] + df2["tip"]

# Görev 23: Total_bill değişkeninin kadın ve erkek için ayrı ayrı ortalamasını bulunuz.
#               Bulduğunuz ortalamaların altında olanlara 0,
#                   üstünde ve eşit olanlara 1 verildiği yeni bir total_bill_flag değişkeni oluşturunuz.
#               Kadınlar için Female olanlarının ortalamaları, erkekler için ise Male olanların ortalamaları dikkate alınacktır.
#               Parametre olarak cinsiyet ve total_bill alan bir fonksiyon yazarak başlayınız. (If-else koşulları içerecek)
female_mean = df2.groupby("sex").total_bill.mean()[0]
male_mean = df2.groupby("sex").total_bill.mean()[1]


def total_bill_flag(gender, total_bill):
    if gender == "Female" and total_bill < female_mean:
        return 0
    elif gender == "Female" and total_bill >= female_mean:
        return 1
    elif gender == "Male" and total_bill < male_mean:
        return 0
    elif gender == "Male" and total_bill >= male_mean:
        return 1


df2["total_bill_flag"] = df2.apply(lambda x: total_bill_flag(x.sex, x.total_bill), axis=1)
print(df2.head())

# Görev 24: total_bill_flag değişkenini kullanarak cinsiyetlere göre ortalamanın altında ve üstünde olanların sayısını gözlemleyiniz.
df2.groupby(["sex", "total_bill_flag"]).total_bill_flag.count()

# Görev 25: Veriyi total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
df2.sort_values("total_bill_tip_sum", ascending=False)
df2_new = df2.sort_values("total_bill_tip_sum", ascending=False)[:30]
