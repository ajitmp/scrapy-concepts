# import the required library
#curl http://localhost:6800/schedule.json -d project=testing_scrapy -d spider=books
import requests
 

#get list of all spiders
#curl http://localhost:6800/listspiders.json?project=testing_scrapy
url = "http://localhost:6800/listspiders.json"
params= {'project': 'testing_scrapy'}
# make Python request
response = requests.get(url, params=params)
SPIDERS=[]
# resolve and print the JSON response
if response.status_code == 200:
    data =response.json()
    SPIDERS=data.get('spiders', "No spiders found")
    print(SPIDERS)
else:
    print(response.json())

# speficy schedule endpoint
url = 'http://localhost:6800/schedule.json'

for spider in SPIDERS: 
    # specify project and spider names
    data = {'project': 'testing_scrapy', 'spider': spider}
    
    # make Python request
    response = requests.post(url, data=data)
    
    # resolve and print the JSON response
    if response.status_code == 200:
        print(response.json())
    else:
        print(response.json())
