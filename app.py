from flask import Flask,request,render_template
import pandas as pd
import numpy as np
import pickle
import sklearn

app=Flask(__name__)


pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)


@app.route('/')
def welcome():
    return render_template('input.html')

@app.route('/result',methods=['POST','get'])
def sepalpetal():
    if request.method == 'POST':
      result = request.form

    SepalLengthCm=int(result['SepalLength'])
    SepalWidthCm=int(result['SepalWidth'])
    PetalLengthCm=int(result['PetalLength'])
    PetalWidthCm=int(result['PetalWidth'])
    prediction=classifier.predict([[SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm]])
    return "The predicted flower is:"+str(prediction)



if __name__ == '__main__':
   app.run(debug = True) 