import urllib.request
import json
import textwrap

with urllib.request.urlopen('https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224') as f:
    text = f.read()
    decordedtext = text.decode('UTF-8')
    print(textwrap.fill(decordedtext, width=50))
