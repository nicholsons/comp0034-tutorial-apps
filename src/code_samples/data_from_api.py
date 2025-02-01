import urllib.request

# Get data from the arxiv API
# https://info.arxiv.org/help/api/basics.html#python

url = 'http://export.arxiv.org/api/query?search_query=all:education&start=0&max_results=1'
data = urllib.request.urlopen(url)
print(data.read().decode('utf-8'))
