from __future__ import print_function
import requests
import os
import json
from datetime import datetime

org,repo,c = raw_input().split()
c = datetime.strptime(c, '%d-%m-%Y').date()
ti = '1900-02-08T05:54:12Z'
pull = 'https://api.github.com/repos/'+ org +'/' + repo + '/issues'
issue = 'https://api.github.com/repos/'+ org +'/' + repo + '/pulls'
joke_pul = requests.get(pull).content
joke_pulls = json.loads(joke_pul.decode('utf-8'))
joke_issu = requests.get(issue).content
joke_issues = json.loads(joke_issu.decode('utf-8'))

for joke_issue in joke_issues:
	date = joke_issue['created_at']
	fmt = "%Y-%m-%dT%H:%M:%SZ"
	date_only = datetime.strptime(date, fmt).date()
	if date_only == c:
		for joke_pull in joke_pulls:
			dates = joke_pull['created_at']
			fmts = "%Y-%m-%dT%H:%M:%SZ"
			dates_only = datetime.strptime(dates, fmts).date()
			if dates_only == c:
				if joke_pull['created_at'] > joke_issue['created_at']:
					print(joke_issue['html_url'])
					print(joke_pull['html_url'])
				else:
					continue
		