from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph
import json

sparql = SPARQLWrapper("http://127.0.0.1:7200/repositories/group_e_football")

queries = {
    "1": """
prefix football: <http://www.cs7is1.org/ontologies/football-ontology-3#>

Select (Count(?win_club_id) as ?number_of_wins) ?club_name
where {
    ?competition_entity a football:Competition;
                        football:competition_name ?competition_name;
                        football:competition_id ?competition_id.
    FILTER(?competition_name= "uefa-champions-league")

    ?games_entity a football:Games;
            football:competition_code ?competition_id;
            football:game_id ?game_id;
            football:win_club_id ?win_club_id.

    ?club_entity a football:Clubs;
            football:club_id ?win_club_id;
            football:club_pretty_name ?club_name.

}
GROUP BY ?club_name
ORDER BY DESC (?number_of_wins)
""",
"2": """
prefix football: <http://www.cs7is1.org/ontologies/football-ontology-3#>

Select *
where {
    ?s ?p ?o
}
LIMIT 25
"""
}



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


