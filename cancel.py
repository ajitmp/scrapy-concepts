# import the required library
import requests
 
# speficy the schedule endpoint
url = 'http://localhost:6800/cancel.json'
 
# replace with the target job ID
job_id = '2355a5e44b1611efa99218c04d3aadee'
 
# specify request parameters
data = {'project': 'testing_scrapy', 'job': job_id}
 
# make Python request
response = requests.post(url, data=data)
 
# resolve and print the JSON response
if response.status_code == 200:
    print(response.json())
else:
    print(response.json())
