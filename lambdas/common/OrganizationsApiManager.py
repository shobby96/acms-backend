from lambdas.common.base_api_manager import BaseAPIManager
from lambdas.common.query_maker import *
from lambdas.common import constants
import boto3

AuthFlow = 'USER_PASSWORD_AUTH'
ClientId = '338hugd3tjgu3jepna5puq6hj'
client = boto3.client('cognito-idp')

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

    @BaseAPIManager.route('/organizations/id', 'GET')
    def get_organization(self, schema="acmsSchema", table_name="organizations_v1", limit=10,
                          event={}):
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
                                    filter_columns=['organization_id'],
                                    filter_values=[query_string_parameters.get('organization_id', 1)],
                                    filter_conditions=['='])
            print('query: ', query)
            results = execute_query(self._conn, query, limit, column_names=constants.organization_arg_types)
            http_response_object = create_http_response_object(returnDataObject=results)
            return http_response_object

        except Exception as err:
            print('GetRequestsException: ', err)
            raise err

    @BaseAPIManager.route('/organizations', 'POST')
    def post_organization(self, schema="acmsSchema", table_name="organizations_v1", event={}):
        try:
            request = event.get('body')
            print('body: ', request)
            # Checking if all the required keys exist in the request
            required_columns = ["organization_name", "user_id"]

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

            # Removing user_id from request to use it as a filter
            user_id = request.pop('user_id')

            # Make query for execution
            column_names = request.keys()
            values = request.values()
            query = insert_query_maker(schema_name=schema, table_name=table_name, columns=column_names,
                                       values=values, return_column_name='organization_id')
            print('insertQuery: ', query)

            # Execute insert query. Set fetch flag to false.
            results = execute_query(self._conn, query, is_fetch=1, autocommit=0)
            print(f'results: {results}')
            if results:
                organization_id = results[0][0]

                # Execute insert query for Link Table
                query = insert_query_maker(schema_name=schema, table_name='organizations_users_link',
                                           columns=['organization_id', 'user_id'],
                                           values=[organization_id, user_id])
                results = execute_query(self._conn, query, is_fetch=0, autocommit=1)
                http_response_object = create_http_response_object(returnDataObject=results)

                response = client.update_user_attributes(
                    UserAttributes=[
                        {
                            "Name": "custom:organizationID",
                            "Value": str(organization_id)
                        }
                    ],
                    AccessToken=event.get('headers').get('accesstoken', '')
                )


                return http_response_object

            self._conn.rollback()
        except Exception as err:
            print('PostRequestException: ', err)
            raise err



    @BaseAPIManager.route('/organizations', 'PUT')
    def put_organizations(self, schema='acmsSchema', table_name='organizations_v1', event={}):
        try:
            # Sample request
            # request = {
            #     'requestNumber': 1,
            # }
            request = event.get('body')

            # Checking if all the desired keys in the request
            required_columns = ['email', 'organization_id']
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
            organization_id = {'organization_id': request.pop('organization_id')}
            print(f"organizationID: {organization_id}")
            filter_conditions = ['=']
            query = update_query_maker(schema_name=schema, table_name=table_name, request_body=request,
                                       filter=organization_id, filter_conditions=filter_conditions)
            print('acceptQuery: ', query)
            results = execute_query(self._conn, query, is_fetch=0)
            http_response_object = create_http_response_object(returnDataObject=results)
            return http_response_object
        except Exception as err:
            print('AcceptRequestException: ', err)
            raise err
