import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
import warnings
warnings.filterwarnings('ignore')

sample_data = pd.read_csv("Corona.csv")
sample_data.head()

features=["Temperature","BodyPain","Age","RunnyNose","DiffBreath","TravelledZone","OtherDisease"]
target=["Infected"]

X_train,X_test,Y_train,Y_test=train_test_split(sample_data[features],sample_data[target],test_size=0.3)

model=LogisticRegression()
model.fit(X_train,Y_train)

model.score(X_train,Y_train)

file = open('model.pkl', 'wb')
pickle.dump(model, file)
file.close()