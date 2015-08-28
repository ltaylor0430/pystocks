""" Pystocks API 1.0
    Author: Lawrence Taylor
"""


import json
from urllib.parse import urlencode
from urllib.request import urlopen

baseurl = "https://query.yahooapis.com/v1/public/yql?"
yql_query = "select wind from weather.forecast where woeid=2460286"
yql_url = baseurl + urlencode({'q': yql_query}) + "&format=json"
result = urlopen(yql_url).read().decode("utf-8")
print(type(result))
data = json.loads(result)
print(data['query']['results'])
