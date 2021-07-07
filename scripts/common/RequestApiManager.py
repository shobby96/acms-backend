
from scripts.common import constants
from scripts.common.base_api_manager import BaseAPIManager
from scripts.common.query_maker import *


class RequestsApiManager(BaseAPIManager):

    def __init__(self, conn):
        BaseAPIManager.__init__(self, conn=conn)

    @BaseAPIManager.route('/requests', 'GET')
    def get_requests(self, schema="acmsSchema", table_name="requests_v1", limit=10, request={}):
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

