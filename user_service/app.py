import json
from faker import Faker

def lambda_handler(event, context):
    fake = Faker()
    user = {
        "name" : fake.name(),
        "address" : fake.address(),
        "mobile" : fake.phone_number()   
    }

    return {
        "statusCode": 200,
        "body": json.dumps(user)
    }