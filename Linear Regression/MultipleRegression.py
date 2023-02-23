import numpy as np
import pandas
from sklearn import linear_model

df = pandas.read_csv("cars.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

#print(y)

regr = linear_model.LinearRegression()
regr.fit(X, y)

# predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])

print("Predicted CO2 level for Weight and Volume")
print(predictedCO2)

X1 = df['Weight']
#print("Dumping X1")
#print(X1)
X1 = np.array(X1)
# y = df['CO2']

X1 = X1.reshape((-1, 1))
regr2 = linear_model.LinearRegression()
regr2.fit(X1, y)

predictedCO22 = regr2.predict([[2300]])

print("Dumping CO2 Model2")
print(predictedCO22)


