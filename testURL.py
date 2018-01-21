import requests
import sys
# get a requests handle
req = requests.get("http://www.heartnsoul.com/ascii_art/flowers.txt");

# access status code using req.status_code
print "status: "+str(req.status_code)

# access text in body using req.text
print "content:\n"+str(req.text)

#get filename from user
fname = sys.argv[1]

print fname

#open file for reading
fopen = open(fname,'r')

for x in fopen.readlines():
	print x.strip('\n')

print '\n'

