import psycopg2

from lambdas.common.UsersApiManager import UsersApiManager
from lambdas.common.sample_requests import *

ENDPOINT = "acms-db-main.civ4fifo57x1.us-east-1.rds.amazonaws.com"
PORT = "5432"
USR = "postgres"
REGION = "us-east-1c"
DBNAME = "main"


# client = boto3.client('cognito-idp')
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

    event = {
        'resource': '/requests',
        'path': '/requests',
        'httpMethod': 'GET',
        'headers': None,
        'multiValueHeaders': None,
        'queryStringParameters': {
            'sampleParam': 'value1'
        },
        'multiValueQueryStringParameters': {
            'sampleParam': [
                'value1'
            ]
        }
    }



    event = {
        'resource': '/requests',
        'path': '/requests',
        'httpMethod': 'POST',
        'headers': None,
        'multiValueHeaders': None,
        'queryStringParameters': {},
        'body': {
            'organization_name': 'Shabby soft',
            'email': 'shabbysoft@gmail.com'
        },
        'multiValueQueryStringParameters': {

        }
    }

    event = {
        'resource': '/users',
        'path': '/users',
        'httpMethod': 'POST',
        'headers': None,
        'multiValueHeaders': None,
        'queryStringParameters': {},
        'body': {
            'is_admin': 'true',
            'first_name': 'Shahbakht Anwar',
            'last_name': 'Anwar',
            'email': 'shahbakht.anwar@gmail.com'
        },
        'multiValueQueryStringParameters': {

        }
    }

    event = {
        'resource': '/requests',
        'path': '/requests',
        'httpMethod': 'POST',
        'headers': None,
        'multiValueHeaders': None,
        'queryStringParameters': {},
        'body': {
            'is_admin': 'true',
            'first_name': 'Shahbakht Anwar',
            'last_name': 'Anwar',
            'email': 'shahbakht.anwar@gmail.com'
        },
        'multiValueQueryStringParameters': {

        }
    }

    event = {
        'resource': '/organizations',
        'path': '/organizations',
        'httpMethod': 'POST',
        'headers': None,
        'multiValueHeaders': None,
        'queryStringParameters': {},
        'body': {
            'organization_name': 'Shabby soft1',
            'email': 'shabbysoft@gmail.com',
            'user_id': 1,
        },
        'multiValueQueryStringParameters': {
        }
    }

    event = get_users_request
    # Parse query string parameters to make a route_key for locating function
    path = event['path']
    http_method = event['httpMethod']


    # request = {'queryStringParameters': query_string_parameters, 'body': body}
    route_key = f'method: {http_method}, path: {path}'
    conn = psycopg2.connect(host=ENDPOINT, port=PORT, database=DBNAME, user=USR, password='admin123')
    requests_api_object = UsersApiManager(conn)
    endpoint_function = requests_api_object.route_table.get(route_key, None)

    print('endpoint function: ', endpoint_function, 'route_key: ', route_key)
    if endpoint_function:
        method_to_call = getattr(requests_api_object, endpoint_function)
        print('method_to_call: ', method_to_call, 'endpointfunc: ', endpoint_function)
        http_response_object = method_to_call(event=event)
        print('httpResponseObject: ', http_response_object)
        return http_response_object


    # conn = psycopg2.connect(host=ENDPOINT, port=PORT, database=DBNAME, user=USR, password='admin123')
    # print('conntype: ', type(conn))
    # requests_api_object = RequestsApiManager(conn)

    # Create body for response object
    # responseObject = {}
    # responseObject['sampleParam'] = 1
    # responseObject['message'] = 'This is a response from API call'

    # Create Http request
    # httpObject = {}
    # httpObject['statusCode'] = 200
    # httpObject['headers'] = {}
    # httpObject['headers']['Content-type'] = 'application/json'
    # httpObject['body'] = json.dumps(responseObject)
    # return httpObject




try:
    # conn = psycopg2.connect(host=ENDPOINT, port=PORT, database=DBNAME, user=USR, password='admin123')
    # query = get_query_maker(table_name="requests", schema="acmsSchema", filter_columns=['organizationID'], filter_values=[1], filter_conditions=['='], sort_columns=["requestNumber"], order=['asc'])
    # cur = conn.cursor()
    # cur.execute(query)
    # query_results = cur.fetchall()
    # print(query_results)


    lambda_handler(None, None)

    # requests_api_object.cancel_request()
    # requests_api_object.get_requests()
    # requests_api_object.post_request()
    # requests_api_object.cancel_request()


except Exception as e:
    print("Query execution failed due to {}".format(e))
