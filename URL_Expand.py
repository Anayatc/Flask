import requests
from urllib.parse import urlparse

url = 'http://amzn.to/2pfDiJE'


# takes url as input and returns full url if url has been shortened.
def url_resolve(url):
    session = requests.Session()
    resp = session.head(url, allow_redirects=True)
    return resp.url


def look_up():
    final_dest = url_resolve(url)
    parsed_uri = urlparse(final_dest)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return domain


print(url_resolve('http://amzn.to/2pfDiJE'))
print(url_resolve('https://goo.gl/Oha1fI'))
print(url_resolve('http://ow.ly/nFlK30byASt'))
print(look_up())
