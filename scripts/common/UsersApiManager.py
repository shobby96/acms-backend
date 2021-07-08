from scripts.common.base_api_manager import BaseAPIManager
from scripts.common.query_maker import *
from scripts.common import constants

class UsersApiManager(BaseAPIManager):

    def __init__(self, conn):
        BaseAPIManager.__init__(self, conn=conn)

    @BaseAPIManager.route('/users', 'GET')
    def get_users(self, schema="acmsSchema", table_name="users_v1", limit=10, querystring_parameters={}):
        try:

            query = get_query_maker(schema=schema, table_name=table_name,
                                    limit=querystring_parameters.get('limit', 10),
                                    offset=querystring_parameters.get('offset', 0),
                                    filter_columns=['user_id'],
                                    filter_values=[querystring_parameters.get('user_id', '1')],
                                    filter_conditions=['='])

            print('query: ', query)
            results = execute_query(self._conn, query, limit)
            return results
        except Exception as err:
            print('GetRequestsException: ', err)
            raise err

    @BaseAPIManager.route('/users', 'POST')
    def post_users(self, schema="acmsSchema", table_name="users_v1", request={}):
        try:
            # Sample Request
            request = request.get('body')
            # request = {
            #     "organization_name": 2,
            #     "email": 'family',
            # }

            # Checking if all the required keys exist in the request
            required_columns = ["is_admin", 'first_name', 'last_name', 'organization_id']

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
