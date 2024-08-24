import boto3
import json

def createpolicy():
    iam = boto3.client('iam')

    user_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "*",
                "Resource": "*"
            }
        ]
    }

    response = iam.create_policy(
        PolicyName = 'PythonFullAccessNew',
        PolicyDocument = json.dumps(user_policy)
    )


    print(response)

def get_policy(arn):

    iam = boto3.client('iam')
    response2 = iam.get_policy(
        PolicyArn = arn
    )

    print(response2)

def attach_policy(arn, user):

    iam = boto3.client('iam')
    response3 = iam.attach_user_policy(
        PolicyArn = 'arn:aws:iam::386666042111:policy/PythonFullAccessNew',
        UserName = 'code'
    )

    print(response3)
#createpolicy()

#attach_policy()
get_policy('arn:aws:iam::386666042111:policy/PythonFullAccessNew')



