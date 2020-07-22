from flask import Flask,render_template,url_for,request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

app = Flask(__name__ , template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    dataset = pd.read_csv('datafinal.csv')

    x = dataset.iloc[: , 1:-1].values
    y = dataset.iloc[: , -1].values
    result =0
    value_stat = []
    for i in range(0 , 276):
        if(y[i] > 0):
            result = 1
        elif y[i] < 0:
            result = 0
        else:
            result =0.5
        value_stat.append(result)
        

    final = np.array([value_stat])

    status = final.T

    y = status
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    ann = tf.keras.models.Sequential()

    ann.add(tf.keras.layers.Dense(units=14 , activation = 'relu'))

    ann.add(tf.keras.layers.Dense(units=14 , activation = 'relu'))

    ann.add(tf.keras.layers.Dense(units=1 , activation='relu'))

    ann.compile(optimizer = 'adam' , loss = 'binary_crossentropy' , metrics= ['accuracy'])

    ann.fit(X_train , y_train ,  epochs = 100)
    

    if request.method =='POST':
        dataa = (request.form['a'])
        datab = (request.form['b'])
        datac = (request.form['c'])
        datad = (request.form['d'])
        datae = (request.form['e'])
        dataf = (request.form['f'])
        datag = (request.form['g'])
        datah = (request.form['h'])
        datai = (request.form['i'])
        dataj = (request.form['j'])
        datak = (request.form['k'])
        datal = (request.form['l'])
        health = ann.predict(sc.transform([[dataa,datab,datac,datad,datae,dataf,datag,datah,datai,dataj,datak,datal]]))
        
        

    return render_template('result.html', prediction = health)




if __name__ =='__main__':
    app.run(debug=True)