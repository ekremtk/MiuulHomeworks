"""
Fonksiyonlara Özellik Eklemek

Görev: cat_summary() fonksiyonuna 1 özellik ekleyiniz.
Bu özellik argümanla biçimlendirilebilir olsun.
Var olan özelliği de argümanla kontrol edilebilir hale getirebilirsiniz.

sns.countplot(x=dataframe["embarked"], data=dataframe)
        plt.show(block=True)
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

df.info()

"""
function_name = cat_summary
args = dataframe, column_name
optional = plot type
  1 for countplot
  2 for distplot
  3 for piechart
Goal = Find number of values and calculate the ratio
"""


def cat_summary(dataframe, col_name, plot=0):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

    if (plot == 1):
        sns.countplot(x=dataframe[col_name], data=dataframe).set(title="CountPlot")
        plt.show(block=True)
    elif (plot == 2):
        sns.displot(x=dataframe[col_name], data=dataframe).set(title="DistPlot")
        plt.show(block=True)
    elif (plot == 3):
        plt.pie(x=dataframe[col_name].value_counts(), labels=list(dataframe[col_name].unique()))
        plt.show()
    else:
        pass

cat_summary(df, "sex", plot=3)