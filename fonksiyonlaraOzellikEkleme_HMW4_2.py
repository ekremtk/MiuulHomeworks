"""
Docstring Yazımı
Görev: check_df(), cat_summary() fonksiyonlarına 4 bilgi (uygunsa)
barındıran numpy tarzı docstring yazınız.
(task, params, return, example)
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def check_df(dataframe, head=5):
    """
    Veri seti hakkında en genel bilgileri verir.

    Parameters
    ----------
    dataframe:  dataframe
        Hakkında bilgi edinilmek istenen dataframe'dir.

    head: int
        Sınır için sayısal değer

    Returns
    -------
        Dataframe ait boyut, veri tipi, en baştan itibaren sınır değer miktar kadar veriler,
        en sondan itibaren sınır değer miktar kadar veriler,
        boş değerlerin toplamı, verilerin özet sayısal değerleri ekranda ayrı ayrı gösterilir

    """
    print("##################### Shape #########################")
    print(dataframe.shape)
    print("##################### Types #########################")
    print(dataframe.dtypes)
    print("##################### Head ##########################")
    print(dataframe.head(head))
    print("##################### Tail ##########################")
    print(dataframe.tail(head))
    print("##################### NA ############################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)

# 1.arg = df, 2.arg = col name
# Kendisine girilenlerin hangi sınıfta kaç tane var
# Sınıfların yüzdelik bilgisini alsın
def cat_summary(dataframe, col_name, plot=False):
    """
    Veri setindeki ilgili sınıftaki değerlerin sayımı ve oranı
    Ayrıca istenirse grafik çizimi yapılır

    Parameters
    ----------
    dataframe:  dataframe
        Hakkında bilgi edinilmek istenen dataframe'dir.

    col_name: string
        Dataframedeki sütun ismidir

    plot: Boolen
        Grafik çizim seçeneğidir. Varsayılan olarak false değeri vardır

    Returns
    -------
        İlgili değişkenin sayıları ve oranı
        Aktif edilirse grafiği

    """
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("####################################################################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)