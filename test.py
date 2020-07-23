import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

df = pd.read_csv('datafinal.csv')


x = df.iloc[: , -1].values
result = 0
values = []

for i in range(0,276):
    if(x[i] == 0):
        result = 0.5
    elif(x[i] < -2):
        result = 0
    elif(x[i] > -2):
        result = 1
    else:
        result = 0
    values.append(result)
    

print(values)
