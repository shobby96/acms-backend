import json
import datetime

def concat_filter_statements(filter_columns, filter_values, filter_conditions):
    filter_statement = "where "
    i = 0
    for column, condition, value in zip(filter_columns, filter_conditions, filter_values):
        filter_statement = filter_statement + "{column} {condition} '{value}' "\
            .format(column=column, condition=condition, value=value)
        i = i + 1
        if i < len(filter_columns):
            filter_statement = filter_statement + "and "
    return filter_statement


def concat_sort_statements(sort_columns=[], order=[]):
    if not sort_columns:
        return ""
    order_statement = 'order by '
    i = 0
    for column, order in zip(sort_columns, order):
        order_statement = order_statement + f"\"{column}\" {order}"
        i = i + 1
        if i < len(sort_columns):
            order_statement = order_statement + ','
        else:
            order_statement = order_statement + '\n'
    return order_statement


def concat_headers_or_values(columns=[], is_header=1):
    column_string = ''
    i = 0
    for column in columns:
        column_string = column_string + (f"{column}, " if is_header else f"{column}, ")
        i = i + 1
        if i >= len(columns):
            column_string = column_string[:-2]
    return column_string


def get_query_maker(schema="", table_name="", filter_columns=[], filter_values=[], filter_conditions=[],
                    limit=10, offset=0, sort_columns=[], order=[]):
    print('limit: ', limit, 'offset: ', offset)
    select_statement = "select * from \"{schema}\".{table_name} \n".format(schema=schema, table_name=table_name)
    filter_statement = concat_filter_statements(filter_columns, filter_values, filter_conditions) + \
                       "\n" if filter_columns else ""
    offset_statement = f"offset {offset} \n"
    limit_statement = f"limit {limit}"
    sort_statement = concat_sort_statements(sort_columns, order)
    query = select_statement + filter_statement + sort_statement + offset_statement + limit_statement + ";"
    return query


def insert_query_maker(schema_name="", table_name="", columns=None, values=None, return_column_name=None):

    if values is None:
        values = []
    if columns is None:
        columns = []

    column_names = ["userID", "invitationTo", "reason", "status", "date"]
    print(concat_headers_or_values(column_names))
    column_string = concat_headers_or_values(columns)
    values = concat_headers_or_values(values, is_header=0)
    return_column = f'RETURNING {return_column_name}'
    if not return_column_name:
        return_column = ''
    insert_query = """INSERT INTO \"{schema_name}\".{table_name}
                        ({column_string})
                        VALUES ({values})
                        {return_column};
                        """.format(schema_name=schema_name, table_name=table_name, column_string=column_string,
                                   values=values, return_column=return_column)

    return insert_query




def execute_query(connection, query, limit=10, is_fetch=1, autocommit=1, column_names=[]):
    try:
        cur = connection.cursor()
        cur.execute(query)
        if is_fetch:
            query_results = cur.fetchmany(size=limit)
            print('query_results: ', query_results, 'column_names: ', column_names)
            if column_names:
                query_results = result_list_to_object(column_names=column_names, data_rows=query_results)
            connection.commit()
            connection.close
            return query_results
        cur.close()
        if autocommit:
            connection.commit()
        connection.close()
    except Exception as e:
        print(f'Execute Query Exception: {e}')
        connection.rollback()
        connection.close()
        raise e

def request_type_check(request_body=None, arg_types=None):
    if request_body is None:
        requestBody = {}

    for key in request_body:
        if (key in arg_types) and not(isinstance(request_body[key], arg_types[key])):
            raise Exception(f'Invalid argument type for {key}')


def concat_column_and_values(columns=[], values=[]):
    concat_string = ""
    i = 0
    for (column, value) in zip(columns, values):
        concat_string = concat_string + f'{column} = {value}'
        i = i + 1
        if i < len(columns):
            concat_string = concat_string + ','
        else:
            concat_string = concat_string + '\n'

    return concat_string


def update_query_maker(schema_name='', table_name='', request_body=None, filter={}, filter_conditions=[]):

    filter_columns = filter.keys()
    filter_values = filter.values()

    update_statement = f'UPDATE \"{schema_name}\".{table_name} \n'
    columns = request_body.keys()
    values = request_body.values()
    set_statement = f'SET {concat_column_and_values(columns, values)}'
    filter_statement = concat_filter_statements(filter_columns, filter_values, filter_conditions) + \
                       "\n" if filter_columns else ""
    query = update_statement + set_statement + filter_statement
    return query


def parse_querystring_parameters(querystring_parameters={}):
    for param in querystring_parameters:
        print('qrm: ', querystring_parameters[param], ' param: ', param)
        if querystring_parameters[param] and len(querystring_parameters[param]) == 1:
            querystring_parameters[param] = querystring_parameters[param][0]
    if 'limit' not in querystring_parameters:
        querystring_parameters['limit'] = 10
    if 'offset' not in querystring_parameters:
        querystring_parameters['offset'] = 0
    print('parameters query string: ', querystring_parameters)

    return querystring_parameters


def datetime_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    raise TypeError("Unknown type")

def create_http_response_object(returnDataObject={}, headers={}, status_code=200):
    # Create Http request
    http_object = {}
    http_object['statusCode'] = status_code
    http_object['headers'] = headers
    http_object['headers']['Content-type'] = 'application/json'
    http_object['headers'] = {"Access-Control-Allow-Origin": "*"}
    if returnDataObject:
        http_object['body'] = json.dumps(returnDataObject, default=str)
    return http_object


def result_list_to_object(data_rows=[], column_names=[]):
    try:

        data_rows_with_tags = []
        for row in data_rows:
            print('row: ', row)
            body_object = {}
            if len(row) == len(column_names):
                for column_name, value in zip(column_names, row):
                    body_object[column_name] = value
                data_rows_with_tags.append(body_object)
        print(f'data_row_with_tags: {data_rows_with_tags}')
        return data_rows_with_tags
    except Exception as err:
        print(f'Exception in converting object to list: {err}')
        raise err


def object_contains(required_columns=[], object={}):
    for column in required_columns:
        if column not in object:
            raise Exception(f'{column} value is required')