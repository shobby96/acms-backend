# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import json

def lambda_handler(event, context):
    # Parse query string parameters
    sampleParam = event['queryStringParameters']['sampleParam']
    host = event['headers']['Host']
    stage = event['requestContext']['stage']
    path = event['path']
    print(sampleParam, host, stage, path)
    print(f'sampleParam, {sampleParam}')  # Press ⌘F8 to toggle the breakpoint.

    # Create body for response object
    responseObject = {}
    responseObject['sampleParam'] = 1
    responseObject['message'] = 'This is a response from API call'

    # Create Http request
    httpObject = {}
    httpObject['statusCode'] = 200
    httpObject['headers'] = {}
    httpObject['headers']['Content-type'] = 'application/json'
    httpObject['body'] = json.dumps(responseObject)
    return httpObject


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    event = {"queryStringParameters": {"sampleParam": 1, "sampleParam1": 2}}
    lambda_handler(event, None)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
