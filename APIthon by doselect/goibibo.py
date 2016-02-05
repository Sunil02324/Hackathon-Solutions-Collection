from __future__ import print_function
import requests
import os
import json
from datetime import datetime

id = input()
url = 'https://developer.goibibo.com/api/voyager/?app_id=6dd5883d&app_key=bc4632f2c33a866680aec37c2ed432a5&method=hotels.get_hotels_data&id_list=['+ str(id) + ']&id_type=_id'
joke_txt = requests.get(url).content
joke_texts = json.loads(joke_txt.decode('utf-8'))
name = joke_texts['data'][''+str(id)+'']['hotel_geo_node']['name']
print (name, end="")






import requests
import os
import json
from datetime import datetime

id = raw_input()

url = 'https://api.twitter.com/1.1/statuses/show.json?id='+id
headers = {
 "oauth_consumer_key":"ZEUhWrdwYRjdZdY3wLICgET3T", 
 "oauth_nonce":"0011f0d85a38b6a07be504518acbacbb", 
 "oauth_signature":"%2BT%2BxBYVYAme175FGltdLkIx6g0s%3D", 
 "oauth_signature_method":"HMAC-SHA1", 
 "oauth_timestamp":"1454228027",
 "oauth_token":"2321959032-9IrK7P61pNwGpqgBJ1ujEl5l6KHeNf1S64lW38e",
 "oauth_version":"1.0"
}
joke_txt = requests.get(url, headers=headers).content
joke_texts = json.loads(joke_txt.decode('utf-8'))
print joke_texts