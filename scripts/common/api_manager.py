import inspect
import json
import os
import requests
from boto3 import session
from lambdas.common.logger import Logger
from aws_requests_auth.boto_utils import BotoAWSRequestsAuth
from lambdas.common.constants import Constants


class APIManager(object):
    """
        This class serves as the base class for all the module level API Managers.

    This class is used both by Clients as well as Servers.

    This code handles both the local and remote use of the service.
    Local Mode is for testing server calls locally. In local mode, much of what the API Gateway does is faked.
    Remote Mode is for sending client calls to AWS lambda and receive the response from Lambda.
    """

    _api_url = ""
    _route_table = {}
    _function_names = {}
    _test = False
    _api_host = ""

    def __init__(self, test=False, api_url=""):
        """
        Constructor for the base API Manager. It handles authorization from API Gateway for subsequent calls

        :param test: It decides the mode of api manager. False means Remote Mode, True means Local Mode
        :type test: bool
        :param api_url: It is the API Gateway Endpoint URL
        :type api_url: str
        """
        try:
            # Replace private_dns_name with public_dns_name if we add api_public_dns environment variable,
            # to make API calls from local machine
            if os.environ.get('api_public_dns'):  # 'https://vpce-03df3a7d4b2e8a693-jqpydd82.execute-api.us-east-1.vpce.amazonaws.com/v1'
                self._api_url = "https://" + os.environ.get('api_public_dns') + "/v1"
            else:
                self._api_url = api_url
            self._api_host= api_url.split('/')[2]
            self._route_table = {}
            self._test = test
            self._session = session.Session()
            self._auth = BotoAWSRequestsAuth(aws_host=self._api_host, aws_region=self._session.region_name ,aws_service='execute-api')
        except Exception as ex:
            print("Exception occurred: " + str(ex))
            raise

    def get_http_error(self):
        """
        It returns the default Error Class to be raised as base implementation

        :return: default Error Class
        :rtype: object
        """
        return requests.exceptions.HTTPError

    def get_connection_error(self):
        """
        It returns the default Error Class to be raised as base implementation

        :return: default Error Class
        :rtype: object
        """
        return requests.exceptions.ConnectionError

    @classmethod
    def route(cls, path, method):
        """
        This is the decorator factory method

        :param path: path of the API
        :type path: str
        :param method: API method type e.g. GET, POST, PUT
        :type method: str
        :return: decorator function
        :rtype: function
        """
        def real_decorator(function_):
            """
            This decorator method actually decorates the API methods.
            It sets up two things: 1) _route_table 2) _function_names
            _route_table & _function_names has information of following:
            1) Class Name 2) Function Name 3) Arguments of the Function 4) API Method 5) API Path

            :param function_: function to be decorated
            :type function_: function
            :return: decorated function
            :rtype: function
            """
            # setting up frame
            formal_arguments = {}

            # inspect the signature and populate formal_arguments dictionary
            signature = inspect.signature(function_)  # of the form --> (self, x, y, z=None)
            for param in signature.parameters.values():
                if param.name not in ['self', 'cls']:  # ignore self/cls arguments
                    # add the element in formal_arguments dictionary having
                    # key = parameter_name, value = default_value, if any, otherwise None
                    if param.default == inspect._empty and param.name:
                        formal_arguments[param.name] = None
                    else:
                        formal_arguments[param.name] = param.default
            # print('formal arguments: ', formal_arguments)
            # print(function.__name__, inspect.signature(function))
            frame = {'Function': function_, 'Method': method, 'Path': path,
                     'Class': None, 'Args': formal_arguments}

            # populating _route_table
            cls._route_table[(path, method)] = frame

            # populating _function_name
            base_class = str(function_).split(' ')[1].split('.')[0]
            if (function_.__name__, base_class) in cls._function_names:
                print("DUPLICATE FUNCTION NAME {}".format(function_.__name__))
            cls._function_names[(function_.__name__, base_class)] = frame

            # wrapper for the decorator
            def wrapper(*args, **kwargs):
                result = function_(*args, **kwargs)
                return result

            return wrapper

        return real_decorator

    def _get_frame(self, path, method):
        """
        Getter of frame from _route_table

        :param path: path of the API
        :type path: str
        :param method: API method type e.g. GET, POST, PUT
        :type method: str
        :return: frame dictionary
        :rtype: dict
        """
        return self.__class__._route_table[(path, method)]

    def handle(self, instance, path, method, event):
        """
        This method calls the actual backend handler function of the API

        :param instance: the subclass of the API Manager
        :type instance: APIManager
        :param path: path of the API
        :type path: str
        :param method: API method type e.g. GET, POST, PUT
        :type method: str
        :param event: input dictionary
        :type event: dict
        :return: the response of the API call
        :rtype: dict
        """
        # print('handle:: ', instance, path, method, event)

        # Get Function name
        frame = self._get_frame(path, method)
        func = frame['Function']
        Logger.log(method=func.__name__)

        # convert input to dictionary, if it is not already a dictionary
        if isinstance(event, str):
            if event == "":
                event = "{}"
            event = json.loads(event)

        # Prepare keyword arguments for the function
        kw = {}
        for parameter_name, default_value in frame['Args'].items():
            if event is not None and parameter_name in event:
                kw[parameter_name] = event[parameter_name]
            else:
                print("MISSING ARG {} {} {} {}".format(path, method, event, parameter_name))
                kw[parameter_name] = default_value

        # Add arbitrary keyword arguments
        if 'kwargs' in frame['Args'] and event is not None:
            kw.pop('kwargs', None)
            for parameter in event:
                if parameter not in kw:
                    kw[parameter] = event[parameter]

        # Call the actual function
        result = func(instance, **kw)
        return result

    def dump_table(self):
        """
        Method for dumping route table _route_table

        :return: None
        :rtype: None
        """
        print(self.__class__._route_table)

    def lambda_handler(self, instance, event, _context):
        """
        This method serves as the base class implementation of the API call handler that is called from subclasses

        :param instance: the subclass of the API Manager
        :type instance: APIManager
        :param event: input dictionary
        :type event: dict
        :param _context: context dictionary
        :type _context: dict
        :return: the response of the API call
        :rtype: dict
        """

        print("IN LAMBDA_HANDLER\n", instance, event, _context, sep='\n')
        path = event['path']
        method = event['httpMethod']
        print(path, method)
        if method in ['POST', 'PUT']:
            arguments = event['body']
        else:
            arguments = event['queryStringParameters']
        header_validation_status = self.get_headers_validation_status(event.get('headers'))
        if header_validation_status['statusCode'] == 200:
            return self.add_response_headers(
                self.handle(instance, path, method, arguments))
        else:
            return self.add_response_headers({
                Constants.STATUSCODE: header_validation_status['statusCode'],
                Constants.BODY: json.dumps(header_validation_status['body'])
            })

    def request(self, method, path, **kwargs):
        """
        This method makes the API calls as Client. It works in both modes.
        Remote Mode (self._test = False) (If part)
        Local Mode (self._test = True) (Else part)

        :param method: the method that makes the API call
        :type method: function
        :param path: path of the API
        :type path: str
        :param kwargs: keywords arguments
        :type kwargs: dict
        :return: response of the API call
        :rtype: dict
        """
        print('test api')
        if not self._test:  # Remote Mode
            try:
                print('request:: method.__name__:', method.__name__, ' path:', path)
                response = method(path, **kwargs)

                print(response.status_code, response.reason)
                response.raise_for_status()

                if isinstance(response.text, dict):
                    return response.text
                return json.loads(response.text)
            except(requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as error:
                if method.__name__.upper() == 'GET':
                    arguments = kwargs['params']
                else:
                    arguments = kwargs['data']

                arguments_dump = json.dumps(arguments).replace('null', '\"None\"').replace("'", '"')
                print("Arguments_dump = ", arguments_dump)
                try:
                    if len(arguments_dump) > 200:  # truncating lengthy args to satisfy step function character limit
                        arguments_dump = "{}"
                    arguments_dict = json.loads(arguments_dump)
                except ValueError:
                    arguments_dict = {}
                response_dictionary = None
                status_code = None
                if response is not None:
                    response_dictionary = response.text
                    print("response.text = ", response.text)
                    status_code = response.status_code
                    if not isinstance(response.text, dict):
                        response_dictionary = json.loads(response.text.replace("'", '`'), strict=False)
                        print("response_dictionary = ", response_dictionary)

                        if not isinstance(response_dictionary, dict):
                            response_dictionary = {"Message": response.text}
                            print("response_dictionary created = ", response_dictionary)

                print("Arguments_dict = ", arguments_dict)
                # print("Arguments_dict_str = ", str(arguments_dict))
                http_error_msg = '\"Body\": {0}, \"StatusCode\": \"{1}\", \"URL\": \"{2}\", \"Arguments\": {3}' \
                    .format(response_dictionary, status_code, path, arguments_dict)
                http_error_msg = "{" + http_error_msg + "}"
                http_error_msg = http_error_msg.replace("'", '"')
                print("http_error_msg = ", http_error_msg)

                if type(error).__name__ == 'ConnectionError':
                    raise self.get_connection_error()(http_error_msg).with_traceback(error.__traceback__) from error
                raise self.get_http_error()(http_error_msg).with_traceback(error.__traceback__) from error
            except Exception as error:
                print("Unhandled Exception occurred in API Manager = ", str(error))
                raise
        else:  # Local Mode
            method = method.__name__.upper()
            if self._api_url:
                path = path.split(self._api_url, 1)[1]

            if method == 'GET':
                arguments = kwargs['params']
            else:
                arguments = kwargs['data']

            response = self.handle(self, path, method, arguments)

            status_code = response['statusCode']
            response = response['body']

            if not isinstance(response, dict):
                response = json.loads(response.replace("'", '`'))
            print('request::response =:', response)

            if 400 <= status_code < 600:
                arguments_dump = json.dumps(arguments).replace('null', '\"None\"').replace("'", '"')
                print("Arguments_dump = ", arguments_dump)
                try:
                    arguments_dict = json.loads(arguments_dump)
                except ValueError:
                    arguments_dict = {}
                print("Arguments_dict = ", arguments_dict)
                print("Arguments_dict_str = ", str(arguments_dict))
                http_error_msg = '\"Body\": {0}, \"StatusCode\": \"{1}\", \"URL\": \"{2}\", \"Arguments\": {3}'\
                    .format(response, status_code, path, arguments_dict)
                http_error_msg = "{" + http_error_msg + "}"
                http_error_msg = http_error_msg.replace("'", '"')
                print("http_error_msg = ", http_error_msg)

                raise self.get_http_error()(http_error_msg)

            return response

    def remote(self, *args, **kwargs):
        """
        This method is called from the Client.
        It prepares the arguments for request method, calls the Server and returns the response back to the Client

        :param args: positional arguments
        :type args: tuple
        :param kwargs: keywords arguments
        :type kwargs: dict
        :return: response of the API call
        :rtype: dict
        """
        frame = self.current_frame
        data = {}
        method = frame['Method']
        formal_args = frame['Args']
        i = 0
        print('remote:: method:', method, 'formal_args:', formal_args, 'path:', frame['Path'])

        for k in formal_args:
            if k in kwargs:
                data[k] = kwargs[k]
            elif i < args.__len__():
                data[k] = args[i]
                i += 1
        if 'kwargs' in formal_args and kwargs is not None:
            for key in kwargs:
                if key not in data:
                    data[key] = kwargs[key]
        try:
            if method == 'POST':
                response = self.request(requests.post,
                                        self._api_url + frame['Path'],
                                        auth=self._auth,
                                        data=json.dumps(data),
                                        headers={'content-type': 'application/json', 'Host': self._api_host})
            elif method == 'PUT':
                response = self.request(requests.put,
                                        self._api_url + frame['Path'],
                                        auth=self._auth,
                                        data=json.dumps(data),
                                        headers={'content-type': 'application/json', 'Host': self._api_host})
            elif method == 'GET':
                response = self.request(requests.get,
                                        self._api_url + frame['Path'],
                                        auth=self._auth,
                                        params=data,
                                        headers={'content-type': 'application/json', 'Host': self._api_host})
            else:
                response = "Unknown method {}".format(frame['Method'])
                raise Exception(response)
        except Exception:
            raise


        return response

    def add_response_headers(self, response):
        """
        This function append the response headers in final response of the API

        :param attr: The dictionary of response
        :type attr: dict
        :return: json object with response headers
        :rtype: dict
        """
        print("add_response_headers has been called: ", type(response))
        try:
            headers = {'headers': {
                        'Cache-Control': 'no-store',
                        'Pragma': 'no-cache',
                        'X-Frame-Options': 'deny',
                        'X-Content-Type-Options': 'nosniff',
                        'Strict-Transport-Security': 'max-age=0',
                        'Content-Security-Policy': 'default-src \"self\"',
                        'X-Permitted-Cross-Domain-Policies': None}}
            
            response.update(headers)
            return response
        except Exception as e:
            print("Exception: ", e)
        
    
    def get_headers_validation_status(self, headers):
        """
        This function checks the headers and validate if exists

        :param attr: The dictionary of headers
        :type attr: dict
        :return: json object with status and body
        :rtype: dict
        """
        print("get_headers_validation_status has been called: ", headers)
        if (headers is not None):
            # convert all keys to lower case
            headers = dict((k.lower(), v) for k,v in headers.items())
            
            if (headers.get("content-type") is not None) and (headers.get("content-type") != "application/json"):
                status_code = 415
                body = "content-type " + headers["content-type"] + " is not supported"
            else:
                status_code = 200
                body = "Success"
        else:
            status_code = 200
            body = "Success"
            
        return {Constants.STATUSCODE: status_code,
                Constants.BODY: body}

    def __getattribute__(self, attr):
        """
        This is overridden implementation of special magic method of Python that is called
        whenever any member variable or method of the class is called using dot notation.
        If the method being called is a decorated method, the call is being sent to 'remote' function as it is
        a Server call initiated from a Client. The functions returns the same object in any case

        :param attr: the name of member variable or method
        :type attr: str
        :return: the object with the name stored in 'attr'
        :rtype: object
        """
        obj = super().__getattribute__(attr)
        if obj is not None:
            try:
                # print("__getattribute__ :: obj.__name__ : ", obj.__name__)
                if obj.__name__.startswith("wrapper"):
                    if (attr, self.__class__.__name__) in self.__class__._function_names:
                        self.current_frame = self.__class__._function_names[(attr, self.__class__.__name__)]
                        try:
                            return self.__getattribute__('remote')
                        except Exception:
                            raise
                    else:
                        raise Exception("Unknown method {}".format(attr))
                else:
                    return obj
            except Exception:
                # we found object, but can't check its name. just return it
                # print(str(ex))
                return obj
        return obj

    def parse_errror_object(self,error):
        """
        :param error: instance of a subclass of BaseError
        :type error: BaseError
        :return: returns reference string of the error passed in the input
        :rtype: str
        """
        try:
            reference = error['Body']['Reference']
            return reference
        except Exception as error:
            return ''

