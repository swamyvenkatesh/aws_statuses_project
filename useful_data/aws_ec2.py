import boto3
from aws_profile import key_pair

# print key_pair['region']
# print key_pair['ACCESS_ID']
# print  key_pair['ACCESS_KEY']

# AWS EC2 connection
ec2 = boto3.client('ec2', region_name=key_pair['region'], aws_access_key_id=key_pair['ACCESS_ID'],
         aws_secret_access_key= key_pair['ACCESS_KEY'])
response = ec2.describe_instances()

# print "Common Response for describing instances "
# print "$$"*20
# print response
# print "$$"*20


response1 = ec2.describe_instances(
    Filters=[
        {
            'Name': 'instance-id',
            'Values': [
                'i-080e475888791c735',
            ]
        },
    ],
    InstanceIds=[
        'i-080e475888791c735',
    ],
    # DryRun=False,
    # MaxResults=123,
    # NextToken=''
)

print "specific instance output "
print "$$"*20
print response1
print "$$"*20



