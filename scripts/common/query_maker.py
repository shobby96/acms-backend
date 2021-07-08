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
    select_statement = "select * from \"{schema}\".{table_name} \n".format(schema=schema, table_name=table_name)
    filter_statement = concat_filter_statements(filter_columns, filter_values, filter_conditions) + \
                       "\n" if filter_columns else ""
    offset_statement = f"offset {offset} \n"
    limit_statement = f"limit {limit}"
    sort_statement = concat_sort_statements(sort_columns, order)
    query = select_statement + filter_statement + sort_statement + offset_statement + limit_statement + ";"
    return query


def insert_query_maker(schema_name="", table_name="", columns=None, values=None):

    if values is None:
        values = []
    if columns is None:
        columns = []
    column_names = ["userID", "invitationTo", "reason", "status", "date"]
    print(concat_headers_or_values(column_names))
    column_string = concat_headers_or_values(columns)
    values = concat_headers_or_values(values, is_header=0)
    insert_query = """INSERT INTO \"{schema_name}\".{table_name}
                        ({column_string})
                        VALUES ({values});
                        """.format(schema_name=schema_name, table_name=table_name, column_string=column_string,
                                   values=values)

    return insert_query


def execute_query(connection, query, limit=10, is_fetch=1):
    cur = connection.cursor()
    cur.execute(query)
    if is_fetch:
        query_results = cur.fetchmany(size=limit)
        print(query_results)
        return query_results
    cur.close()
    connection.commit()
    connection.close()


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
