import re, urllib
print re.sub('</p>', '', re.sub('<br>|<p>|<br/> |<br/>','\n', re.sub('No', '\nNo', 
urllib.URLopener().open('http://www.99-bottles-of-beer.net/lyrics.html').read()[3516:16297])))


