import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_train = pd.read_csv("data/dataset/train.csv")

print("> Survivors and Dead count")
Outcome = df_train["Survived"]

total = len(Outcome)
survived = Outcome[Outcome == 1].count()
dead = total - survived

survived_perc = (survived / total) * 100
dead_perc = (dead / total) * 100
print ("Survived= {}% , Dead={}% (sum is {}) Out of {} example".format(np.round(survived_perc) , np.round(dead_perc) , survived_perc + dead_perc , total))

PClass = df_train["Pclass"]

print("> passengers % distribution by class")
PClass_counts = np.round((PClass.value_counts() / total)*100)
print(PClass_counts)

print("> Histogram dead vs class")
Surv_counts = PClass[Outcome == 1].value_counts().sort_index()
Dead_counts = PClass[Outcome == 0].value_counts().sort_index()

plt.bar((0 , 0.8 ,1.6) , Surv_counts.values , width=0.4 , label="survivors")
plt.bar((0 , 0.8 ,1.6) , Dead_counts.values , width=0.4 , label="dead" , bottom=Surv_counts.values)
plt.xticks((0 , 0.8 ,1.6)  , ('1st' , '2nd' , '3rd'))
plt.legend()
plt.show()