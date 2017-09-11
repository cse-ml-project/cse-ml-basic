# cse-ml-basic camp 자료 
Azure Machine Learning cse camp  

이 Repo는 Azure Machine Learning in cse - 발표자료 & 실습자료 Repo임  

- Github URL : https://github.com/cse-ml-project/cse-ml-basic  

### github organazaion 가입
- github id 또는 email을 채널에 공유
- organization 가입 초대 승인

### ML 기본 세션 진행

### Iris를 이용한 예측 데모 진행

### Iris 모델 구축 데모
Iris 데모 데이터는 붓꽃 Label 데이터로 일반적인 분석 시나리오의 설명 등에 사용되는 예제 데이터임  
![Iris 데이터 구조](./images/iris.png)  
Iris 데이터 link : data 폴더 참조  


### 모바일 게임 데모 데이터
Game 데모 데이터는 가상의 모바일 게임사 시나리오에서 사용되는 게임사의 사용자 정보 예제 데이터임  
https://github.com/CloudBreadPaPa/azure-ml-busan/tree/master/data 폴더 하위 참조  

### Game 이탈 예측 모델 구축 데모
Game 데이터에 대한 구조 이해  

### 단계별 모델 구축
- Machine Learning 모델을 생성  
- ![Game User Chrun](images/20-2.png)  

### 실시간 예측 분석 ###
위의 공개한 분석모델을 활용해 예측모델(Predict model)을 구축하고 API를 통해 실시간 예측을 수행하는 것이 목표.

- Machine Learning 모델을 생성 후, Resfult API로 Azure Machine Learning 모델 생성
- 학습 모델을 실행하고, Test 예측 결과 확인
- 예측 모델(Predictive model)로 생성 후 API Web Service로 배포
- 생성된 Web service의 API Key를 이용해 C# 코드에서 real-time predict 수행 (코드 폴더 참조)

    ```
    public class UserChurnController : ApiController  
    {
        // POST api/UserChurn
        public HttpResponseMessage POST(CBChurn p)
        {
            // Machine Learning 분석 요청
            InvokeRequestResponseService(p).Wait();
            ...
        }

        // Machine Learning Web Service 호출
        static async Task InvokeRequestResponseService(CBChurn p)
        {
            ...
            const string apiKey = "API키-수정"; // Replace this with the API key for the web service
            client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", apiKey);
            client.BaseAddress = new Uri("Machine-Learning-Web-Service-URL-수정");
            HttpResponseMessage response = await client.PostAsJsonAsync("", scoreRequest).ConfigureAwait(false);
            if (response.IsSuccessStatusCode)
            {
                string result = await response.Content.ReadAsStringAsync();
                Debug.WriteLine("Result: {0}", result);
                p.ChurnYN = result;
            }
            ...
        }
    }
    ```

- ![CloudBread Game User Chrun](images/20-5.png)  

- Machine Learning API Controller를 publish 하고, 코드를 실행해 테스트 하거나, Postman 등에서 테스트 수행해 real-time prediction 수행
- Batch 작업을 수행하기 위해서 Machine Learning Batch execution이 제공하는 코드 이용이 가능.  

- ![CloudBread Game User Chrun](images/20-6.png)  

- 추가적으로, Functions를 이용해 server-less로 batch 호출 역시 가능  

- ![CloudBread Game User Chrun](images/20-7.png)  

- Excel을 이용해 Batch 분석도 가능  


### Python + Machine Learning 데모 코드
Azure Machine Learning이 노출하는 API를 Python에서 호출하는 예제 수행  

Iris 데이터를 호출해 RRE를 수행하는 예제  

C# 예제 코드
- 생성된 Web service의 API Key를 이용해 C# 코드에서 real-time predict 수행 (코드 폴더 참조)

#### Python3 예제 코드

```
import urllib
# If you are using Python 3+, import urllib instead of urllib2
import json
import re
import requests


data =  {

        "Inputs": {

                "input1":
                {
                    "ColumnNames": ["Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width", "Species"],
                    "Values": [ [ "1", "1", "1", "1", "" ], ]
                },        },
            "GlobalParameters": {
}
    }

body = str.encode(json.dumps(data))

# change url here
url = 'https://ussouthcentral.services.azureml.net/workspaces/a742afb173054d3ca4c4568eb889bb2d/services/13f806c7378e4d418a059f7e3a4a97bb/execute?api-version=2.0&details=true'
api_key = '<YOUR_API_KEY>' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)
response = urllib.request.urlopen(req)


    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers)
    # response = urllib.request.urlopen(req)

result = response.read()
print(result)


```