######################---Görev 1---######################
# Görev 1 : Keşifçi Veri Analizi
######################---Görev 1---######################

# Import Libraries etc.

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

import missingno as msno
from datetime import date
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import LocalOutlierFactor
from sklearn.preprocessing import MinMaxScaler, LabelEncoder, StandardScaler, RobustScaler

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 500)


######################---Görev 1---######################
# Adım 1: Genel resmi inceleyiniz.
######################---Görev 1---######################

def load():
    data = pd.read_csv("Module#3_FeatureEngineering/datasets/diabetes.csv")
    return data


def check_df(dataframe, head=5):
    print("##################### Dataset Shape #####################")
    print(dataframe.shape)
    print("##################### Dataset Detailed Information #####################")
    print(dataframe.info())
    print("##################### Data Types #####################")
    print(dataframe.dtypes)
    print("##################### Head (First 5 Values in Data) #####################")
    print(dataframe.head(head))
    print("##################### Tail (Last 5 Values in Data) #####################")
    print(dataframe.tail(head))
    print("##################### NA (Sum of NA Datas) #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)


df = load()  # Dataset Load
check_df(df)  # Getting Information about dataset with using function

######################---Görev 1---######################
# Adım 2: Numerik ve kategorik değişkenleri yakalayınız.
######################---Görev 1---######################

# Categorical Columns
cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

# Numerical Columns
num_cols = [col for col in df.columns if df[col].dtypes in ["int64", "float64"]]

# Numerical but actually categorical columns
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]


######################---Görev 1---######################
# Adım 3: Numerik ve kategorik değişkenlerin analizini yapınız.
######################---Görev 1---######################

# Categorical Variable Analysis
def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)


# Apply on All Categorical Variables
for col in cat_cols:
    if df[col].dtypes == "bool":
        print("Category: ", col, "\n There is not a figure for this category because of it is a boolean type")
    else:
        cat_summary(df, col, plot=True)


# Numerical Variable Analysis
def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    # If Plot == True, Plot a histogram graph, write a title and axis label
    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)


# Apply on All Numerical Variables
for col in num_cols:
    num_summary(df, col, plot=True)


######################---Görev 1---######################
# Adım 4: Hedef değişken analizi yapınız.
# (Kategorik değişkenlere göre hedef değişkenin ortalaması, hedef değişkene göre numerik değişkenlerin ortalaması)
######################---Görev 1---######################

# Target is "Outcome" variable

# Function for categorical analysis according to target
def target_summary_with_cat(dataframe, target, categorical_col):
    print(pd.DataFrame({"TARGET_MEAN": dataframe.groupby(categorical_col)[target].mean()}), end="\n\n\n")


# Apply on all categorical variables
for col in cat_cols:
    target_summary_with_cat(df, "Outcome", col)


# Function for numerical analysis according to target
def target_summary_with_num(dataframe, target, numerical_col):
    print(dataframe.groupby(target).agg({numerical_col: "mean"}), end="\n\n\n")


# Apply on all numerical variables
for col in num_cols:
    target_summary_with_num(df, "Outcome", col)

######################---Görev 1---######################
# Adım 5: Aykırı gözlem analizi yapınız.
######################---Görev 1---######################

# Checking all outliers in the dataset with boxplot
for col in df.columns:
    sns.boxplot(x=df[col])
    plt.show(block=True)


# Find Outliers with function
def outlier_thresholds(dataframe, col_name, q1=0.25, q3=0.75):
    quartile1 = dataframe[col_name].quantile(q1)  # Q1'i Hesapla
    quartile3 = dataframe[col_name].quantile(q3)  # Q3 Hesapla
    interquantile_range = quartile3 - quartile1  # IQR Hesapla
    up_limit = quartile3 + 1.5 * interquantile_range  # Üst Limit
    low_limit = quartile1 - 1.5 * interquantile_range  # Alt Limit
    return low_limit, up_limit


# Check if there is an outlier or not
def check_outlier(dataframe, col_name):
    low_limit, up_limit = outlier_thresholds(dataframe, col_name)
    if dataframe[(dataframe[col_name] > up_limit) | (dataframe[col_name] < low_limit)].any(axis=None):
        return True
    else:
        return False


for col in df.columns:
    print(col, check_outlier(df, col))

clf = LocalOutlierFactor(n_neighbors=20)
clf.fit_predict(df)

######################---Görev 1---######################
# Adım 6: Eksik gözlem analizi yapınız.
######################---Görev 1---######################

# Check if there is any missing value
df.isnull().values.any()


# If there is a missing values catch it and calcule it's ratio with a Function
def missing_values_table(dataframe, na_name=False):
    na_columns = [col for col in dataframe.columns if dataframe[col].isnull().sum() > 0]

    n_miss = dataframe[na_columns].isnull().sum().sort_values(ascending=False)
    ratio = (dataframe[na_columns].isnull().sum() / dataframe.shape[0] * 100).sort_values(ascending=False)
    missing_df = pd.concat([n_miss, np.round(ratio, 2)], axis=1, keys=['n_miss', 'ratio'])
    print(missing_df, end="\n")

    if na_name:
        return na_columns


missing_values_table(df, True)

######################---Görev 1---######################
# Adım 7: Korelasyon analizi yapınız.
######################---Görev 1---######################

# Corelation Analysis
corr = df[num_cols].corr()

# Visualize the correlation result on the heatmap
sns.set(rc={'figure.figsize': (12, 12)})
sns.heatmap(corr, cmap="RdBu")
plt.show(block=True)

# First convert them to the positive values with absolute
cor_matrix = df.corr().abs()

# Then create an empty numpy matrix and fill with True/False
upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(bool))
# If the correlation higher than %90 put them into the dropping list
drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > 0.90)]

cor_matrix[drop_list]

# Drop Them from the list
df.drop(drop_list, axis=1)


# Make it with a function
def high_correlated_cols(dataframe, plot=False, corr_th=0.90):
    corr = dataframe.corr()
    cor_matrix = corr.abs()
    upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(bool))
    drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > corr_th)]
    if plot:
        import seaborn as sns
        import matplotlib.pyplot as plt
        sns.set(rc={'figure.figsize': (15, 15)})
        sns.heatmap(corr, cmap="RdBu")
        plt.show(block=True)
    return drop_list


high_correlated_cols(df)
# First trial with the correlation ratio %90
# drop_list = high_correlated_cols(df, plot=True)
drop_list = high_correlated_cols(df, plot=True, corr_th=0.25)
df.drop(drop_list, axis=1)
high_correlated_cols(df.drop(drop_list, axis=1), plot=True)
