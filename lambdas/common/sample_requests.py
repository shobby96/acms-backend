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
        'headers': None,
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

get_requests = {
        'resource': '/requests',
        'path': '/requests',
        'httpMethod': 'GET',
        'headers': None,
        'multiValueHeaders': None,
        'queryStringParameters': {
            'user_id': 1
        },
        'multiValueQueryStringParameters': {
            'user_id': [1]
        }
    }


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
            'organization_id': [1]
        }
    }
post_request = {
        'resource': '/requests',
        'path': '/requests',
        'httpMethod': 'POST',
        'headers': None,
        'multiValueHeaders': None,
        'queryStringParameters': {
            'organization_id': 1
        },
        'body': {
                "user_id": 1,
                "invitation_to": 'family',
                'reason': "Site visit",
                'status': 0,
                'invitation_date': '20210103',
                "invite_time": '9:30:20',
        }
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
   "body":"{\"mail\": \"shabbyamazon@gmail.com\",\n                \"password\": \"Test@123\"}",

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