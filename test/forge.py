# Created by Spencer Owen
# https://github.com/spudstud
# twitter @spencer450

# Querries the puppet forge for select modules

import json
import urllib2
# import sys
# import requests
from xml.etree.ElementTree import Element, SubElement, Comment,  tostring

forgeurl='https://forge.puppetlabs.com/modules.json?q=gitlab'
jsonURL=urllib2.urlopen(forgeurl)
jsonObject=json.load(jsonURL)

# print jsonObject#For debugging

# Create a xml object that matches the documentaion 
# http://www.alfredforum.com/topic/5-generating-feedback-in-workflows/

items = Element('items')

for x in jsonObject:
	item = SubElement(items, 'item')
	item.set('uid', x['full_name'] )
	#item.set('arg', x['desc']      ) # arg allows you to pass a string to other displays (notification center)
	item.set('valid', 'yes')

	title = SubElement(item, 'title')
	title.text = str( x['full_name'] )

	subtitle = SubElement(item, 'subtitle')
	subtitle.text = str( x['desc'] )

#icon = SubElement(item, 'icon')
#icon.text = "MtGox.png"
# print '....'
print tostring(items)
