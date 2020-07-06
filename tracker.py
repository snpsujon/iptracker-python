#ip tracker v1 by snpsujon
#a simple python script
#visit : https://snpsujon.me
#github : https://github.com/snpsujon
#youtube : https://www.youtube.com/snpsujon

import urllib2
import json


#Find own ip
url = "http://ip-api.com/json/"
load1 = urllib2.urlopen(url)
read1 = load1.read()
result1 = json.loads(read1)
print ("\nYour IP: " + result1['query'])
print ("if you want to terminated type exit\n")

while True:
    ip = raw_input("Which IP you want to track: ")

    if ip == 'exit':
        break
    else:
        #ipstack
        api = "http://api.ipstack.com/"
        load = urllib2.urlopen(api + ip + '?access_key=fd0c1eae3c2d27ee676af0db2b864b0e')  #use own api from ipstack.com 
        read = load.read()
        result = json.loads(read)

        #ip-api
        url = "http://ip-api.com/json/"
        load1 = urllib2.urlopen(url + ip)
        read1 = load1.read()
        result1 = json.loads(read1)





        if result1['status'] == 'success':
            # latitude
            lati = result['latitude']
            lat = "{:.4f}".format(lati)
            # longitude
            lon = result['longitude']
            long = "{:.4f}".format(lon)

            # more info
            more = json.dumps(result['location'])

            # printing information
            print ("\nInformation About This IP[" + ip + "] :\n")
            print ("IP: " + result['ip'])
            print ("IP Type: " + result['type'])
            print ("Continent Name: " + result['continent_name'])
            print ("Continent Code: " + result['continent_code'])
            print ("Country: " + result['country_name'])
            print ("Country Code: " + result1['countryCode'])
            print ("Region Name: " + result['region_name'])
            print ("Region Code: " + result['region_code'])
            print ("City: " + result['city'])
            print ("Zip: " + result['zip'])
            print ("TimeZone: " + result1['timezone'])
            print ("isp: " + result1['isp'])
            print ("Latitude: " + lat)
            print ("longitude: " + long)
            print ("More Info :\n" + more)
            print ("\n\n")
        else:
            print ("\nThere has an error with you IP[" + ip + "] Please try again\n")
