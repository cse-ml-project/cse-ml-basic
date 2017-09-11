import urllib2
# If you are using Python 3+, import urllib instead of urllib2

import json 


data =  {

        "Inputs": {

                "input1":
                {
                    "ColumnNames": ["idx", "나이", "프로모션참여수", "식별자", "일평균게임플레이분", "90일내아이템구매수", "게임레벨범위", "보유크리스탈", "유입경로", "인종", "성별", "가입코드", "구매번호", "주당접속수", "가입국가", "이탈여부"],
                    "Values": [ [ "0", "0", "0", "0", "0", "0", "0", "0", "value", "value", "value", "0", "0", "0", "value", "value" ], [ "0", "0", "0", "0", "0", "0", "0", "0", "value", "value", "value", "0", "0", "0", "value", "value" ], ]
                },        },
            "GlobalParameters": {
}
    }

body = str.encode(json.dumps(data))

url = 'https://asiasoutheast.services.azureml.net/workspaces/46d0e60b05b34558827abd41f11d204f/services/5fe50da906bf450d81d07db8aab4c9c5/execute?api-version=2.0&details=true'
api_key = 'R0PlD/Mo+R2olr+I8qFTbBseKqtQ3oeNas8pcfMhzuQ+thj3sfqN+sWjGeTaZPXiu1+3rluYBv8YVKKKoMtqxw==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib2.Request(url, body, headers) 

try:
    response = urllib2.urlopen(req)

    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers) 
    # response = urllib.request.urlopen(req)

    result = response.read()
    print(result) 
except urllib2.HTTPError, error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())

    print(json.loads(error.read()))                 