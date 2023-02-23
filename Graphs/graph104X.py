import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data.csv')

# print(df.to_string())

print(df)
print(df.head(10))

print(df.tail())

print(df.info())

Calories =df["Calories"]

Maxpulse =df["Maxpulse"]

X = df["Duration"]

#df["Calories"].fillna(130, inplace = True)

# print(X)

Y = df["Pulse"]

X1 = np.array(X)
Y1 = np.array(Y)


t1 =np.arange(start=1, stop=X1.size+1, step=1)

plt.plot(t1, Y1)
plt.title("Sports Watch Data")
plt.xlabel("time ")
plt.ylabel("Pulse")


plt.show()


plt.show()

plt.plot(t1, X1)
plt.title("Sports Watch Data")
plt.xlabel("time ")
plt.ylabel("Duration")

plt.show()


plt.plot(Y1, marker = 'o')
plt.title("Sports Watch Data")
plt.xlabel("time ")
plt.ylabel("Pulse")


plt.show()

plt.plot(Calories, marker = 'o')
plt.title("Sports Watch Data")
plt.xlabel("time ")
plt.ylabel("Calories")


plt.show()

plt.plot(Maxpulse, marker = 'o')
plt.title("Sports Watch Data")
plt.xlabel("time ")
plt.ylabel("Maxpulse")


plt.show()

plt.bar(t1,Maxpulse)
plt.show()


feature =df[['Duration','Calories','Maxpulse']]

# plt.bar(t1,XYZ)
# plt.show()


