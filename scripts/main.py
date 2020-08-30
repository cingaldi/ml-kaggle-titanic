import pandas as pd
import matplotlib.pyplot as plt

df_train = pd.read_csv("data/dataset/train.csv")
df_test = pd.read_csv("data/dataset/test.csv")

#Feature "Cabin" removed due to few non-missing values
#Feature "Age" removed because replacement with mean/median would bias data
X = df_train[['Pclass', 'Name', 'Sex', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Embarked']]
Y = df_train["Survived"]

print("> Train Dataset - Counting missing values over {} examples".format(len(X)))
print(X.isnull().sum())

print("> Ground Truth - Are there missing values?")
print(("no" , "yes")[int(Y.isnull().sum() > 0)])

print("> Test Dataset - Counting missing values over {} examples".format(len(df_test)))
print(df_test.isnull().sum())

#print("> Train Dataset - Checking distribution for feature 'Age'")
#plt.hist(X["Age"] , bins=80)
#plt.show()

print("> Replacing missing Values 'Embarked' feature")
X["Embarked"] = X["Embarked"].fillna(X["Embarked"].value_counts().index[0])

print("> Train Dataset - Counting missing values over {} examples".format(len(X)))
print(X.isnull().sum())


#-------------