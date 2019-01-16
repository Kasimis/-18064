import urllib2
a=raw_input('enter url')
response = urllib2.urlopen(a)
html = response.read()
import re
i=len(re.findall("<a href",html))
j=len(re.findall("</p>", html))+len(re.findall("<br>", html))
print ("Number of links",i)
print ("Number of line changes",j)
