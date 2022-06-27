import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def marks_prediction(hrs):
    X = pd.read_csv('Linear_X_Train.csv')
    y = pd.read_csv('Linear_Y_Train.csv')
    X = X.values
    y = y.values

    model = LinearRegression()
    model.fit(X, y)

    X_test = np.array(hrs).reshape((1,-1))

    return model.predict(X_test)[0]

