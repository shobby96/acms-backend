import psycopg2

from lambdas.common.UsersApiManager import UsersApiManager
from lambdas.common.AuthenticationApiManager import AuthenticationApiManager
from lambdas.common.OrganizationsApiManager import OrganizationsApiManager
from lambdas.common.sample_requests import *
from lambdas.common.query_maker import *

ENDPOINT = "acms-db-main.civ4fifo57x1.us-east-1.rds.amazonaws.com"
PORT = "5432"
USR = "postgres"
REGION = "us-east-1c"
DBNAME = "main"
#
# import boto3
# client = boto3.client('cognito-idp')
# user = client.get_user(AccessToken='eyJraWQiOiI4Vk5YYmRQSFd4cEFDdlVWTXVPcnpoN1Y3dllreWljMExVRDFwRzFSdUVJPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJiZDI4MDA4MC0yOTQzLTQ3MDItODE0MS0zZTE3ZGM1MmMzMTAiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiY3VzdG9tOmxhc3ROYW1lIjoiQW53YXIiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9yMU44VExxanEiLCJjb2duaXRvOnVzZXJuYW1lIjoiYmQyODAwODAtMjk0My00NzAyLTgxNDEtM2UxN2RjNTJjMzEwIiwib3JpZ2luX2p0aSI6IjZlZGY5N2JjLWViNzAtNDFiYy1hZWQxLTM5Y2Q4MGVmNjkyNCIsImF1ZCI6IjMzOGh1Z2QzdGpndTNqZXBuYTVwdXE2aGoiLCJldmVudF9pZCI6IjZmN2M2YjU2LTZlMmUtNDdlNS1iZWIxLTE3YWM3ODEzYTIwYiIsImN1c3RvbTpmaXJzdE5hbWUiOiJTaGFoYmFraHQiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTYyNjcxNDU5NSwiZXhwIjoxNjI2NzE4MTk1LCJpYXQiOjE2MjY3MTQ1OTUsImp0aSI6IjI4Y2FkNzc4LTBkZjItNGRlMS1iYmQwLTk2NGI0ZjExMzNkOCIsImVtYWlsIjoic2hhYmJ5YW1hem9uQGdtYWlsLmNvbSJ9.ZZW6W47T5rvzLA6jNSCMlrPkE-F9JxMGi5O35-7yYT71bdF2ulloGzh2be2szYjqxYtxeAqrHv9cH9nbqD1vB8XvSdvJuoLYQCEcliC0qMvzAGgC2BeZ5DS90EiiPDn0l4dP1l1h4rluRnWJAUZeaGi6IJdyCxIE9jR6pz6N-2YVzwRoHj90jtPjMmVOzaRWoeMKP1AZUEP17dubiQE20U6LLq0JjICGl3LDnF0cgxq7Pvk8L-Eq48HMXv3moUZQI20KQOZHlSPEAbT2z7zc7yDFxq5Nrq6sIRLLtp1gZVYmtuSg3LtyTSwYMuhkBb26XPsuR_Et7xB1qfIAbtRFKg')
# user_pools = client.initiate_auth(
# AuthFlow='USER_PASSWORD_AUTH',
# AuthParameters={
#         'USERNAME': 'shabbyamazon@gmail.com',
#         'PASSWORD': 'Test@123',
#
#     },
# ClientId = '338hugd3tjgu3jepna5puq6hj'
# )
# print('Auth: ', user_pools)
# user = client.get_user(AccessToken=user_pools['AuthenticationResult']['AccessToken'])
# print('user', user)
def lambda_handler(event, context):
    try:
        # event = post_organizations_request
        print("event: ", event)
        # Parse event to make a route_key for locating function
        path = event['path']
        http_method = event['httpMethod']
        route_key = f'method: {http_method}, path: {path}'

        # Initiating connection with DB and initializing base class
        conn = psycopg2.connect(host=ENDPOINT, port=PORT, database=DBNAME, user=USR, password='admin123')
        requests_api_object = OrganizationsApiManager(conn)
        endpoint_function = requests_api_object.route_table.get(route_key, None)

        print('endpoint function: ', endpoint_function, 'route_key: ', route_key)

        # Converting Body to json
        body = event.get('body', {})
        if body and isinstance(body, str):
            event['body'] = json.loads(body)
            print('event ', event)
        # If a function is located in the route table, call it with event as a parameter
        if endpoint_function:
            method_to_call = getattr(requests_api_object, endpoint_function)
            print('method_to_call: ', method_to_call, 'endpointfunc: ', endpoint_function)
            http_response_object = method_to_call(event=event)
            print('httpResponseObject: ', http_response_object)
            return http_response_object
    except Exception as err:
        errorString = str(err)
        errorObject = result_list_to_object(data_rows=[[errorString]], column_names=['error'])
        http_response_object = create_http_response_object(returnDataObject=errorObject, status_code=400)
        print(f'HttpResponse: {http_response_object}')
        return http_response_object




def main():
    try:
        lambda_handler(None, None)
    except Exception as e:
        print("Query execution failed due to {}".format(e))


if __name__ == '__main__':
    main()
