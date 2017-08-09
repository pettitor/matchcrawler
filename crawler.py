import json
#import urllib2
from urllib.request import urlopen
#import requests
import time
import codecs

reader = codecs.getreader("utf-8")
for match_id in range (3333000000, 3333549786):
	#data = json.load(urllib2.urlopen("https://api.opendota.com/api/matches/"+str(match_id)))
	try:
		response = urlopen("https://api.opendota.com/api/matches/"+str(match_id))
		data = json.load(reader(response))
	#data = json.load(requests.get("https://api.opendota.com/api/matches/"+str(match_id)))
		print(data)
		with open(str(match_id)+".json", 'w') as outfile:
#			outfile.write('{ "index" : {"_index":"matches","_type":"match","_id":"'+str(match_id)+'"}}\n')
			json.dump(data, outfile)
			outfile.write('\n')
		outfile.close()
		time.sleep(2)
	except:
		pass
