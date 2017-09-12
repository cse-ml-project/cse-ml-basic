import urllib.request
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'idx': "1",   
                            'age': "1",   
                            'promotion_num': "1",   
                            'identity': "1",   
                            'game_play_min_per_day': "1",   
                            'item_purchase_num_in_90_days': "1",   
                            'game_level': "1",   
                            'crystal': "1",   
                            'race': "",   
                            'gender': "",   
                            'register_code': "1",   
                            'purchase_num': "1",   
                            'game_play_num_per_week': "1",   
                            'country': "",   
                            'churn_YN': "",   
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://asiasoutheast.services.azureml.net/subscriptions/3e6494d9d19d41c6bfa644870aecc57b/services/2b11b85c3fbe4daf8b8e6dc17c558e11/execute?api-version=2.0&format=swagger'
api_key = '<CHANGE-HERE>' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))