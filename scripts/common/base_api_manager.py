import inspect

class BaseAPIManager(object):
    _api_url = ""
    _route_table = {}
    _conn = {}

    def __init__(self, conn, api_url="abc"):
        self._api_url = api_url
        self._conn = conn
        print('BASEAPIMANAGER: ')

    @classmethod
    def route(cls, path, method):
        # Add route to route table
        print(f'method: {method}, path: {path}')

        def decorator(func):
            cls._route_table[f'method: {method}, path: {path}'] = func.__name__
            print(f'Route Table: ', cls._route_table)
            print("Function Signature ", inspect.signature(func))
            signature = inspect.signature(func)

            for param in signature.parameters.values():
                print(f'param, {param.name}, {param.default}')

            def wrapper(*args, **kwargs):
                print("start")
                func(*args, **kwargs)
                print("end")
            return wrapper
        return decorator

    @property
    def api_url(self):
        return self._api_url

    @property
    def route_table(self):
        return self._route_table
