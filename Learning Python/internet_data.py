#Importing modules needed for internet usage
import urllib
import urllib2
from lxml import html
import requests

#testing on npre website to pull information
url = requests.get('https://my.npre.illinois.edu/')
page = html.fromstring(url.text) #Creates html file in variable
