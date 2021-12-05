from lambdas.common import constants
from lambdas.common.base_api_manager import BaseAPIManager
from lambdas.common.query_maker import *

import jwt


def get_id_from_headers(event):
    try:
        headers = event.get('headers')
        if headers:
            id_token = headers.get('Authorization')
            if id_token:
                user_id = jwt.decode(id_token, options={"verify_signature": False}).get("custom:id")
                return user_id
            raise Exception(f'idToken value is required')
    except Exception as err:
        print('id_from_headers: ', err)

class RequestsApiManager(BaseAPIManager):

    def __init__(self, conn):
        BaseAPIManager.__init__(self, conn=conn)

    @BaseAPIManager.route('/request/admin', 'GET')
    def get_requests_admin(self, schema="acmsSchema", table_name="requests_v1", limit=10, event={}):
        try:
            query_string_parameters = event.get('multiValueQueryStringParameters', {})
            query_string_parameters = parse_querystring_parameters(query_string_parameters)
            # Checking if all the required keys exist in the request
            required_columns = ["organization_id"]

            for column in required_columns:
                if column not in query_string_parameters:
                    raise Exception(f'{column} value is required')
            query = get_query_maker(schema=schema, table_name=table_name,
                                    limit=query_string_parameters.get('limit', 10),
                                    offset=query_string_parameters.get('offset', 0),
                                    filter_columns=['organization_id', 'status'],
                                    filter_values=[query_string_parameters.get('organization_id', 1),
                                                   query_string_parameters.get('status', 0)],
                                    filter_conditions=['=', '='])
            print('getQueryMaker: ', query)
            results = execute_query(self._conn, query, limit, is_fetch=1)
            return results
        except Exception as err:
            print('GetRequestsException: ', err)
            raise err

    @BaseAPIManager.route('/request', 'GET')
    def get_requests(self, schema="acmsSchema", table_name="requests_v1", limit=10, event={}):
        try:
            print('event in get_requests: ', event)
            query_string_parameters = event.get('multiValueQueryStringParameters', {})
            print('qrs1: ', query_string_parameters)
            query_string_parameters = parse_querystring_parameters(query_string_parameters)
            print('qrs2: ', query_string_parameters)
            # Checking if all the required keys exist in the request
            id = get_id_from_headers(event)
            print('gettingquery: ')
            query = get_query_maker(schema=schema, table_name=table_name,
                                    limit=query_string_parameters.get('limit', 10),
                                    offset=query_string_parameters.get('offset', 0),
                                    filter_columns=['user_id', 'status'],
                                    filter_values=[id, query_string_parameters.get('status', 0)],
                                    filter_conditions=['=', '='])
            print('getQueryMaker: ', query)
            results = execute_query(self._conn, query, limit, is_fetch=1,
                                    column_names=list(constants.request_arg_types.keys()))
            http_response_object = create_http_response_object(returnDataObject=results)
            return http_response_object
        except Exception as err:
            print('GetRequestsException: ', err)
            raise err


    @BaseAPIManager.route('/request', 'POST')
    def post_request(self, schema="acmsSchema", table_name="requests_v1", event={}):
        try:

            request = event.get('body')
            id = get_id_from_headers(event)
            # Checking if all the required keys exist in the request
            required_columns = ["invitation_to", 'reason', 'status', 'invitation_date',
                                "invite_time"]

            for column in required_columns:
                if column not in request:
                    raise Exception(f'{column} value is required')

            # Checking if all the values for keys are of the desired type
            request_type_check(request, constants.post_request_arg_types)

            # If values are strings, preserve quotations for query execution
            for key in request:
                if isinstance(request[key], str):
                    request[key] = f"\'{request[key]}\'"

            # Get Organization ID for User
            user_id = id
            get_organization_id_query = """
                                        SELECT l.organization_id
                                        FROM \"{schema}\".organizations_users_link l
                                        WHERE l.user_id = {user_id}
                                        """.format(user_id=user_id, schema=schema)


            # Execute insert query. Set fetch flag to false.
            results = execute_query(self._conn, get_organization_id_query, is_fetch=1)
            if results:
                organization_id = results[0][0]

                # Format date and time according to standard
                request['invitation_date'] = f"TO_DATE({request['invitation_date']}, 'YYYYMMDD')"
                request['invite_time'] = f"TO_TIMESTAMP({request['invite_time']},'HH:MI:SS')"

                # Adding organization_id to request
                request['organization_id'] = organization_id

                # Make query for execution
                column_names = request.keys()
                values = request.values()
                query = insert_query_maker(schema_name=schema, table_name=table_name, columns=column_names,
                                           values=values)
                print('insertQuery: ', query)

                # Execute insert query. Set fetch flag to false.
                results = execute_query(self._conn, query, is_fetch=0)
                http_response_object = create_http_response_object(returnDataObject=results)
                return http_response_object


            raise Exception(f'Organization ID cant be left null')

        except Exception as err:
            print('PostRequestException: ', err)
            raise err

    @BaseAPIManager.route('/request/accept', 'PUT')
    def accept_request(self, schema='acmsSchema', table_name='requests_v1', event={}):
        try:
            request = event.get('body')
            # Checking if all the required keys exist in the request
            required_columns = ["request_number"]
            for column in required_columns:
                if column not in request:
                    raise Exception(f'{column} value is required')

            # Checking if all the values for keys are of the desired type
            request_type_check(request, constants.post_request_arg_types)

            # Add Status to Request
            request['status'] = 1

            # Removing requestNumber from request to use it as a filter
            request_number = {'request_number': request.pop('request_number')}
            filter_conditions = ['=']
            query = update_query_maker(schema_name=schema, table_name=table_name, request_body=request,
                                       filter=request_number, filter_conditions=filter_conditions)

            # Execute insert query. Set fetch flag to false.
            results = execute_query(self._conn, query, is_fetch=0)
            http_response_object = create_http_response_object(returnDataObject=results)
            return http_response_object

        except Exception as err:
            print('AcceptRequestException: ', err)
            raise err

    @BaseAPIManager.route('/request/cancel', 'PUT')
    def cancel_request(self, schema='acmsSchema', table_name='requests_v1', event={}):
        try:
            request = event.get('body')
            # Checking if all the required keys exist in the request
            required_columns = ["request_number"]
            for column in required_columns:
                if column not in request:
                    raise Exception(f'{column} value is required')

            # Checking if all the values for keys are of the desired type
            request_type_check(request, constants.post_request_arg_types)

            # Add Status to Request
            request['status'] = 2

            # Removing requestNumber from request to use it as a filter
            request_number = {'request_number': request.pop('request_number')}
            filter_conditions = ['=']
            query = update_query_maker(schema_name=schema, table_name=table_name, request_body=request,
                                       filter=request_number, filter_conditions=filter_conditions)

            # Execute insert query. Set fetch flag to false.
            results = execute_query(self._conn, query, is_fetch=0)
            print('cancelRequestQuery: ', query)
            http_response_object = create_http_response_object(returnDataObject=results)
            return http_response_object


        except Exception as err:
            print('CancelRequestException: ', err)
            raise err

