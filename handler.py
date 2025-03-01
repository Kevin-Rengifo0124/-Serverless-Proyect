import json


def hello(event, context):
    body = {
        "message": "Nombre: Kevin Rengifo Ospina/ edad: 21 años / Ciudad: Armenia - Quindio",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

