import psycopg2

import json

from scripts.common.RequestApiManager import RequestsApiManager
from scripts.common.OrganizationsApiManager import OrganizationsApiManager
ENDPOINT = "acms-db-main.civ4fifo57x1.us-east-1.rds.amazonaws.com"
PORT = "5432"
USR = "postgres"
REGION = "us-east-1c"
DBNAME = "main"




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
        'resource': '/organizations',
        'path': '/organizations',
        'httpMethod': 'PUT',
        'headers': None,
        'multiValueHeaders': None,
        'queryStringParameters': {},
        'body': {
            'organization_id': 1,
            'email': 'shabbysoft@gmail.com'
        },
        'multiValueQueryStringParameters': {

        }
    }

    # Parse query string parameters to make a route_key for locating function
    path = event['path']
    http_method = event['httpMethod']
    query_string_parameters = event.get('multiValueQueryStringParameters', {})
    processed_query_string_parameters = parse_querystring_parameters(query_string_parameters)
    body = event.get('body', {})
    request = {'queryStringParameters': query_string_parameters, 'body': body}
    route_key = f'method: {http_method}, path: {path}'
    conn = psycopg2.connect(host=ENDPOINT, port=PORT, database=DBNAME, user=USR, password='admin123')
    requests_api_object = OrganizationsApiManager(conn)
    endpoint_function = requests_api_object.route_table.get(route_key, None)
    print('endpoint function: ', endpoint_function)
    if endpoint_function:
        method_to_call = getattr(requests_api_object, endpoint_function)
        method_to_call(request=event)


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



def parse_querystring_parameters(querystring_parameters={}):
    if 'limit' not in querystring_parameters:
        querystring_parameters['limit'] = 10
    if 'offset' not in querystring_parameters:
        querystring_parameters['offset'] = 0


    return querystring_parameters

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
