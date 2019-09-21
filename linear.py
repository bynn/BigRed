import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest 
from sklearn.feature_selection import chi2 
from sklearn import preprocessing
from scipy import stats

df = pd.read_csv("random.csv")
# features we want to look at
features = ["Income", "Long","Lat","YOB","Gender","APL"]
#x = features
x = df.loc[:,features].values
#standarize features
scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
X = scaler.fit_transform(x)
#y = target
y = df.loc[:,['Accepted']].values

print(df.head())

test = SelectKBest(score_func=chi2, k="all")
fit = test.fit(X,y)
dfscores = pd.DataFrame(fit.scores_)
dfcolumns = pd.DataFrame(features)

scores = pd.concat([dfcolumns, dfscores], axis=1)
scores.columns = ["features","scores"]
print(scores)
