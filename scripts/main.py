import pandas as pd

df_train = pd.read_csv("data/dataset/train.csv")
df_test = pd.read_csv("data/dataset/test.csv")

X = df_train[['Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']]
Y = df_train["Survived"]


print("> Train Dataset - Counting missing values over {} examples".format(len(X)))
print(X.isnull().sum())

print("> Ground Truth - Are there missing values?")
print(("no" , "yes")[int(Y.isnull().sum() > 0)])

print("> Test Dataset - Counting missing values over {} examples".format(len(df_test)))
print(df_test.isnull().sum())