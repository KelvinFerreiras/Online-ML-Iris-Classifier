#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
# print(dict["sl"])
#dict["sl"],dict["sw"],dict["pl"],dict["pw"]

import sys 
import urllib3, requests, json


def main(dict):
    wml_credentials={
    "url": "https://us-south.ml.cloud.ibm.com",
    "username": "146f93c0-e6f2-49aa-a40f-09b98bdee9a6",
    "password": "c6a1826a-bfed-433c-baf9-e0e2269d2ea0"
    }
    
    headers = urllib3.util.make_headers(basic_auth='{username}:{password}'.format(username=wml_credentials['username'], password=wml_credentials['password']))
    url = '{}/v3/identity/token'.format(wml_credentials['url'])
    response = requests.get(url, headers=headers)
    mltoken = json.loads(response.text).get('token')
    
    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
    
   
    print(dict["sl"])
    print(dict["sw"])


    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"fields": ["sepal_lenght", "sepal_width", "petal_lenght", "petal_width"], "values": [[dict["sl"],dict["sw"],dict["pl"],dict["pw"]]]}
    
    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/v3/wml_instances/8a75195d-58cc-4250-a126-82610361dec2/published_models/a29aee24-5e90-456e-8eeb-50dce5efbcce/deployments/2645b20b-2ab3-4f28-9b88-eefbf8ecef92/online', json=payload_scoring, headers=header)
    print("Scoring response")
    retval=json.loads(response_scoring.text)
    print(retval)
    
    return retval
