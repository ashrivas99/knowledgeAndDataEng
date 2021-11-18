from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph
from query_file import queries
import json


sparql = SPARQLWrapper("http://127.0.0.1:7200/repositories/group_e_football")


app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
def hello():
    return "Group E Football Server"


@app.route('/query/<id>', methods=['GET'])
def query_handler(id):

    sparql.setQuery(queries.get(str(id)))
    sparql.setReturnFormat(JSON)

    return sparql.query().convert()



@app.route('/user-query', methods=['GET'])
def user_query():
    query_string = request.args.get('user_query')

    sparql.setQuery(str(query_string))
    sparql.setReturnFormat(JSON)


    return sparql.query().convert()


@app.route('/query-text/<id>', methods=['GET'])
def query_text_handler(id):

    return str(queries[str(id)])

if __name__ == '__main__':
    app.run(debug=True)


