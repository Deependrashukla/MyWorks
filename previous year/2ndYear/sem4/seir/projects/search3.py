import sys
import time
from whoosh import index
from whoosh.fields import Schema, TEXT, ID
from whoosh import index
import os, os.path
from whoosh import index
from whoosh import qparser
from whoosh.qparser import QueryParser
import configparser
def index_search(dirname, search_fields, search_query, numResults):
    start = time.time()
    ix = index.open_dir(dirname)
    schema = ix.schema
    
    og = qparser.OrGroup.factory(0.9)
    mp = qparser.MultifieldParser(search_fields, schema, group = og)

    
    q = mp.parse(search_query)
    
    i=0
    with ix.searcher() as s:
        results = s.search(q, terms=True, limit = 10)
        print("Search Results: ")
        
        print(results[0:10])
        docWithPath=results[0]['path']
        textContent=results[0]['textdata']
        print(docWithPath, "\n", textContent)
    end = time.time()
    print("Time taken: ", end - start)
myQuery = str(sys.argv[1])

config = configparser.RawConfigparser()
config.read("ConfigFile.properties")
myQuery=config.get("ParameterSearch", "myQuery")
indexDir=config.get("ParameterSearch","indexDir")
results_dict = index_search("indexdir", ['title','content'], myQuery)
