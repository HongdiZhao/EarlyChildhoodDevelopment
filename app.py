
from flask import Flask, render_template, url_for, redirect, request, abort
from datetime import datetime
app = Flask(__name__)
app.info={}


import pandas as pd
import numpy as np
import pickle
from sklearn import base
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression



class ColumnSelectTransformer(base.BaseEstimator, base.TransformerMixin):
    def __init__(self, col_names):
        self.col_names = col_names  # We will need these in transform()
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X[self.col_names].values


# ECD_logistics = pickle.load(open('ECD_logistics_identifyletters','rb'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/model', methods = ['GET','POST'])
def model():
    if request.method == 'GET':
        return render_template('model.html')


ECD_logistics = pickle.load(open('ECD_logistics_identifyletters_t','rb'))

def return_pred(earlyc_edu, age, melevel, windex5, has_hometoy, num_books):
    input_list = dict()
    inp = []
#     input_list['country'] = country
    input_list['earlyc_edu2'] = earlyc_edu
    input_list['age2'] = age
    input_list['melevel2'] = melevel
    input_list['windex52'] = windex5
    input_list['has_hometoy2'] = has_hometoy
    input_list['num_books2'] = num_books

    for k, v in input_list.items():
        inp.append(v)
    inp1 = np.asarray(inp, dtype=np.float32)
    inp2 = inp1.reshape(1,-1)
    predict_dummy = ECD_logistics.predict(inp2)
    predict_proba = ECD_logistics.predict_proba(inp2)[:,1]

    add = "and the probability is {}"
    if np.round(predict_dummy[0]) == 1:
        return "Child is able to identify 10 letters/alphabet " + (add.format(np.round(predict_proba[0],2)))
    else:
        return "Child is NOT able identify 10 letters/alphabet "+ (add.format(np.round(predict_proba[0],2)))


def return_pred_2(age, melevel, windex5, has_hometoy, num_books):
    input_list = dict()
    inp = []
    input_list['earlyc_edu2'] = 1
    input_list['age2'] = age
    input_list['melevel2'] = melevel
    input_list['windex52'] = windex5
    input_list['has_hometoy2'] = has_hometoy
    input_list['num_books2'] = num_books

    for k, v in input_list.items():
        inp.append(v)
    inp1 = np.asarray(inp, dtype=np.float32)
    inp2 = inp1.reshape(1,-1)
    predict_dummy = ECD_logistics.predict(inp2)
    predict_proba = ECD_logistics.predict_proba(inp2)[:,1]

    add = "and the probability is {}"
    if np.round(predict_dummy[0]) == 1:
        return "Child is able to identify 10 letters/alphabet " + (add.format(np.round(predict_proba[0],2)))
    else:
        return "Child is NOT able identify 10 letters/alphabet "+ (add.format(np.round(predict_proba[0],2)))



@app.route('/predict', methods = ['GET','POST'])
def predict():
    if request.method == 'GET':
        return render_template('predict.html')
    else:
        app.info['c_early_edu'] = request.form['earlyc_edu_1']
        app.info['family_wealth'] = request.form['windex5_1']
        app.info['m_edu'] = request.form['melevel_1']
        app.info['c_age'] = request.form['age_1']
        app.info['c_hashometoy'] = request.form['has_hometoy_1']
        app.info['c_num_books'] = request.form['num_books_1']
        Pred = return_pred(app.info['c_early_edu'],app.info['family_wealth'],app.info['m_edu'], app.info['c_age'],app.info['c_hashometoy'],app.info['c_num_books'])
        Pred_2 = return_pred_2(app.info['family_wealth'],app.info['m_edu'], app.info['c_age'],app.info['c_hashometoy'],app.info['c_num_books'])
        return render_template('model.html', Pred = Pred, Pred_2 = Pred_2)


@app.route('/worldmap', methods = ['GET','POST'])
def worldmap():
    if request.method == 'GET':
        return render_template('worldmap.html')

@app.route('/worldmap_edu', methods = ['GET','POST'])
def worldmap_edu():
    if request.method == 'GET':
        return render_template('worldmap_edu.html')



if __name__ == "__main__":
    app.run(port=33507, debug=True)

