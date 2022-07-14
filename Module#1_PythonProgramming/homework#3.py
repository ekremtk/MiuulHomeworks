# Gorev 1: Verilen değerlerin veri yapılarını inceleyiniz

x = 8
y = 3.2
z = 8j + 18
a = "Hello World"
b = True
c = 23 < 22
l = [1, 2, 3, 4]
d = {"Name": "Jake",
     "Age": "27",
     "Adress": "Downtown"}
t = {"Machine Learning", "Data Science"}
s = {"Python", "Machine Learning", "Data Science"}

type(x)   # int
type(y)   # float
type(z)   # complex
type(a)   # str
type(b)   # bool
type(c)   # bool
type(l)   # list
type(d)   # dict
type(t)   # set
type(s)   # set

###################################################################

# Gorev 2:  Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
text = "The goal is to turn data into information, and information into insight"

text = text.upper()
text = text.replace(",", " ")
text = text.replace(".", " ")
text = text.split()

###################################################################
# Görev 3:  Verilen listeye aşağıdaki adımları uygulayınız.

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# Adım1: Verilen listenin eleman sayısına bakınız.
number_of_elements = len(lst)

# Adım2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
lst[0]
lst[10]

# Adım3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
newlist = lst[0:4]

# Adım4: Sekizinci indeksteki elemanı siliniz.
lst.remove(lst[8])

# Adım5: Yeni bir eleman ekleyiniz.
lst.append("Q")

# Adım6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.
lst.insert(8, "N")

###################################################################
# Görev 4:  Verilen sözlük yapısına aşağıdaki adımları uygulayınız.

dict = {"Christian": ["America", 18],
        "Daisy": ["England", 12],
        "Antonio": ["Spain", 22],
        "Dante": ["Italy", 25]}

# Adım1: Key değerlerine erişiniz.
dict.keys()

# Adım2: Value'lara erişiniz.
dict.values()

# Adım3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
dict["Daisy"] = ["England", 13]

# Adım4: Key değeri Ahmet value değeri[Turkey,24] olan yeni bir değer ekleyiniz.
dict["Ahmet"] = ["Turkey", 24]

# Adım5: Antonio'yu dictionary'den siliniz.
dict.pop("Antonio")

###################################################################

# Görev 5:Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri return eden fonksiyon yazınız.
# Liste elemanlarına tek tek erişmeniz gerekmektedir.
# Her bir elemanın çift veya tek olma durumunu kontrol etmek için  % yapısını kullanabilirsiniz.

list = [2, 13, 18, 93, 22]

def checknums(numlist):
     even_list = []
     odd_list = []
     for num in numlist:
          if num % 2 == 0:
               even_list.append(num)
          else:
               odd_list.append(num)
     return even_list, odd_list

even_list, odd_list = checknums(list)

###################################################################

# Görev 6:  List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyükharfe çeviriniz ve başına NUM ekleyiniz.

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

df.columns = ["NUM_" + col.upper() for col in df.columns]


###################################################################

# Görev 7:  List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan değişkenlerin isimlerinin sonuna "FLAG" yazınız.

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

df.columns = [col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]

###################################################################

# Görev 8:  List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz
# ve yeni bir data frame oluşturunuz

# İpucu:
# Önce verilen listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
# Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz ve
# adını new_df olarak isimlendiriniz.

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

og_list = ["abbrev", "no_previous"]

new_cols = [col for col in df.columns if col not in og_list]

new_df = df[new_cols]
new_df.head()
