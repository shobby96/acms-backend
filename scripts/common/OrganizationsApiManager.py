from scripts.common.base_api_manager import BaseAPIManager
from scripts.common.query_maker import *
from scripts.common import constants

class OrganizationsApiManager(BaseAPIManager):
    def __init__(self, conn):
        BaseAPIManager.__init__(self, conn=conn)

    @BaseAPIManager.route('/organizations', 'GET')
    def get_organizations(self, schema="acmsSchema", table_name="organizations_v1", limit=10, querystring_parameters={}):
        try:

            query = get_query_maker(schema=schema, table_name=table_name,
                                    limit=querystring_parameters.get('limit', 10),
                                    offset=querystring_parameters.get('offset', 0),
                                    filter_columns=['organization_name'],
                                    filter_values=[querystring_parameters.get('organization_name', 'SEPTEM SYSTEMS')],
                                    filter_conditions=['='])

            print('query: ', query)
            results = execute_query(self._conn, query, limit)
            return results
        except Exception as err:
            print('GetRequestsException: ', err)
            raise err

    @BaseAPIManager.route('/organizations', 'POST')
    def post_organizations(self, schema="acmsSchema", table_name="organizations_v1", request={}):
        try:
            # Sample Request
            request = request.get('body')
            # request = {
            #     "organization_name": 2,
            #     "email": 'family',
            # }

            # Checking if all the required keys exist in the request
            required_columns = ["organization_name"]

            for column in required_columns:
                if column not in request:
                    raise Exception(f'{column} value is required')

            # Checking if all the values for keys are of the desired type
            request_type_check(request, constants.post_organization_arg_types)

            # If values are strings, preserve quotations for query execution
            for key in request:
                if isinstance(request[key], str):
                    request[key] = f"\'{request[key]}\'"

            # Format date and time according to standard
            # request['date'] = f"TO_DATE({request['date']}, 'YYYYMMDD')"
            # request['timeOfArrival'] = f"TO_TIMESTAMP({request['timeOfArrival']},'HH:MI:SS')"

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



    @BaseAPIManager.route('/organizations', 'PUT')
    def put_organizations(self, schema='acmsSchema', table_name='organizations_v1', request={}):
        try:
            # Sample request
            # request = {
            #     'requestNumber': 1,
            # }
            request = request.get('body')

            # Checking if all the desired keys in the request
            required_columns = ['email']
            for column in required_columns:
                if column not in request:
                    raise Exception(f'{column} value is required')

            # Add Status to Request
            # request['status'] = 1

            # If values are strings, preserve quotations for query execution
            for key in request:
                if isinstance(request[key], str):
                    request[key] = f"\'{request[key]}\'"

            # Removing requestNumber from request to use it as a filter
            request_number = {'organization_id': request.pop('organization_id')}
            filter_conditions = ['=']
            query = update_query_maker(schema_name=schema, table_name=table_name, request_body=request,
                                       filter=request_number, filter_conditions=filter_conditions)
            print('acceptQuery: ', query)
            execute_query(self._conn, query, is_fetch=0)
        except Exception as err:
            print('AcceptRequestException: ', err)
            raise err
