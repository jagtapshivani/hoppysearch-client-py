import json
import requests

# origin = "https://en5b7dd3ch.execute-api.ap-south-1.amazonaws.com/"
# url = origin+"search"
# config_data = dict()
# config_data["q"] = "wife"
# payload = ""
# headers = {
#   "accept": "application/json",
#   "Authorization": "hs_i4in8hz1j4d9mlmb"
# }
# config = json.dumps(config_data)
# response = requests.get(url, params = config_data, headers= headers)
# print(response.content)


# url = origin+"search"
# config_data = dict()
luceneQuery = "name: Mr AND type: Mother"
# headers = {
#   "Authorization": "hs_i4in8hz1j4d9mlmb"
# }

# data = {
#     "defaultKeyNameToBeSearch" : "",
#     "analyzerClass" : "org.apache.lucene.analysis.standard.StandardAnalyzer",
#     "luceneQuery" : luceneQuery
# }
# config = json.dumps(config_data)
# response = requests.post(url, json = data, headers= headers)
# print(response.content)

config_data = dict()
config_data["q"] = "wife"
from urllib3 import HTTPSConnectionPool
headers = {
  'accept': 'application/json',
  'Authorization': 'hs_i4in8hz1j4d9mlmb'
}
pool = HTTPSConnectionPool('en5b7dd3ch.execute-api.ap-south-1.amazonaws.com', headers= headers)
response = pool.request('GET','/search', fields = config_data)
# print(response.data)
data = {
    "defaultKeyNameToBeSearch" : "",
    "analyzerClass" : "org.apache.lucene.analysis.standard.StandardAnalyzer",
    "luceneQuery" : luceneQuery
}
response = pool.request_encode_body('GET','/search', body = json.dumps(data))
response
print(json.loads(response.data)['documents'])
print('NumCon', pool.num_connections)
print('NumRq', pool.num_requests)
