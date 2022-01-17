# low-confidence inferences

import json


THRESHOLD = .94


def lambda_handler(event, context):

    # Get the inferences from the event

    body = json.loads(event['body'])
    inferences = json.loads(body['inferences'])

    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = any(x > THRESHOLD for x in inferences)

    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise ValueError("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
