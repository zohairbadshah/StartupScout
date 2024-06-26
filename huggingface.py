import requests



def query(payload):
        API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
        
        headers = {"Authorization": "Bearer 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"}
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
      
def hugging_face(website_content,crunchbase_content,relevance_content):
    prompt = f"""
    
    I am giving you information about a company from different sources, combine them in a concise form in the format given below
    
    Information:
    {website_content}
    {crunchbase_content}
    {relevance_content}

    
    Provide the information as :
    - Description: What does the company do
    - Industry: What is the industry of the company
    - Customers: Is it B2C or B2B
    - Geography: The location in which the company operates
    - Funding: Total funding amount and investors
    """ 
    output = query({
        "inputs": prompt,
    })
    if "error" in output:
        return output["error"]
    response_text = output[0]['generated_text']
    model_response = response_text.split("Provide the information as")[1]
    return model_response

