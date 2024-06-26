import requests
import json
import time

def get_relevance(uri):

    region='f1db6c'

    base_url = f"https://api-{region}.stack.tryrelevance.com/latest"
    api_key = 'e90666d8968d-4416-99b0-126ed92c5d5d:sk-ZGFhMTNlNzEtNmFhNC00YWU1LTkwMTEtNGYwNjJkNzFiMDRl'

    headers = {
    "Authorization": api_key,
    }
    
    response=requests.post(base_url+f'/studios/71b87f7f-60f3-494b-9876-96051ac5d504/trigger_limited', 
        headers=headers,
        data=json.dumps({"params":{"query":uri},"project":"e90666d8968d-4416-99b0-126ed92c5d5d"})
    )
    
    job=response.json()
    return job['output']['answer']