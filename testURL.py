import requests
import sys

file_name = sys.argv[1]
fwrite = open('report.csv', 'w')
fopen = open(file_name, 'r')
counter = 0

for line in fopen.readlines():
    counter = counter + 1
    url = line.strip('\n')
    try:
        req = requests.head(url)
        success = 'true'

    except Exception as e:
        print e
        success = 'false'

    if (success == 'false'):
        fwrite.write('[-],' + str(counter) +',' + url +',' +'No Result' + '\n')	
	
    else:
	code=str(req.status_code)
    	if (code.startswith('2')):
        	print ('[+] ' + url + ',' + code + '\n')
        	fwrite.write('[+],' + str(counter) + ',' + url + ',' + code+ '\n')
    	else:
        	print ('[-] ' + url + ',' + code +'\n')
        	fwrite.write('[-],' + str(counter) +',' + url + ',' + code + '\n')

fwrite.close()
fopen.close()
