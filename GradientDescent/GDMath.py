#In linear regression, the model targets to get the best-fit regression line to predict the value of y based on
#the given input value (x). While training the model, the model calculates the cost function which measures the
#Root Mean Squared error between the predicted value (pred) and true value (y). The model targets to minimize
#the cost function.
#To minimize the cost function, the model needs to have the best value of θ1 and θ2. Initially model selects
#θ1 and θ2 values randomly and then iteratively update these value in order to minimize the cost function
#until it reaches the minimum. By the time model achieves the minimum cost function, it will have the best
#θ1 and θ2 values. Using these finally updated values of θ1 and θ2 in the hypothesis equation of linear
#Equation, the model predicts the value of x in the best manner it can.

#Therefore, the question arises – How do θ1 and θ2 values get updated?
#Linear Regression Cost Function:

import numpy as np

n =100


#J =1/n*np.sum(predi-yi)