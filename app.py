from flask import Flask, render_template, request
from urllib.request import urlopen
import pickle

app = Flask(__name__)

# Routing
@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def predict():
    with open('model.pkl', 'rb') as f:
        clf2 = pickle.load(f)

    weight = request.args.get("weight")
    length1 = request.args.get("length1")
    length2 = request.args.get("length2")
    length3 = request.args.get("length3")
    height = request.args.get("height")
    width = request.args.get("width")
    X = tuple([[int(weight), int(length1), int(length2), int(length3), int(height), int(width)]])
    predict_value = clf2.predict(X)

    fish_dict = {0: 'Bream', 1: 'Parkki', 2: 'Perch', 3: 'Pike', 4: 'Roach', 5: 'Smelt'}
    predict = fish_dict.get(round(predict_value[0]))

    return render_template('index.html', prediction = predict)

