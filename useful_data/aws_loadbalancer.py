import boto3
from aws_profile import key_pair

iam = boto3.client('iam', region_name=key_pair['region'], aws_access_key_id=key_pair['ACCESS_ID'],
         aws_secret_access_key= key_pair['ACCESS_KEY'])

# response1 = iam.get_server_certificate(
#     ServerCertificateName='some_name'
# )

response2 = iam.get_role(
    RoleName='swamy_role'
)
print "&&&"*20
print response2
print "&&&"*20




elb = boto3.client('elb',region_name=key_pair['region'], aws_access_key_id=key_pair['ACCESS_ID'],
         aws_secret_access_key= key_pair['ACCESS_KEY'])

response = elb.describe_load_balancers(
    LoadBalancerNames=[
        'data-loadbalancer',
    ]
    # Marker='',
    # PageSize=123
)


print "$$$"*20
print response
print "$$$"*20