from lambdas.common.base_api_manager import BaseAPIManager
from lambdas.common.query_maker import *
from lambdas.common import constants
import boto3
import copy
from lambdas.common.UsersApiManager import UsersApiManager

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

            # Removing organizationID from request to use it as a filter
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

    @BaseAPIManager.route('/organizations/addMember', 'POST')
    def post_member(self, schema='acmsSchema', table_name='organizations_v1', event={}):
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
            # for key in request:
            #     if isinstance(request[key], str):
            #         request[key] = f"\'{request[key]}\'"

            # Removing organizationID from request to use it as a filter
            organization_id = request.pop('organization_id')
            email_addr = request.get('email')
            print(f"organizationID: {str(organization_id)}")
            print(f"email: {email_addr}")
            response = client.admin_create_user(
                UserPoolId='us-east-1_r1N8TLqjq',
                # ClientId=ClientId,
                Username=str(email_addr),
                UserAttributes=[
                    {
                        'Name': 'email',
                        'Value': str(email_addr)
                    },
                    {
                        "Name": "custom:organizationID",
                        "Value": str(organization_id)
                    }
                ],
                DesiredDeliveryMediums=[
                    'EMAIL',
                ],

            )
            print(f"response: {response}")
            # filter_conditions = ['=']
            # query = update_query_maker(schema_name=schema, table_name=table_name, request_body=request,
            #                            filter=organization_id, filter_conditions=filter_conditions)
            # print('acceptQuery: ', query)
            # results = execute_query(self._conn, query, is_fetch=0)
            # http_response_object = create_http_response_object(returnDataObject=results)
            # return http_response_object
        except Exception as err:
            print('AcceptRequestException: ', err)
            raise err

    @BaseAPIManager.route('/organizations/confirmMember', 'POST')
    def confirmMember(self, schema='acmsSchema', table_name='organizations_v1', event={}):
        try:
            print('schema: ', schema)

            request = event.get('body')

            # Checking if all the desired keys in the request
            required_columns = ['session', 'first_name', 'last_name']
            for column in required_columns:
                if column not in request:
                    raise Exception(f'{column} value is required')


            response = client.respond_to_auth_challenge(
                ClientId=ClientId,
                ChallengeName='NEW_PASSWORD_REQUIRED',
                Session=request.get('session'),
                ChallengeResponses={
                    'NEW_PASSWORD': request.get('password'),
                    'USERNAME': request.get('email')
                },
            )

            event_copy = copy.deepcopy(event)
            user_manager = UsersApiManager(conn=self._conn)
            user_id = user_manager.post_users(event=event_copy)
            if user_id:
                user_id = user_id[0][0]
                response = client.admin_update_user_attributes(
                    UserPoolId='us-east-1_r1N8TLqjq',
                    Username=request.get('email'),
                    UserAttributes=[
                        {
                            'Name': 'email',
                            'Value': request.get('email'),
                        },
                        {
                            "Name": "custom:firstName",
                            "Value": request.get('first_name')
                        },
                        {
                            "Name": "custom:lastName",
                            "Value": request.get('last_name')
                        },
                        {
                            "Name": "custom:id",
                            "Value": str(user_id)
                        },

                    ]
                )
                print(f"response: {response}")

        except Exception as err:
            print('ConfirmMemberException: ', err)