from __future__ import print_function
import requests
import os
import json
from datetime import datetime


org,repo,c = raw_input().split()
c = datetime.strptime(c, '%d-%m-%Y').date()
pulls = 0
issues = 0
####Issues requests##
url = 'https://api.github.com/repos/'+ org +'/' + repo + '/issues'
joke_txt = requests.get(url).content
joke_texts = json.loads(joke_txt.decode('utf-8'))
for joke_text in joke_texts:
	date = joke_text['created_at']
	fmt = "%Y-%m-%dT%H:%M:%SZ"
	date_only = datetime.strptime(date, fmt).date()
	if date_only == c:
		issues += 1
print ('Issues: ' + str(issues))

####Pull requests##
url = 'https://api.github.com/repos/'+ org +'/' + repo + '/pulls'
joke_txt = requests.get(url).content
joke_texts = json.loads(joke_txt.decode('utf-8'))
for joke_text in joke_texts:
	date = joke_text['created_at']
	fmt = "%Y-%m-%dT%H:%M:%SZ"
	date_only = datetime.strptime(date, fmt).date()
	if date_only == c:
		pulls += 1
		
out = 'Pull requests: ' + str(pulls)
print (out, end="")	