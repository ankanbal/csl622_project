import sys
import xml.etree.ElementTree as etr

tree = etr.parse('Zapata_rail.xml')
root= tree.getroot()
l=[]

for name in root.iter('username'):
	l.append((name.text))

print(l)
