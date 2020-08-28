import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_absolute_error

def getPoints(numOfPoints,std,degree,noise):
    x = np.linspace(0, 0.9, numOfPoints)
    eta, y = transformer(degree, noise, std, x)
    return x,eta,y


def transformer(degree, noise, std, x):
    eta = std * noise
    y = 2 * x ** degree + eta
    return eta, y


def plotPoints(x,y):
    plt.plot(x, y, '.', ms=5, label='Constructed Data')
    plt.show()


def fitPoly(x,y,deg):
    poly = PolynomialFeatures(degree=deg)
    X = poly.fit_transform(x[:, np.newaxis])
    lin = linear_model.LinearRegression()
    lin.fit(X, y)
    yPred = lin.predict(X)
    return yPred,lin,poly

def predictOut(lin,poly,yPred_in,y,degree):
    x_out=np.linspace(0.9,1, 15)
    noise = np.random.randn(15)
    eta, y_out = transformer(degree,noise,1,x_out)
    X_out = poly.transform(x_out[:, np.newaxis])
    yPred_out = lin.predict(X_out)
    return mean_absolute_error(y,yPred_in), mean_absolute_error(y_out,yPred_out), x_out, y_out, yPred_out



if __name__ == "__main__":
    numOfPoints = 100
    std = 1
    degree = 1
    x,eta,y = getPoints(numOfPoints,std, degree, np.random.randn())
    # plotPoints(x,y)
    yPred = fitPoly(x,y,2)
    # plotPoints(x,yPred)