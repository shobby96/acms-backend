import psycopg2
from scripts.common import constants
from scripts.common.base_api_manager import BaseAPIManager
from scripts.common.query_maker import *
import json

ENDPOINT = "acms-db-main.civ4fifo57x1.us-east-1.rds.amazonaws.com"
PORT = "5432"
USR = "postgres"
REGION = "us-east-1c"
DBNAME = "main"


class RequestsApiManager(BaseAPIManager):

    def __init__(self, conn):
        BaseAPIManager.__init__(self, conn=conn)

    @BaseAPIManager.route('/requests', 'GET')
    def get_requests(self, schema="acmsSchema", table_name="requests", limit=10, request={}):
        try:
            query = get_query_maker(schema=schema, table_name=table_name)
            results = execute_query(self._conn, query, limit)
            return results
        except Exception as err:
            print('GetRequestsException: ', err)
            raise err

    @BaseAPIManager.route('/requests', 'POST')
    def post_request(self, schema="acmsSchema", table_name="requests", request={}):
        try:
            # Sample Request
            request = {"userID": 2,
                       "invitationTo": 'family',
                       'reason': "Site visit",
                       'status': 0,
                       'date': '20170103',
                       "timeOfArrival": '9:30:20',
                       "organizationID": 1}

            # Checking if all the required keys exist in the request
            required_columns = ["userID", "invitationTo", 'reason', 'status', 'date',
                                "timeOfArrival", "organizationID"]

            for column in required_columns:
                if column not in request:
                    raise Exception(f'{column} value is required')

            # Checking if all the values for keys are of the desired type
            request_type_check(request, constants.post_request_arg_types)

            # If values are strings, preserve quotations for query execution
            for key in request:
                if isinstance(request[key], str):
                    request[key] = f"\'{request[key]}\'"

            # Format date and time according to standard
            request['date'] = f"TO_DATE({request['date']}, 'YYYYMMDD')"
            request['timeOfArrival'] = f"TO_TIMESTAMP({request['timeOfArrival']},'HH:MI:SS')"

            # Make query for execution
            column_names = request.keys()
            values = request.values()
            query = insert_query_maker(schema_name=schema, table_name=table_name, columns=column_names, values=values)
            print('insertQuery: ', query)

            # Execute insert query. Set fetch flag to false.
            execute_query(self._conn, query, is_fetch=0)

        except Exception as err:
            print('PostRequestException: ', err)
            raise err

    @BaseAPIManager.route('/requests/accept', 'PUT')
    def accept_request(self, schema='acmsSchema', table_name='requests', request={}):
        try:
            # Sample request
            request = {
                'requestNumber': 1,
            }

            # Checking if all the desired keys in the request
            required_columns = ['requestNumber']
            for column in required_columns:
                if column not in request:
                    raise Exception(f'{column} value is required')

            # Add Status to Request
            request['status'] = 1

            # Removing requestNumber from request to use it as a filter
            request_number = {'requestNumber': request.pop('requestNumber')}
            filter_conditions = ['=']
            query = update_query_maker(schema_name=schema, table_name=table_name, request_body=request,
                                       filter=request_number, filter_conditions=filter_conditions)
            print('acceptQuery: ', query)

        except Exception as err:
            print('AcceptRequestException: ', err)
            raise err

    @BaseAPIManager.route('/requests/cancel', 'PUT')
    def cancel_request(self, schema='acmsSchema', table_name='requests', request={}):
        try:
            # Sample Request
            request = {
                'requestNumber': 1,
                'cancellationReason': 'Not available'
            }

            # Checking if all the desired keys in the request
            required_columns = ['cancellationReason', 'requestNumber']
            for column in required_columns:
                if column not in request:
                    raise Exception(f'{column} value is required')

            # Add Status to Request
            request['status'] = 2

            # If values are strings, preserve quotations for query execution
            for key in request:
                if isinstance(request[key], str):
                    request[key] = f"\'{request[key]}\'"

            # Removing requestNumber from request to use it as a filter
            request_number = {'requestNumber': request.pop('requestNumber')}
            filter_conditions = ['=']
            query = update_query_maker(schema_name=schema, table_name=table_name, request_body=request,
                                       filter=request_number, filter_conditions=filter_conditions)

            print('Update Query: ', query)
            # Execute update query. Set fetch flag to false
            execute_query(self._conn, query, is_fetch=0)

        except Exception as err:
            print('CancelRequestException: ', err)
            raise err


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

    # Parse query string parameters to make a route_key for locating function
    path = event['path']
    http_method = event['httpMethod']
    query_string_parameters = event.get('multiValueQueryStringParameters', {})
    body = event.get('body', {})
    request = {'queryStringParameters': query_string_parameters, 'body': body}
    route_key = f'method: {http_method}, path: {path}'
    conn = psycopg2.connect(host=ENDPOINT, port=PORT, database=DBNAME, user=USR, password='admin123')
    requests_api_object = RequestsApiManager(conn)
    endpoint_function = requests_api_object.route_table.get(route_key, None)
    print('endpoint function: ', endpoint_function)
    if endpoint_function:
        method_to_call = getattr(requests_api_object, endpoint_function)
        print('methodtoCall: ', method_to_call)
        # method_to_call(request=request)


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
