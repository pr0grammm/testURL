import requests
import sys

try:
	#get filename from user
	fname = sys.argv[1]


	#open file for reading
	fopen = open(fname,'r')

	#do for every line in file
	for line in fopen.readlines():
		url=line.strip('\n')
		req=requests.get(url)
		print url
		print str(req.status_code)
		

	fopen.close()

except Exception as e:
	print e
