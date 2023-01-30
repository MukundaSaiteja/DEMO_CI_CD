import json


def handle_request(payload):
    # parse the payload as a JSON object
    data = json.loads(payload)

    # Able to perform any operations on data
    result = sum(data["numbers"])
    result1 = min(data["numbers"])
    result2 = max(data["numbers"])


    # return the result as a JSON response
    response = {
        "result": result,
        "Min": result1,
       "Max": result2
    }
    return json.dumps(response)


payload = '{"numbers": [1, 2, 3,4]}'
print(handle_request(payload))