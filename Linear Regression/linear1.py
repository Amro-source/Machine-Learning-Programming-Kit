import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [3,5,7,10] # 10, not 9, so the fit isn't perfect

coef = np.polyfit(x,y,1)
print(coef)
poly1d_fn = np.poly1d(coef)
# poly1d_fn is now a function which takes in x and returns an estimate for y

#plt.plot(x,y, 'yo', x, poly1d_fn(x), '--k')

plt.plot(x,y)
#'--k'=black dashed line, 'yo' = yellow circle marker

plt.xlim(0, 5)
plt.ylim(0, 12)