from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph

sparql = SPARQLWrapper("http://127.0.0.1:7200/repositories/test1")

sparql.setQuery("""
PREFIX ex: <http://example.org/>

SELECT ?station ?HeightValue WHERE {
?station ex:Height ?HeightValue . }

LIMIT 10
""")



sparql.setReturnFormat(JSON)
results = sparql.query().convert()
print(results)


#http://localhost:7200/sparql?name=&infer=true&sameAs=true&query=PREFIX%20ex%3A%20%3Chttp%3A%2F%2Fexample.org%2F%3E%20%0A%0ASELECT%20%3Fstation%20%3FHeightValue%20WHERE%20%7B%0A%3Fstation%20ex%3AHeight%20%3FHeightValue%20.%20%7D