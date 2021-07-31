from lambdas.common.base_api_manager import BaseAPIManager
from lambdas.common.query_maker import *
from lambdas.common.UsersApiManager import UsersApiManager
import boto3
import copy;

AuthFlow = 'USER_PASSWORD_AUTH'
ClientId = '338hugd3tjgu3jepna5puq6hj'
client = boto3.client('cognito-idp')

class AuthenticationApiManager(BaseAPIManager):

    def __init__(self, conn):
        BaseAPIManager.__init__(self, conn=conn)

    @BaseAPIManager.route('/signin', 'POST')
    def post_signin_request(self,  event={}):
        try:

            body = event.get('body', {})

            required_columns = ["email", "password"]
            for column in required_columns:
                if column not in body:
                    raise Exception(f'{column} value is required')


            auth_result = client.initiate_auth(
                AuthFlow=AuthFlow,
                AuthParameters={
                    'USERNAME': body['email'],
                    'PASSWORD': body['password']
                },
                ClientId=ClientId
            )

            if auth_result['AuthenticationResult']:
                user_profile = {}
                user_profile['authenticationToken'] = auth_result.get('AuthenticationResult',{})
                user_profile['profile'] = client.get_user(AccessToken=auth_result['AuthenticationResult']['AccessToken'])
                user_profile['profile'].pop('ResponseMetadata')
                print(f'UserProfile: {user_profile}')
                http_response_object = create_http_response_object(user_profile)
                print('response_object_auth: ', http_response_object)
                return http_response_object

            http_response_object = create_http_response_object({'message': 'User confirmed successfully!'})
            return http_response_object
        except Exception as err:
            print('signinRequestException: ', err)
            raise err

    @BaseAPIManager.route('/signup', 'POST')
    def post_signup_request(self, event={}):
        try:
            event_copy = copy.deepcopy(event)
            user_manager = UsersApiManager(conn=self._conn)
            user_id = user_manager.post_users(event=event_copy)
            body = event.get('body', {})
            print(f'bodyInSignUpRequest: {body}')

            if user_id:
                user_id = user_id[0][0]
                print(f'user_id: {user_id}')
                required_columns = ["email", "password", 'first_name', 'last_name']
                print(f'body: {body}')
                for column in required_columns:
                    if column not in body:
                        raise Exception(f'{column} value is required')
                response = client.sign_up(
                            ClientId=ClientId,
                            Username=body.get('email'),
                            Password=body.get('password'),
                            UserAttributes=[
                                {
                                    'Name': 'email',
                                    'Value': body.get('email'),
                                },
                                {
                                    "Name": "custom:firstName",
                                    "Value": body.get('first_name')
                                },
                                {
                                    "Name": "custom:lastName",
                                    "Value": body.get('last_name')
                                },
                                {
                                    "Name": "custom:id",
                                    "Value": str(user_id)
                                },
                                {
                                    "Name": "custom:organizationID",
                                    "Value": ""
                                }
                            ],

                )
                print('response: ', response)
                http_response_object = create_http_response_object(
                    {'message': 'Please check email for verification code!!'})
                return http_response_object
        except Exception as err:
            print('signupRequestException: ', err)
            raise


    @BaseAPIManager.route('/confirm', 'POST')
    def post_confirm_signup_request(self, event={}):
        try:

            body = event.get('body', {})

            required_columns = ["verification_code", "email"]
            print(f'body: {body}')
            for column in required_columns:
                if column not in body:
                    raise Exception(f'{column} value is required')

            response = client.confirm_sign_up(
                        ClientId=ClientId,
                        Username=body.get('email'),
                        ConfirmationCode=body.get('verification_code'))

            print('response: ', response)
            http_response_object = create_http_response_object({'message': 'User confirmed successfully!'})
            return http_response_object
            # if auth_result['AuthenticationResult']:
            #     user_profile = {}
            #     user_profile['authenticationToken'] = auth_result.get('AuthenticationResult', {})
            #     user_profile['profile'] = client.get_user(
            #         AccessToken=auth_result['AuthenticationResult']['AccessToken'])
            #     user_profile['profile'].pop('ResponseMetadata')
            #     print(f'UserProfile: {user_profile}')
            #     http_response_object = create_http_response_object(user_profile)
            #     print('response_object_auth: ', http_response_object)
            #     return http_response_object
        except Exception as err:
            print('signupRequestException: ', err)
            raise err

    @BaseAPIManager.route('/confirm', 'POST')
    def post_confirm_signup_request(self, event={}):
        try:

            body = event.get('body', {})

            required_columns = ["verification_code", "email"]
            print(f'body: {body}')
            for column in required_columns:
                if column not in body:
                    raise Exception(f'{column} value is required')

            response = client.confirm_sign_up(
                ClientId=ClientId,
                Username=body.get('email'),
                ConfirmationCode=body.get('verification_code'))

            print('response: ', response)
            http_response_object = create_http_response_object({'message': 'User confirmed successfully!'})
            return http_response_object
            # if auth_result['AuthenticationResult']:
            #     user_profile = {}
            #     user_profile['authenticationToken'] = auth_result.get('AuthenticationResult', {})
            #     user_profile['profile'] = client.get_user(
            #         AccessToken=auth_result['AuthenticationResult']['AccessToken'])
            #     user_profile['profile'].pop('ResponseMetadata')
            #     print(f'UserProfile: {user_profile}')
            #     http_response_object = create_http_response_object(user_profile)
            #     print('response_object_auth: ', http_response_object)
            #     return http_response_object
        except Exception as err:
            print('signupRequestException: ', err)
            raise err
