import os
from dotenv import load_dotenv
import json
from urllib3 import HTTPSConnectionPool
from data import Data
load_dotenv()
origin = os.getenv('URL') # Current Enviroment URL


class HoppysearchClient:

    def __init__(self, config):
        self.headers = {
            'accept': 'application/json',
            'Authorization': 'hs_i4in8hz1j4d9mlmb'
        }
        self.apiKey = config[0]
        self.defaultKeyNameToBeSearch = "" if config[1] == "" else config[1]
        self.pool = HTTPSConnectionPool(
            'en5b7dd3ch.execute-api.ap-south-1.amazonaws.com', headers=self.headers)

    def lucene_search(self, luceneQuery):
        luceneQuery = "name: Mr AND type: Mother"
        data = {
            "defaultKeyNameToBeSearch": self.defaultKeyNameToBeSearch,
            "analyzerClass": "org.apache.lucene.analysis.standard.StandardAnalyzer",
            "luceneQuery": luceneQuery
        }
        response = self.pool.request_encode_body(
            'GET', '/search', body=json.dumps(data))
        if response.status == 200:
            # print('NumCon', self.pool.num_connections)
            # print('NumRq', self.pool.num_requests)
            return Data.from_json(json.loads(response.data)['documents'])
        else:
            return response.status

    def simple_search(self, query):
        config_data = dict()
        config_data["q"] = query
        response = self.pool.request('GET', '/search', fields=config_data)
        if response.status == 200:
            # print('NumCon', self.pool.num_connections)
            # print('NumRq', self.pool.num_requests)
            return Data.from_json(json.loads(response.data)['documents'])
        else:
            return response.status
