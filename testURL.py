import requests

# get a requests handle
req = requests.get("http://www.heartnsoul.com/ascii_art/flowers.txt");

# access status code using req.status_code
print "status: "+str(req.status_code)

# access text in body using req.text
print "content:\n"+str(req.text)
