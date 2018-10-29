import csv
import requests
import xml.etree.ElementTree as ET


l = []
tree = ET.parse('Yugoslav_torpedo_boat_T5.xml')
root=tree.getroot()
f = open("demofile.txt","w")
for name in root.iter('{http://www.mediawiki.org/xml/export-0.10/}username'):
    l.append(name.text)
    f.write(name.text)
    f.write("\n")

#https://en.wikipedia.org/w/index.php?title=Special:Contributions&offset=20070214050528&limit=500&contribs=user&target=Stavenn&namespace=&tagfilter=&start=&end=