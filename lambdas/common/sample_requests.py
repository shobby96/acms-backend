get_users_request = {
        'resource': '/users',
        'path': '/users',
        'httpMethod': 'GET',
        'headers': None,
        'multiValueHeaders': None,
        'queryStringParameters': {

        },
        'multiValueQueryStringParameters': {
                'organization_id': [2]
        }
}

post_users_request = {
        'resource': '/users',
        'path': '/users',
        'httpMethod': 'POST',
        'headers': None,
        'multiValueHeaders': None,
        'queryStringParameters': {},
        'body': {
            'first_name': 'Shahbakht Anwar',
            'last_name': 'AnwarNew',
            'email': 'shahbakhtanwar123@gmail.com'
        },
        'multiValueQueryStringParameters': {
        }
    }


post_add_users_request = {
        'resource': '/users/add',
        'path': '/users/add',
        'httpMethod': 'POST',
        'headers': None,
        'multiValueHeaders': None,
        'queryStringParameters': {},
        'body': {
            'first_name': 'Talal',
            'last_name': 'Anwar',
            'email': 'tan@gmail.com'
        },
        'multiValueQueryStringParameters': {
        }
    }

get_organizations_request = {
        'resource': '/organizations',
        'path': '/organizations',
        'httpMethod': 'GET',

        'multiValueHeaders': None,
        'queryStringParameters': {},
        'body': {

        },

        'multiValueQueryStringParameters': {
                "organization_id": [1]
        }
    }

post_organizations_request = {
   "resource":"/organizations",
   "path":"/organizations",
   "httpMethod":"POST",
   "headers":{
      "accept":"application/json, text/plain, */*",
      "accept-encoding":"gzip, deflate, br",
      "accept-language":"en-GB,en-US;q=0.9,en;q=0.8",
      "accesstoken":"eyJraWQiOiJHRTdcL3JubWg4WnBrODRFZ3dXV0tUUVQ3RDhOTGRycXRqVTBxQmZMQjZmRT0iLCJhbGciOiJSUzI1NiJ9.eyJvcmlnaW5fanRpIjoiNjFmZWE5MzgtZjlhZi00NjRmLWJlYmYtMTdhN2U5NjBiZDcyIiwic3ViIjoiOTFhN2ZlODEtYmM0Yy00M2UzLTkxNTgtMGMzZTNiZDg4Y2U4IiwiZXZlbnRfaWQiOiIwNDVjYTgwMi1iOWZhLTQwNmItYjAzMy0yOGU0Y2Q0ZjdmZmUiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIiwiYXV0aF90aW1lIjoxNjI3NzYxNzMzLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9yMU44VExxanEiLCJleHAiOjE2Mjc3NjUzMzMsImlhdCI6MTYyNzc2MTczMywianRpIjoiYWUxNGIzYzItMGNkOC00MDA3LTk5ZDktNWYzNzllMTVjOTJjIiwiY2xpZW50X2lkIjoiMzM4aHVnZDN0amd1M2plcG5hNXB1cTZoaiIsInVzZXJuYW1lIjoiOTFhN2ZlODEtYmM0Yy00M2UzLTkxNTgtMGMzZTNiZDg4Y2U4In0.XJhobfE_pxyXkXSU926WuyLGPimUoQHB7GzixF3obUB2pbwfWc3z-zhQDgKLf9QnIV1nNiHEwp9iZ6qm_r50kJYnwU6uCJtj_GaYcsjOQjk2TOxg6PH6wnSX-0RlZcL3D-3GZ1iCuNMiliASOKaaJo0LkXCQd8X31aCy7E5QhOMGXZoAUSw8v9nSKEVhSsds_b63S9o3A666gYPvGB3jYzcsWkayaJrqkeqhTksjil7kGjPIPEVKASv8tXLc44_xKtzdEvfl0hSiCCGwVHjuotHHAgpgwMp1QRSzdLoiJEDf-P-In8oS1ztSrYAZvm9ojO8ltO1CW1cEUVQv8GrvKA",
      "Authorization":"eyJraWQiOiI4Vk5YYmRQSFd4cEFDdlVWTXVPcnpoN1Y3dllreWljMExVRDFwRzFSdUVJPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI5MWE3ZmU4MS1iYzRjLTQzZTMtOTE1OC0wYzNlM2JkODhjZTgiLCJjdXN0b206bGFzdE5hbWUiOiJBbndhciIsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX3IxTjhUTHFqcSIsImN1c3RvbTppZCI6IjU2IiwiY29nbml0bzp1c2VybmFtZSI6IjkxYTdmZTgxLWJjNGMtNDNlMy05MTU4LTBjM2UzYmQ4OGNlOCIsIm9yaWdpbl9qdGkiOiI2MWZlYTkzOC1mOWFmLTQ2NGYtYmViZi0xN2E3ZTk2MGJkNzIiLCJhdWQiOiIzMzhodWdkM3RqZ3UzamVwbmE1cHVxNmhqIiwiZXZlbnRfaWQiOiIwNDVjYTgwMi1iOWZhLTQwNmItYjAzMy0yOGU0Y2Q0ZjdmZmUiLCJjdXN0b206Zmlyc3ROYW1lIjoiU2hhaGJha2h0IiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2Mjc3NjE3MzMsImV4cCI6MTYyNzc2NTMzMywiaWF0IjoxNjI3NzYxNzMzLCJqdGkiOiJkNTNlN2VlNy1hZjIzLTQwMzMtYjQwYi1mNTcwZTlkNWFkMGQifQ.cVBCG__6yPR_nysCcX1k8MXQq0BsztXBFxIwaL-zDtLjvG67_IXPUjL4lBBWeZV21KNB_ey2yr0fDWOI7yTrvlyGzm0-NdZBPNGQwny1kZ2aZZzXXIkD-2BlV0PzjfmgzczWwDgP_UACThTrJX_tUh_Q6Mqij2eylR3SakxTe7B6llKY7BgLzMQcdv2FEJKMPJcNhd-jw4t16IITLPv0m-yidRJhryV3X-efyugXtjm9VPwsznNejnvSz8INUavi7xT2LJpII1tOsN0spb6bNNSb-JyUbTnbZMdwa1TUS5obRnnIDzkxF5GxEGzDjKBbA6ZycnDHJmFjL7rkMii3FQ",
      "content-type":"application/json;charset=UTF-8",
      "Host":"qz8a0nzf5b.execute-api.us-east-1.amazonaws.com",
      "origin":"http://localhost:3000",
      "referer":"http://localhost:3000/",
      "sec-ch-ua":"\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
      "sec-ch-ua-mobile":"?1",
      "sec-fetch-dest":"empty",
      "sec-fetch-mode":"cors",
      "sec-fetch-site":"cross-site",
      "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36",
      "X-Amzn-Trace-Id":"Root=1-6105ac4f-1db7687e3993d8245631708c",
      "X-Forwarded-For":"72.255.7.138",
      "X-Forwarded-Port":"443",
      "X-Forwarded-Proto":"https"
   },
   "multiValueHeaders":{
      "accept":[
         "application/json, text/plain, */*"
      ],
      "accept-encoding":[
         "gzip, deflate, br"
      ],
      "accept-language":[
         "en-GB,en-US;q=0.9,en;q=0.8"
      ],
      "accesstoken":[
         "eyJraWQiOiJHRTdcL3JubWg4WnBrODRFZ3dXV0tUUVQ3RDhOTGRycXRqVTBxQmZMQjZmRT0iLCJhbGciOiJSUzI1NiJ9.eyJvcmlnaW5fanRpIjoiNjFmZWE5MzgtZjlhZi00NjRmLWJlYmYtMTdhN2U5NjBiZDcyIiwic3ViIjoiOTFhN2ZlODEtYmM0Yy00M2UzLTkxNTgtMGMzZTNiZDg4Y2U4IiwiZXZlbnRfaWQiOiIwNDVjYTgwMi1iOWZhLTQwNmItYjAzMy0yOGU0Y2Q0ZjdmZmUiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIiwiYXV0aF90aW1lIjoxNjI3NzYxNzMzLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9yMU44VExxanEiLCJleHAiOjE2Mjc3NjUzMzMsImlhdCI6MTYyNzc2MTczMywianRpIjoiYWUxNGIzYzItMGNkOC00MDA3LTk5ZDktNWYzNzllMTVjOTJjIiwiY2xpZW50X2lkIjoiMzM4aHVnZDN0amd1M2plcG5hNXB1cTZoaiIsInVzZXJuYW1lIjoiOTFhN2ZlODEtYmM0Yy00M2UzLTkxNTgtMGMzZTNiZDg4Y2U4In0.XJhobfE_pxyXkXSU926WuyLGPimUoQHB7GzixF3obUB2pbwfWc3z-zhQDgKLf9QnIV1nNiHEwp9iZ6qm_r50kJYnwU6uCJtj_GaYcsjOQjk2TOxg6PH6wnSX-0RlZcL3D-3GZ1iCuNMiliASOKaaJo0LkXCQd8X31aCy7E5QhOMGXZoAUSw8v9nSKEVhSsds_b63S9o3A666gYPvGB3jYzcsWkayaJrqkeqhTksjil7kGjPIPEVKASv8tXLc44_xKtzdEvfl0hSiCCGwVHjuotHHAgpgwMp1QRSzdLoiJEDf-P-In8oS1ztSrYAZvm9ojO8ltO1CW1cEUVQv8GrvKA"
      ],
      "Authorization":[
         "eyJraWQiOiI4Vk5YYmRQSFd4cEFDdlVWTXVPcnpoN1Y3dllreWljMExVRDFwRzFSdUVJPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI5MWE3ZmU4MS1iYzRjLTQzZTMtOTE1OC0wYzNlM2JkODhjZTgiLCJjdXN0b206bGFzdE5hbWUiOiJBbndhciIsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX3IxTjhUTHFqcSIsImN1c3RvbTppZCI6IjU2IiwiY29nbml0bzp1c2VybmFtZSI6IjkxYTdmZTgxLWJjNGMtNDNlMy05MTU4LTBjM2UzYmQ4OGNlOCIsIm9yaWdpbl9qdGkiOiI2MWZlYTkzOC1mOWFmLTQ2NGYtYmViZi0xN2E3ZTk2MGJkNzIiLCJhdWQiOiIzMzhodWdkM3RqZ3UzamVwbmE1cHVxNmhqIiwiZXZlbnRfaWQiOiIwNDVjYTgwMi1iOWZhLTQwNmItYjAzMy0yOGU0Y2Q0ZjdmZmUiLCJjdXN0b206Zmlyc3ROYW1lIjoiU2hhaGJha2h0IiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2Mjc3NjE3MzMsImV4cCI6MTYyNzc2NTMzMywiaWF0IjoxNjI3NzYxNzMzLCJqdGkiOiJkNTNlN2VlNy1hZjIzLTQwMzMtYjQwYi1mNTcwZTlkNWFkMGQifQ.cVBCG__6yPR_nysCcX1k8MXQq0BsztXBFxIwaL-zDtLjvG67_IXPUjL4lBBWeZV21KNB_ey2yr0fDWOI7yTrvlyGzm0-NdZBPNGQwny1kZ2aZZzXXIkD-2BlV0PzjfmgzczWwDgP_UACThTrJX_tUh_Q6Mqij2eylR3SakxTe7B6llKY7BgLzMQcdv2FEJKMPJcNhd-jw4t16IITLPv0m-yidRJhryV3X-efyugXtjm9VPwsznNejnvSz8INUavi7xT2LJpII1tOsN0spb6bNNSb-JyUbTnbZMdwa1TUS5obRnnIDzkxF5GxEGzDjKBbA6ZycnDHJmFjL7rkMii3FQ"
      ],
      "content-type":[
         "application/json;charset=UTF-8"
      ],
      "Host":[
         "qz8a0nzf5b.execute-api.us-east-1.amazonaws.com"
      ],
      "origin":[
         "http://localhost:3000"
      ],
      "referer":[
         "http://localhost:3000/"
      ],
      "sec-ch-ua":[
         "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\""
      ],
      "sec-ch-ua-mobile":[
         "?1"
      ],
      "sec-fetch-dest":[
         "empty"
      ],
      "sec-fetch-mode":[
         "cors"
      ],
      "sec-fetch-site":[
         "cross-site"
      ],
      "User-Agent":[
         "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36"
      ],
      "X-Amzn-Trace-Id":[
         "Root=1-6105ac4f-1db7687e3993d8245631708c"
      ],
      "X-Forwarded-For":[
         "72.255.7.138"
      ],
      "X-Forwarded-Port":[
         "443"
      ],
      "X-Forwarded-Proto":[
         "https"
      ]
   },
   "queryStringParameters":"None",
   "multiValueQueryStringParameters":"None",
   "pathParameters":"None",
   "stageVariables":"None",
   "requestContext":{
      "resourceId":"1d3rtw",
      "authorizer":{
         "claims":{
            "sub":"91a7fe81-bc4c-43e3-9158-0c3e3bd88ce8",
            "custom:lastName":"Anwar",
            "iss":"https://cognito-idp.us-east-1.amazonaws.com/us-east-1_r1N8TLqjq",
            "custom:id":"56",
            "cognito:username":"91a7fe81-bc4c-43e3-9158-0c3e3bd88ce8",
            "origin_jti":"61fea938-f9af-464f-bebf-17a7e960bd72",
            "aud":"338hugd3tjgu3jepna5puq6hj",
            "event_id":"045ca802-b9fa-406b-b033-28e4cd4f7ffe",
            "custom:firstName":"Shahbakht",
            "token_use":"id",
            "auth_time":"1627761733",
            "exp":"Sat Jul 31 21:02:13 UTC 2021",
            "iat":"Sat Jul 31 20:02:13 UTC 2021",
            "jti":"d53e7ee7-af23-4033-b40b-f570e9d5ad0d"
         }
      },
      "resourcePath":"/organizations",
      "httpMethod":"POST",
      "extendedRequestId":"DWfcdEiooAMF9gg=",
      "requestTime":"31/Jul/2021:20:02:23 +0000",
      "path":"/dev/organizations",
      "accountId":"261044366975",
      "protocol":"HTTP/1.1",
      "stage":"dev",
      "domainPrefix":"qz8a0nzf5b",
      "requestTimeEpoch":1627761743562,
      "requestId":"758b7784-97d4-4d8c-bdf3-4b39eceb9c09",
      "identity":{
         "cognitoIdentityPoolId":"None",
         "accountId":"None",
         "cognitoIdentityId":"None",
         "caller":"None",
         "sourceIp":"72.255.7.138",
         "principalOrgId":"None",
         "accessKey":"None",
         "cognitoAuthenticationType":"None",
         "cognitoAuthenticationProvider":"None",
         "userArn":"None",
         "userAgent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36",
         "user":"None"
      },
      "domainName":"qz8a0nzf5b.execute-api.us-east-1.amazonaws.com",
      "apiId":"qz8a0nzf5b"
   },
   "body":"{\"organization_name\":\"New Organization\",\"email\":\"neworg@gmail.com\",\"user_id\":56}",
   "isBase64Encoded":"false"
}

put_organizations_request= {
        'resource': '/organizations',
        'path': '/organizations',
        'httpMethod': 'PUT',
        'headers': None,
        'multiValueHeaders': None,
        'queryStringParameters': {},
        'body': {
                'organization_id': 14,
                'email': 'shabbysof123t@gmail.com'
        },
        'multiValueQueryStringParameters': {

        }
}

post_member_organization = {
        'resource': '/organizations/addMember',
        'path': '/organizations/addMember',
        'httpMethod': 'POST',
        'headers': None,
        'multiValueHeaders': None,
        'queryStringParameters': {},
        'body': {
                'organization_id': 14,
                'email': 'lasifo8480@luxiu2.com'
        },
        'multiValueQueryStringParameters': {

        }
}


confirm_organization_member = {
        'resource': '/organizations/confirmMember',
        'path': '/organizations/confirmMember',
        'httpMethod': 'POST',
        'headers': None,
        'multiValueHeaders': None,
        'queryStringParameters': {},
        'body': {
                'first_name': 'Shahbakht',
                'last_name': 'Anwar',
                'email': 'lasifo8480@luxiu2.com',
                'password': 'Test@12345',
                'session': 'AYABeC7B1qAQ7F8IqNc-acPm5dwAHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo3NDU2MjM0Njc1NTU6a2V5L2IxNTVhZmNhLWJmMjktNGVlZC1hZmQ4LWE5ZTA5MzY1M2RiZQC4AQIBAHiAcAt7Ei832QLLvv5tnR-fAKEzaf-OMDg-j1aLh6qMVAGq8sD6i3DMWfgYmuhbRGhbAAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMwU5oh_RK0ETYyMUjAgEQgDtfWMwReeTQhVeYpHcLFEBOIC2W2MO7rsERENqrpqyMSwFtcsTcbONX_gYKXqayQIFkTxVKolk-PwOevQIAAAAADAAAEAAAAAAAAAAAAAAAAABneuaV3Ooo6rK459JWfUVL_____wAAAAEAAAAAAAAAAAAAAAEAAADUgh5yyv6LCqezDzqh_-sxuB9iEtBE_W7z1zd1SWNZlH9lJPLMyQ2JmT3y2jPD1b7vNG34ABw7FctiHeZI9D8TwRCKVnHH2SQY_ssXEQMBEGPAtqA3yO9aJznOYtyzn3CECArfBx-BEgNdtrQTh2nf_OTNuEQiJGo8ffOciAyHGZ8sbeCw45n5Yuaj8wTOXyHxZNfiqKxsyVJu9jaA-c8gHhWbBYTeMqjWi9tkSRaDsiv0jXG4H9IvHgYRUOw40EBMXPw-afwgm6YAciVa4Zn_MBjpEw5gpdi57OLGmIAyV_P2iv6C'
        },
        'multiValueQueryStringParameters': {

        }
}

get_requests = {'resource': '/request', 'path': '/request', 'httpMethod': 'GET', 'headers': {'accept': 'application/json, text/plain, */*', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8', 'accesstoken': 'eyJraWQiOiJHRTdcL3JubWg4WnBrODRFZ3dXV0tUUVQ3RDhOTGRycXRqVTBxQmZMQjZmRT0iLCJhbGciOiJSUzI1NiJ9.eyJvcmlnaW5fanRpIjoiZTZjZTVlY2MtMDVjMS00OGQyLTliNDEtNDZhZmQ0YjNjNGNiIiwic3ViIjoiMTgwMmY5ZjgtN2JhYy00YzhhLWFiNjMtYTVmMzE1NzA4ODYxIiwiZXZlbnRfaWQiOiIxYjZhZmY2OC04YmI4LTQ5MGYtOTE3Zi1kNGMxMDc1ZmIwN2QiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIiwiYXV0aF90aW1lIjoxNjI4NjgwMzMxLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9yMU44VExxanEiLCJleHAiOjE2Mjg2ODM5MzEsImlhdCI6MTYyODY4MDMzMSwianRpIjoiMzJjMGQzMDAtMmQ3YS00MTEwLWI5ZGQtZjg3YmI3M2JkZTliIiwiY2xpZW50X2lkIjoiMzM4aHVnZDN0amd1M2plcG5hNXB1cTZoaiIsInVzZXJuYW1lIjoiMTgwMmY5ZjgtN2JhYy00YzhhLWFiNjMtYTVmMzE1NzA4ODYxIn0.xh0DUBYEAkuWoV1JldJzFYglN4VFi72PTFLwAWC-a70_lOJGQRV3oKoowsk9ojJcCaPybpzpYuxzLK8yNSYTvCPl668H-ULwON7R3Y8wEkFqfrjdVwjcm4TprrIYuM8oxWNhW2yzfnB3pcSsvpGd1kIPE_x85omSruxyjmL_NCKkXJQ-yGTaKJ-lFtns7UIDDb4tnjJOZwCbQ2fxOwAdBfM0oAH26lPoeYlx9XUrh7XYDRouey08Wefc7xIGyiBKUxOYMMkeEeOZLLOmRlQ_2dAPf7chwpJ0-4nvreY3I3GIsz43H92epjCeq04Zn6gZIrY8c8q0QSTlZ9HLq3p8Yg', 'Authorization': 'eyJraWQiOiI4Vk5YYmRQSFd4cEFDdlVWTXVPcnpoN1Y3dllreWljMExVRDFwRzFSdUVJPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIxODAyZjlmOC03YmFjLTRjOGEtYWI2My1hNWYzMTU3MDg4NjEiLCJjdXN0b206bGFzdE5hbWUiOiJXZWIiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9yMU44VExxanEiLCJjdXN0b206aWQiOiI3MCIsImNvZ25pdG86dXNlcm5hbWUiOiIxODAyZjlmOC03YmFjLTRjOGEtYWI2My1hNWYzMTU3MDg4NjEiLCJjdXN0b206b3JnYW5pemF0aW9uSUQiOiIyOSIsIm9yaWdpbl9qdGkiOiJlNmNlNWVjYy0wNWMxLTQ4ZDItOWI0MS00NmFmZDRiM2M0Y2IiLCJhdWQiOiIzMzhodWdkM3RqZ3UzamVwbmE1cHVxNmhqIiwiZXZlbnRfaWQiOiIxYjZhZmY2OC04YmI4LTQ5MGYtOTE3Zi1kNGMxMDc1ZmIwN2QiLCJjdXN0b206Zmlyc3ROYW1lIjoiUmVhY3QiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTYyODY4MDMzMSwiZXhwIjoxNjI4NjgzOTMxLCJpYXQiOjE2Mjg2ODAzMzEsImp0aSI6ImZlMjRmNWY4LThlMGYtNGM4Mi05OWQ2LTZkNjVmY2M5MmRiNCJ9.NwgC9xDgEWeDptxOu2uHiVbVmMSW148JTHHRdJcNVS4hLt38HD93UdYyxxQaNTJIJuOqDz0zDwtfB0ZXq-ukBpeMXLdIQkyMg_3TSV3vTtWTH_fInblyAakXzJJqzEvWSRrSs4C9n8FQIloqYkZhPgSto7Hm1JzYAwNlJWxktleTDgeXxfOzFYbiSr2D--cvkhg5B2cp6uCzoIcR4Lc9NC51Yg8y8LVq2PkByGqNtrTOQZahK_IGoUdECYWNE6U_6Txp_SYhv2GCkCr_O_DIGPdJ3xCm4-ihagi8QHjTOCocBDGNvrfLmOuxXWswsI5Vrw_uhkW4aLLg_BLS2I-2NA', 'Host': 'qz8a0nzf5b.execute-api.us-east-1.amazonaws.com', 'origin': 'http://localhost:3000', 'referer': 'http://localhost:3000/', 'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"', 'sec-ch-ua-mobile': '?1', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'cross-site', 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36', 'X-Amzn-Trace-Id': 'Root=1-6113b64c-583ab2343123d7b40a18b385', 'X-Forwarded-For': '72.255.7.138', 'X-Forwarded-Port': '443', 'X-Forwarded-Proto': 'https'}, 'multiValueHeaders': {'accept': ['application/json, text/plain, */*'], 'accept-encoding': ['gzip, deflate, br'], 'accept-language': ['en-GB,en-US;q=0.9,en;q=0.8'], 'accesstoken': ['eyJraWQiOiJHRTdcL3JubWg4WnBrODRFZ3dXV0tUUVQ3RDhOTGRycXRqVTBxQmZMQjZmRT0iLCJhbGciOiJSUzI1NiJ9.eyJvcmlnaW5fanRpIjoiZTZjZTVlY2MtMDVjMS00OGQyLTliNDEtNDZhZmQ0YjNjNGNiIiwic3ViIjoiMTgwMmY5ZjgtN2JhYy00YzhhLWFiNjMtYTVmMzE1NzA4ODYxIiwiZXZlbnRfaWQiOiIxYjZhZmY2OC04YmI4LTQ5MGYtOTE3Zi1kNGMxMDc1ZmIwN2QiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIiwiYXV0aF90aW1lIjoxNjI4NjgwMzMxLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9yMU44VExxanEiLCJleHAiOjE2Mjg2ODM5MzEsImlhdCI6MTYyODY4MDMzMSwianRpIjoiMzJjMGQzMDAtMmQ3YS00MTEwLWI5ZGQtZjg3YmI3M2JkZTliIiwiY2xpZW50X2lkIjoiMzM4aHVnZDN0amd1M2plcG5hNXB1cTZoaiIsInVzZXJuYW1lIjoiMTgwMmY5ZjgtN2JhYy00YzhhLWFiNjMtYTVmMzE1NzA4ODYxIn0.xh0DUBYEAkuWoV1JldJzFYglN4VFi72PTFLwAWC-a70_lOJGQRV3oKoowsk9ojJcCaPybpzpYuxzLK8yNSYTvCPl668H-ULwON7R3Y8wEkFqfrjdVwjcm4TprrIYuM8oxWNhW2yzfnB3pcSsvpGd1kIPE_x85omSruxyjmL_NCKkXJQ-yGTaKJ-lFtns7UIDDb4tnjJOZwCbQ2fxOwAdBfM0oAH26lPoeYlx9XUrh7XYDRouey08Wefc7xIGyiBKUxOYMMkeEeOZLLOmRlQ_2dAPf7chwpJ0-4nvreY3I3GIsz43H92epjCeq04Zn6gZIrY8c8q0QSTlZ9HLq3p8Yg'], 'Authorization': ['eyJraWQiOiI4Vk5YYmRQSFd4cEFDdlVWTXVPcnpoN1Y3dllreWljMExVRDFwRzFSdUVJPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIxODAyZjlmOC03YmFjLTRjOGEtYWI2My1hNWYzMTU3MDg4NjEiLCJjdXN0b206bGFzdE5hbWUiOiJXZWIiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9yMU44VExxanEiLCJjdXN0b206aWQiOiI3MCIsImNvZ25pdG86dXNlcm5hbWUiOiIxODAyZjlmOC03YmFjLTRjOGEtYWI2My1hNWYzMTU3MDg4NjEiLCJjdXN0b206b3JnYW5pemF0aW9uSUQiOiIyOSIsIm9yaWdpbl9qdGkiOiJlNmNlNWVjYy0wNWMxLTQ4ZDItOWI0MS00NmFmZDRiM2M0Y2IiLCJhdWQiOiIzMzhodWdkM3RqZ3UzamVwbmE1cHVxNmhqIiwiZXZlbnRfaWQiOiIxYjZhZmY2OC04YmI4LTQ5MGYtOTE3Zi1kNGMxMDc1ZmIwN2QiLCJjdXN0b206Zmlyc3ROYW1lIjoiUmVhY3QiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTYyODY4MDMzMSwiZXhwIjoxNjI4NjgzOTMxLCJpYXQiOjE2Mjg2ODAzMzEsImp0aSI6ImZlMjRmNWY4LThlMGYtNGM4Mi05OWQ2LTZkNjVmY2M5MmRiNCJ9.NwgC9xDgEWeDptxOu2uHiVbVmMSW148JTHHRdJcNVS4hLt38HD93UdYyxxQaNTJIJuOqDz0zDwtfB0ZXq-ukBpeMXLdIQkyMg_3TSV3vTtWTH_fInblyAakXzJJqzEvWSRrSs4C9n8FQIloqYkZhPgSto7Hm1JzYAwNlJWxktleTDgeXxfOzFYbiSr2D--cvkhg5B2cp6uCzoIcR4Lc9NC51Yg8y8LVq2PkByGqNtrTOQZahK_IGoUdECYWNE6U_6Txp_SYhv2GCkCr_O_DIGPdJ3xCm4-ihagi8QHjTOCocBDGNvrfLmOuxXWswsI5Vrw_uhkW4aLLg_BLS2I-2NA'], 'Host': ['qz8a0nzf5b.execute-api.us-east-1.amazonaws.com'], 'origin': ['http://localhost:3000'], 'referer': ['http://localhost:3000/'], 'sec-ch-ua': ['"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"'], 'sec-ch-ua-mobile': ['?1'], 'sec-fetch-dest': ['empty'], 'sec-fetch-mode': ['cors'], 'sec-fetch-site': ['cross-site'], 'User-Agent': ['Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36'], 'X-Amzn-Trace-Id': ['Root=1-6113b64c-583ab2343123d7b40a18b385'], 'X-Forwarded-For': ['72.255.7.138'], 'X-Forwarded-Port': ['443'], 'X-Forwarded-Proto': ['https']}, 'queryStringParameters': {'limit': '10', 'offset': '0'}, 'multiValueQueryStringParameters': {'limit': ['10'], 'offset': ['0']}, 'pathParameters': None, 'stageVariables': None, 'requestContext': {'resourceId': 'lpca1g', 'authorizer': {'claims': {'sub': '1802f9f8-7bac-4c8a-ab63-a5f315708861', 'custom:lastName': 'Web', 'iss': 'https://cognito-idp.us-east-1.amazonaws.com/us-east-1_r1N8TLqjq', 'custom:id': '70', 'cognito:username': '1802f9f8-7bac-4c8a-ab63-a5f315708861', 'custom:organizationID': '29', 'origin_jti': 'e6ce5ecc-05c1-48d2-9b41-46afd4b3c4cb', 'aud': '338hugd3tjgu3jepna5puq6hj', 'event_id': '1b6aff68-8bb8-490f-917f-d4c1075fb07d', 'custom:firstName': 'React', 'token_use': 'id', 'auth_time': '1628680331', 'exp': 'Wed Aug 11 12:12:11 UTC 2021', 'iat': 'Wed Aug 11 11:12:11 UTC 2021', 'jti': 'fe24f5f8-8e0f-4c82-99d6-6d65fcc92db4'}}, 'resourcePath': '/request', 'httpMethod': 'GET', 'extendedRequestId': 'D5lr6HhboAMF8JQ=', 'requestTime': '11/Aug/2021:11:36:44 +0000', 'path': '/dev/request', 'accountId': '261044366975', 'protocol': 'HTTP/1.1', 'stage': 'dev', 'domainPrefix': 'qz8a0nzf5b', 'requestTimeEpoch': 1628681804043, 'requestId': '1aab5a8f-c679-46d2-9ff9-f23821d19193', 'identity': {'cognitoIdentityPoolId': None, 'accountId': None, 'cognitoIdentityId': None, 'caller': None, 'sourceIp': '72.255.7.138', 'principalOrgId': None, 'accessKey': None, 'cognitoAuthenticationType': None, 'cognitoAuthenticationProvider': None, 'userArn': None, 'userAgent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36', 'user': None}, 'domainName': 'qz8a0nzf5b.execute-api.us-east-1.amazonaws.com', 'apiId': 'qz8a0nzf5b'}, 'body': None, 'isBase64Encoded': False}

get_requests_admin = {
        'resource': '/requests/admin',
        'path': '/requests/admin',
        'httpMethod': 'GET',
        'headers': None,
        'multiValueHeaders': None,
        'queryStringParameters': {
            'organization_id': 1
        },
        'multiValueQueryStringParameters': {
            'organization_id': [2]
        }
    }


post_request = {
   "resource":"/request",
   "path":"/request",
   "httpMethod":"POST",
   "headers":{
      "accept":"application/json, text/plain, */*",
      "accept-encoding":"gzip, deflate, br",
      "accept-language":"en-GB,en-US;q=0.9,en;q=0.8",
      "accesstoken":"eyJraWQiOiJHRTdcL3JubWg4WnBrODRFZ3dXV0tUUVQ3RDhOTGRycXRqVTBxQmZMQjZmRT0iLCJhbGciOiJSUzI1NiJ9.eyJvcmlnaW5fanRpIjoiOTg3NmZjMzgtMDg2NC00YTA5LWE3NzEtZjUyZTkwOGM3N2I5Iiwic3ViIjoiMTgwMmY5ZjgtN2JhYy00YzhhLWFiNjMtYTVmMzE1NzA4ODYxIiwiZXZlbnRfaWQiOiJjYTY1OGM5OC00NGE3LTRiOGItOTUyMC1lYjU3MzdmZjMwMTQiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIiwiYXV0aF90aW1lIjoxNjI3OTMyNjMwLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9yMU44VExxanEiLCJleHAiOjE2Mjc5MzYyMzAsImlhdCI6MTYyNzkzMjYzMCwianRpIjoiNmVkMjQ1YzctZmNiNy00ZThmLTkxMTMtMmMyMGRhMDcwNmFmIiwiY2xpZW50X2lkIjoiMzM4aHVnZDN0amd1M2plcG5hNXB1cTZoaiIsInVzZXJuYW1lIjoiMTgwMmY5ZjgtN2JhYy00YzhhLWFiNjMtYTVmMzE1NzA4ODYxIn0.Pmryj59S_Y3qEczi4N07fyBTw3M2PkAzqVmDhJAUa-P4VGZ1jPvLBMyrrN0Yp8WpqzuXp9eSw_ivKdePHwvqEvURs7giH2i7mVHQdw4xUEmIwyY3CUUrPs4yxxgok4rL2UnXYjsfXTH30vWHbmgIAmMxzjTy0dy9jBspSCWAV8ll9fgi9Ok2sk4mLnUcwWLZBiGt9knD24_vCpqjrpANcI9fq6Gj8BzJHgKffAJruBUt5Ejt0gRSMYtT_JB7UHNPPUNugjlVIrK5lUXKPD-klf2tjL5WqgnQRHUnd5UkiYzKz80IHLaoS8RCog7n8IuvQ8cox-E1H6aRlhH5aPwoqQ",
      "Authorization":"eyJraWQiOiI4Vk5YYmRQSFd4cEFDdlVWTXVPcnpoN1Y3dllreWljMExVRDFwRzFSdUVJPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIxODAyZjlmOC03YmFjLTRjOGEtYWI2My1hNWYzMTU3MDg4NjEiLCJjdXN0b206bGFzdE5hbWUiOiJXZWIiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9yMU44VExxanEiLCJjdXN0b206aWQiOiI3MCIsImNvZ25pdG86dXNlcm5hbWUiOiIxODAyZjlmOC03YmFjLTRjOGEtYWI2My1hNWYzMTU3MDg4NjEiLCJjdXN0b206b3JnYW5pemF0aW9uSUQiOiIyOSIsIm9yaWdpbl9qdGkiOiI5ODc2ZmMzOC0wODY0LTRhMDktYTc3MS1mNTJlOTA4Yzc3YjkiLCJhdWQiOiIzMzhodWdkM3RqZ3UzamVwbmE1cHVxNmhqIiwiZXZlbnRfaWQiOiJjYTY1OGM5OC00NGE3LTRiOGItOTUyMC1lYjU3MzdmZjMwMTQiLCJjdXN0b206Zmlyc3ROYW1lIjoiUmVhY3QiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTYyNzkzMjYzMCwiZXhwIjoxNjI3OTM2MjMwLCJpYXQiOjE2Mjc5MzI2MzAsImp0aSI6IjQ2MTBmZjRjLWI3NzUtNDgxNC05NGUxLWEzNzViNDI1ZTIxYiJ9.Iw6OrZBo_l9hTfy2Rwdnw-M3uZHx1jGbj4zOGUsXlLrxoAlL7ze1LiKYeTBgaAD9JJpFK321NQ1hgNdDNDFOfMAEAvIx286xeYs40bFUNJYxO5gfx3afg-P8hLEkAZgA935LGocVxJy-CBdE7KH5WcHtBbnMPAbWk63UtpK3VuGA0OPCdbUFEcLj-hZbiviXHsQS4d3KMcUf2yFOr-cnEvW7O56DXynP65nRIvtbU3lauhyYLK1roVGLbhglC_6B6es5282xKKr0wThBZAbundxt-fAsYfir80LeO2cYljBr7W_tWFIuHFWDXoBHYF1UQeUqkWbSDvSKv4Mmd3LwIg",
      "content-type":"application/json;charset=UTF-8",
      "Host":"qz8a0nzf5b.execute-api.us-east-1.amazonaws.com",
      "origin":"http://localhost:3000",
      "referer":"http://localhost:3000/",
      "sec-ch-ua":"\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
      "sec-ch-ua-mobile":"?1",
      "sec-fetch-dest":"empty",
      "sec-fetch-mode":"cors",
      "sec-fetch-site":"cross-site",
      "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36",
      "X-Amzn-Trace-Id":"Root=1-6108499a-7b8143c43198dfd77c444ff4",
      "X-Forwarded-For":"72.255.7.138",
      "X-Forwarded-Port":"443",
      "X-Forwarded-Proto":"https"
   },
   "multiValueHeaders":{
      "accept":[
         "application/json, text/plain, */*"
      ],
      "accept-encoding":[
         "gzip, deflate, br"
      ],
      "accept-language":[
         "en-GB,en-US;q=0.9,en;q=0.8"
      ],
      "accesstoken":[
         "eyJraWQiOiJHRTdcL3JubWg4WnBrODRFZ3dXV0tUUVQ3RDhOTGRycXRqVTBxQmZMQjZmRT0iLCJhbGciOiJSUzI1NiJ9.eyJvcmlnaW5fanRpIjoiOTg3NmZjMzgtMDg2NC00YTA5LWE3NzEtZjUyZTkwOGM3N2I5Iiwic3ViIjoiMTgwMmY5ZjgtN2JhYy00YzhhLWFiNjMtYTVmMzE1NzA4ODYxIiwiZXZlbnRfaWQiOiJjYTY1OGM5OC00NGE3LTRiOGItOTUyMC1lYjU3MzdmZjMwMTQiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIiwiYXV0aF90aW1lIjoxNjI3OTMyNjMwLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9yMU44VExxanEiLCJleHAiOjE2Mjc5MzYyMzAsImlhdCI6MTYyNzkzMjYzMCwianRpIjoiNmVkMjQ1YzctZmNiNy00ZThmLTkxMTMtMmMyMGRhMDcwNmFmIiwiY2xpZW50X2lkIjoiMzM4aHVnZDN0amd1M2plcG5hNXB1cTZoaiIsInVzZXJuYW1lIjoiMTgwMmY5ZjgtN2JhYy00YzhhLWFiNjMtYTVmMzE1NzA4ODYxIn0.Pmryj59S_Y3qEczi4N07fyBTw3M2PkAzqVmDhJAUa-P4VGZ1jPvLBMyrrN0Yp8WpqzuXp9eSw_ivKdePHwvqEvURs7giH2i7mVHQdw4xUEmIwyY3CUUrPs4yxxgok4rL2UnXYjsfXTH30vWHbmgIAmMxzjTy0dy9jBspSCWAV8ll9fgi9Ok2sk4mLnUcwWLZBiGt9knD24_vCpqjrpANcI9fq6Gj8BzJHgKffAJruBUt5Ejt0gRSMYtT_JB7UHNPPUNugjlVIrK5lUXKPD-klf2tjL5WqgnQRHUnd5UkiYzKz80IHLaoS8RCog7n8IuvQ8cox-E1H6aRlhH5aPwoqQ"
      ],
      "Authorization":[
         "eyJraWQiOiI4Vk5YYmRQSFd4cEFDdlVWTXVPcnpoN1Y3dllreWljMExVRDFwRzFSdUVJPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIxODAyZjlmOC03YmFjLTRjOGEtYWI2My1hNWYzMTU3MDg4NjEiLCJjdXN0b206bGFzdE5hbWUiOiJXZWIiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9yMU44VExxanEiLCJjdXN0b206aWQiOiI3MCIsImNvZ25pdG86dXNlcm5hbWUiOiIxODAyZjlmOC03YmFjLTRjOGEtYWI2My1hNWYzMTU3MDg4NjEiLCJjdXN0b206b3JnYW5pemF0aW9uSUQiOiIyOSIsIm9yaWdpbl9qdGkiOiI5ODc2ZmMzOC0wODY0LTRhMDktYTc3MS1mNTJlOTA4Yzc3YjkiLCJhdWQiOiIzMzhodWdkM3RqZ3UzamVwbmE1cHVxNmhqIiwiZXZlbnRfaWQiOiJjYTY1OGM5OC00NGE3LTRiOGItOTUyMC1lYjU3MzdmZjMwMTQiLCJjdXN0b206Zmlyc3ROYW1lIjoiUmVhY3QiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTYyNzkzMjYzMCwiZXhwIjoxNjI3OTM2MjMwLCJpYXQiOjE2Mjc5MzI2MzAsImp0aSI6IjQ2MTBmZjRjLWI3NzUtNDgxNC05NGUxLWEzNzViNDI1ZTIxYiJ9.Iw6OrZBo_l9hTfy2Rwdnw-M3uZHx1jGbj4zOGUsXlLrxoAlL7ze1LiKYeTBgaAD9JJpFK321NQ1hgNdDNDFOfMAEAvIx286xeYs40bFUNJYxO5gfx3afg-P8hLEkAZgA935LGocVxJy-CBdE7KH5WcHtBbnMPAbWk63UtpK3VuGA0OPCdbUFEcLj-hZbiviXHsQS4d3KMcUf2yFOr-cnEvW7O56DXynP65nRIvtbU3lauhyYLK1roVGLbhglC_6B6es5282xKKr0wThBZAbundxt-fAsYfir80LeO2cYljBr7W_tWFIuHFWDXoBHYF1UQeUqkWbSDvSKv4Mmd3LwIg"
      ],
      "content-type":[
         "application/json;charset=UTF-8"
      ],
      "Host":[
         "qz8a0nzf5b.execute-api.us-east-1.amazonaws.com"
      ],
      "origin":[
         "http://localhost:3000"
      ],
      "referer":[
         "http://localhost:3000/"
      ],
      "sec-ch-ua":[
         "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\""
      ],
      "sec-ch-ua-mobile":[
         "?1"
      ],
      "sec-fetch-dest":[
         "empty"
      ],
      "sec-fetch-mode":[
         "cors"
      ],
      "sec-fetch-site":[
         "cross-site"
      ],
      "User-Agent":[
         "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36"
      ],
      "X-Amzn-Trace-Id":[
         "Root=1-6108499a-7b8143c43198dfd77c444ff4"
      ],
      "X-Forwarded-For":[
         "72.255.7.138"
      ],
      "X-Forwarded-Port":[
         "443"
      ],
      "X-Forwarded-Proto":[
         "https"
      ]
   },
   "queryStringParameters":"None",
   "multiValueQueryStringParameters":"None",
   "pathParameters":"None",
   "stageVariables":"None",
   "requestContext":{
      "resourceId":"lpca1g",
      "authorizer":{
         "claims":{
            "sub":"1802f9f8-7bac-4c8a-ab63-a5f315708861",
            "custom:lastName":"Web",
            "iss":"https://cognito-idp.us-east-1.amazonaws.com/us-east-1_r1N8TLqjq",
            "custom:id":"70",
            "cognito:username":"1802f9f8-7bac-4c8a-ab63-a5f315708861",
            "custom:organizationID":"29",
            "origin_jti":"9876fc38-0864-4a09-a771-f52e908c77b9",
            "aud":"338hugd3tjgu3jepna5puq6hj",
            "event_id":"ca658c98-44a7-4b8b-9520-eb5737ff3014",
            "custom:firstName":"React",
            "token_use":"id",
            "auth_time":"1627932630",
            "exp":"Mon Aug 02 20:30:30 UTC 2021",
            "iat":"Mon Aug 02 19:30:30 UTC 2021",
            "jti":"4610ff4c-b775-4814-94e1-a375b425e21b"
         }
      },
      "resourcePath":"/request",
      "httpMethod":"POST",
      "extendedRequestId":"DdBwLEcaIAMFhmA=",
      "requestTime":"02/Aug/2021:19:38:02 +0000",
      "path":"/dev/request",
      "accountId":"261044366975",
      "protocol":"HTTP/1.1",
      "stage":"dev",
      "domainPrefix":"qz8a0nzf5b",
      "requestTimeEpoch":1627933082547,
      "requestId":"2307e784-d972-470e-b1e7-f45d6c6f0302",
      "identity":{
         "cognitoIdentityPoolId":"None",
         "accountId":"None",
         "cognitoIdentityId":"None",
         "caller":"None",
         "sourceIp":"72.255.7.138",
         "principalOrgId":"None",
         "accessKey":"None",
         "cognitoAuthenticationType":"None",
         "cognitoAuthenticationProvider":"None",
         "userArn":"None",
         "userAgent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36",
         "user":"None"
      },
      "domainName":"qz8a0nzf5b.execute-api.us-east-1.amazonaws.com",
      "apiId":"qz8a0nzf5b"
   },
   "body":{
      "user_id":"70",
      "invitation_to":"Friends",
      "reason":"yam yam",
      "status":0,
      "invitation_date":"20210811",
      "invite_time":"00:04:00"
   },
   "isBase64Encoded":"false"
}

accept_request = {
        'resource': '/requests/accept',
        'path': '/requests/accept',
        'httpMethod': 'PUT',
        'headers': None,
        'multiValueHeaders': None,
        'queryStringParameters': {
            'request_number': 1,

        },
        'body': {
                'request_number': 2
        }
}

cancel_request = {
        'resource': '/requests/cancel',
        'path': '/requests/cancel',
        'httpMethod': 'PUT',
        'headers': None,
        'multiValueHeaders': None,
        'queryStringParameters': {
            'request_number': 1,

        },
        'body': {
                'request_number': 2
        }
}



authentication_request = {
   "resource":"/signin",
   "path":"/signin",
   "httpMethod":"POST",
   "headers":"None",
   "multiValueHeaders":"None",
   "queryStringParameters":"None",
   "multiValueQueryStringParameters":"None",
   "pathParameters":"None",
   "stageVariables":"None",
   "requestContext":{
      "resourceId":"efgnn5",
      "resourcePath":"/signin",
      "httpMethod":"POST",
      "extendedRequestId":"C79w1F8FIAMFy3w=",
      "requestTime":"23/Jul/2021:18:52:53 +0000",
      "path":"/signin",
      "accountId":"261044366975",
      "protocol":"HTTP/1.1",
      "stage":"test-invoke-stage",
      "domainPrefix":"testPrefix",
      "requestTimeEpoch":1627066373138,
      "requestId":"d6c2b23e-5fa0-4e3a-a8a0-ff9640c5e0ac",
      "identity":{
         "cognitoIdentityPoolId":"None",
         "cognitoIdentityId":"None",
         "apiKey":"test-invoke-api-key",
         "principalOrgId":"None",
         "cognitoAuthenticationType":"None",
         "userArn":"arn:aws:iam::261044366975:root",
         "apiKeyId":"test-invoke-api-key-id",
         "userAgent":"aws-internal/3 aws-sdk-java/1.11.1030 Linux/5.4.116-64.217.amzn2int.x86_64 OpenJDK_64-Bit_Server_VM/25.292-b10 java/1.8.0_292 vendor/Oracle_Corporation cfg/retry-mode/legacy",
         "accountId":"261044366975",
         "caller":"261044366975",
         "sourceIp":"test-invoke-source-ip",
         "accessKey":"ASIATZR3U5Z7SL3HKRMU",
         "cognitoAuthenticationProvider":"None",
         "user":"261044366975"
      },
      "domainName":"testPrefix.testDomainName",
      "apiId":"qz8a0nzf5b"
   },
   "body":"{\"email\": \"lasifo8480@luxiu2.com\",\n                \"password\": \"W7Ov3x0,\"}",

}


signup_request = {
   "resource":"/signup",
   "path":"/signup",
   "httpMethod":"POST",
   "headers":{
      "accept":"application/json, text/plain, */*",
      "accept-encoding":"gzip, deflate, br",
      "accept-language":"en-GB,en-US;q=0.9,en;q=0.8",
      "content-type":"application/json;charset=UTF-8",
      "Host":"qz8a0nzf5b.execute-api.us-east-1.amazonaws.com",
      "origin":"http://localhost:3000",
      "referer":"http://localhost:3000/",
      "sec-ch-ua":"\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
      "sec-ch-ua-mobile":"?1",
      "sec-fetch-dest":"empty",
      "sec-fetch-mode":"cors",
      "sec-fetch-site":"cross-site",
      "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36",
      "X-Amzn-Trace-Id":"Root=1-61030b6c-69c5d861756e141c6e7c3cd2",
      "X-Forwarded-For":"72.255.7.138",
      "X-Forwarded-Port":"443",
      "X-Forwarded-Proto":"https"
   },
   "multiValueHeaders":{
      "accept":[
         "application/json, text/plain, */*"
      ],
      "accept-encoding":[
         "gzip, deflate, br"
      ],
      "accept-language":[
         "en-GB,en-US;q=0.9,en;q=0.8"
      ],
      "content-type":[
         "application/json;charset=UTF-8"
      ],
      "Host":[
         "qz8a0nzf5b.execute-api.us-east-1.amazonaws.com"
      ],
      "origin":[
         "http://localhost:3000"
      ],
      "referer":[
         "http://localhost:3000/"
      ],
      "sec-ch-ua":[
         "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\""
      ],
      "sec-ch-ua-mobile":[
         "?1"
      ],
      "sec-fetch-dest":[
         "empty"
      ],
      "sec-fetch-mode":[
         "cors"
      ],
      "sec-fetch-site":[
         "cross-site"
      ],
      "User-Agent":[
         "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36"
      ],
      "X-Amzn-Trace-Id":[
         "Root=1-61030b6c-69c5d861756e141c6e7c3cd2"
      ],
      "X-Forwarded-For":[
         "72.255.7.138"
      ],
      "X-Forwarded-Port":[
         "443"
      ],
      "X-Forwarded-Proto":[
         "https"
      ]
   },
   "queryStringParameters":"None",
   "multiValueQueryStringParameters":"None",
   "pathParameters":"None",
   "stageVariables":"None",
   "requestContext":{
      "resourceId":"gawjvx",
      "resourcePath":"/signup",
      "httpMethod":"POST",
      "extendedRequestId":"DP65BGApoAMF0mw=",
      "requestTime":"29/Jul/2021:20:11:24 +0000",
      "path":"/dev/signup",
      "accountId":"261044366975",
      "protocol":"HTTP/1.1",
      "stage":"dev",
      "domainPrefix":"qz8a0nzf5b",
      "requestTimeEpoch":1627589484776,
      "requestId":"56fa7354-2ea4-4965-aba4-96f3ee31f6b9",
      "identity":{
         "cognitoIdentityPoolId":"None",
         "accountId":"None",
         "cognitoIdentityId":"None",
         "caller":"None",
         "sourceIp":"72.255.7.138",
         "principalOrgId":"None",
         "accessKey":"None",
         "cognitoAuthenticationType":"None",
         "cognitoAuthenticationProvider":"None",
         "userArn":"None",
         "userAgent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36",
         "user":"None"
      },
      "domainName":"qz8a0nzf5b.execute-api.us-east-1.amazonaws.com",
      "apiId":"qz8a0nzf5b"
   },
   "body":"{\"email\":\"shabby12993@gmail.com\",\"password\":\"Test@123\",\"first_name\":\"Shahbakht\",\"last_name\":\"Anwar\"}",
   "isBase64Encoded":"false"
}


confirm_signup_request = {
        'resource': '/confirm',
        'path': '/confirm',
        'httpMethod': 'POST',
        'headers': None,
        'multiValueHeaders': None,
        'queryStringParameters': {
        },
        'body': {
                'email': 'simol47024@britted.com',
                'verification_code': '564060'
        }
}