import psycopg2
from lambdas.common.RequestApiManager import RequestsApiManager
from lambdas.common.OrganizationsApiManager import OrganizationsApiManager
from lambdas.common.AuthenticationApiManager import AuthenticationApiManager
from lambdas.common.UsersApiManager import UsersApiManager
from lambdas.common.sample_requests import *
from lambdas.common.query_maker import *

ENDPOINT = "acms-db-main.civ4fifo57x1.us-east-1.rds.amazonaws.com"
PORT = "5432"
USR = "postgres"
REGION = "us-east-1c"
DBNAME = "main"

def lambda_handler(event, context):
    try:
        event = post_member_organization
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
        body = {}
        print('event1: ', event)
        body = event.get('body', {})
        print('body: ', body, type(body))
        if body and body is not None:
            if isinstance(body, str):
                event['body'] = json.loads(body)
        query_string_parameters = event.get('multiValueQueryStringParameters')
        if query_string_parameters is None:
            event['multiValueQueryStringParameters'] = {}

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
