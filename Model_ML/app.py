#from itertools import Predicate
from os import name
import numpy as np
from flask import Flask , render_template , request
import pickle

loaded_model = pickle.load(open('final_model.sav', 'rb'))

app = Flask(__name__)

@app.route("/" , methods=['POST'])
def hello():
    data1 = request.form['season']
    data2 = request.form['weather']
    data3 = request.form['temp']
    data4 = request.form['humidity	']
    data5 = request.form['windspeed']
    sampel = np.array([[data1,data2,data3,data4,data5]])
    res = loaded_model.predict(sampel)
    print (res)

    return render_template("index.html" , data=res)

if __name__ == "__main__":
    app.run(debug=True , host="0.0.0.0")    