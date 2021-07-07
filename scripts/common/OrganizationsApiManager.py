from scripts.common.base_api_manager import BaseAPIManager
from scripts.common.query_maker import *
from scripts.common import constants

class OrganizationsApiManager(BaseAPIManager):
    def __init__(self, conn):
        BaseAPIManager.__init__(self, conn=conn)

    @BaseAPIManager.route('/organizations', 'GET')
    def get_requests(self, schema="acmsSchema", table_name="organizations_v1", limit=10, querystring_parameters={}):
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

    @BaseAPIManager.route('/requests', 'POST')
    def post_request(self, schema="acmsSchema", table_name="requests", request={}):
        try:
            # Sample Request
            request = {
                "organization_name": 2,
                "email": 'family',
            }

            # Checking if all the required keys exist in the request
            required_columns = ["organization_name"]

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
