import requests, urllib
import urllib, urllib2

response = urllib2.urlopen(raw_input())
html = response.read()
page =  str(html)
before = '<meta property=\"og:image\" content=\"'
pos=str(page).find(before)