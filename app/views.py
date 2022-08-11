from app import app
from flask import Flask, request, jsonify
from app.contentbase_filtering.cb_model import ContentBase
import json

@app.route('/')
def home():
   return "hello world!"


@app.route('/api/re-check', methods=['GET', 'POST'])
def welcome():
    return "It works!"


@app.route('/person/')
def hello():
    return jsonify({'name':'Jimit1',
                    'address':'India'})


@app.route('/api/recommend', methods=['GET', 'POST'])
def recommend():
    content_base = ContentBase("./dataset/movies.csv")
    content_base.fit()
    sim_scores, values =  content_base.genre_recommendations('Tom and Huck (1995)', 10)
    

    results = []
    i = 0
    for value in values:
        result_tmp = {}
        i +=1
        result_tmp['id'] = i
        result_tmp['name'] = value
        results.append(result_tmp)

    # import pdb
    # pdb.set_trace()
    #json_string = json.dumps(results)
    response = app.response_class(
        response=json.dumps(results),
        status=200,
        mimetype='application/json'
    )
    return response