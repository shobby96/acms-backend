from lambdas.common.base_api_manager import BaseAPIManager
from lambdas.common.query_maker import *
from lambdas.common import constants


class UsersApiManager(BaseAPIManager):

    def __init__(self, conn):
        BaseAPIManager.__init__(self, conn=conn)

    @BaseAPIManager.route('/users', 'GET')
    def get_users(self, schema="acmsSchema", table_name="users_v1", limit=10, event={}):
        try:

            query_string_parameters = event.get('multiValueQueryStringParameters', {})
            query_string_parameters = parse_querystring_parameters(query_string_parameters)


            # Checking if all the required keys exist in the request
            required_columns = ['organization_id']
            for column in required_columns:
                if column not in query_string_parameters:
                    raise Exception(f'{column} value is required')

            # Checking if all the values for keys are of the desired type
            request_type_check(query_string_parameters, constants.users_arg_types)

            organization_id = query_string_parameters.get('organization_id')

            query = """SELECT * 
                    FROM "acmsSchema".organizations_users_link l
                    INNER JOIN "acmsSchema".organizations_v1 USING (organization_id)
                    INNER JOIN "acmsSchema".users_v1 USING (user_id)
                    WHERE l.organization_id = {organization_id}
                    LIMIT {limit}
                    OFFSET {offset};""".format(organization_id=organization_id,
                                               limit=query_string_parameters.get('limit', 10),
                                               offset=query_string_parameters.get('offset', 0))

            # query = get_query_maker(schema=schema, table_name=table_name,
            #                         limit=query_string_parameters.get('limit', 10),
            #                         offset=query_string_parameters.get('offset', 0),
            #                         filter_columns=['user_id'],
            #                         filter_values=[query_string_parameters.get('user_id', '1')],
            #                         filter_conditions=['='])

            print('query: ', query)
            results = execute_query(self._conn, query, limit, column_names=constants.users_arg_types)
            http_response_object = create_http_response_object(returnDataObject=results)
            return http_response_object
        except Exception as err:
            print('GetRequestsException: ', err)
            raise err

    @BaseAPIManager.route('/users', 'POST')
    def post_users(self, schema="acmsSchema", table_name="users_v1", event={}):
        try:
            # Sample Request
            body = event.get('body')

            # Checking if all the required keys exist in the request
            required_columns = ['first_name', 'last_name']

            for column in required_columns:
                if column not in body:
                    raise Exception(f'{column} value is required')

            # Checking if all the values for keys are of the desired type
            request_type_check(body, constants.post_organization_arg_types)

            # If values are strings, preserve quotations for query execution
            for key in body:
                if isinstance(body[key], str):
                    body[key] = f"\'{body[key]}\'"

            body['is_admin'] = True

            # Filtering request to keep only attributes in table
            filtered_body = {}
            for key in body:
                if key in constants.users_arg_types:
                    filtered_body[key] = body[key]


            # Make query for execution
            column_names = filtered_body.keys()
            values = filtered_body.values()
            query = insert_query_maker(schema_name=schema, table_name=table_name,
                                       columns=column_names,
                                       values=values,
                                       return_column_name='user_id')
            print('insertQuery: ', query)

            # Execute insert query. Set fetch flag to true.
            results = execute_query(self._conn, query, is_fetch=1)
            return results

        except Exception as err:
            print('PostRequestException: ', err)
            raise err

    @BaseAPIManager.route('/users/add', 'POST')
    def add_users(self, schema="acmsSchema", table_name="users_v1", event={}):
        try:
            # Sample Request
            body = event.get('body')
            # request = {
            #     "organization_name": 2,
            #     "email": 'family',
            # }
            headers = event.get('headers')

            object_contains(required_columns=['organizationID'], object=headers)
            # Checking if all the required keys exist in the request
            required_columns = ['first_name', 'last_name']

            for column in required_columns:
                if column not in body:
                    raise Exception(f'{column} value is required')

            # Checking if all the values for keys are of the desired type
            request_type_check(body, constants.post_organization_arg_types)

            # If values are strings, preserve quotations for query execution
            for key in body:
                if isinstance(body[key], str):
                    body[key] = f"\'{body[key]}\'"

            # Format date and time according to standard
            # request['date'] = f"TO_DATE({request['date']}, 'YYYYMMDD')"
            # request['timeOfArrival'] = f"TO_TIMESTAMP({request['timeOfArrival']},'HH:MI:SS')"
            body['is_admin'] = False

            # Make query for execution
            column_names = body.keys()
            values = body.values()
            query = insert_query_maker(schema_name=schema, table_name=table_name, columns=column_names, values=values)
            print('insertQuery: ', query)

            # Execute insert query. Set fetch flag to false.
            execute_query(self._conn, query, is_fetch=0)

        except Exception as err:
            print('PostRequestException: ', err)
            raise err
