import boto3
from datetime import datetime

ACCESS_ID = "AKIAIZTHY37D2DUS7D6Q"
ACCESS_KEY = "iRWOziukKeDOWKbNwUTye3UbNGhwhjIkJ1jp/cPM"


# Create CloudWatch client
cloudwatch = boto3.client('cloudwatch', region_name='ap-south-1', aws_access_key_id=ACCESS_ID,
         aws_secret_access_key= ACCESS_KEY)

# List alarms of insufficient data through the pagination interface
paginator = cloudwatch.get_paginator('describe_alarms')
for response in paginator.paginate(StateValue='INSUFFICIENT_DATA'):
    print(response['MetricAlarms'])




# # Create an alarm
# cloudwatch.put_metric_alarm(
#     AlarmName='Web_Server_CPU_Utilization',
#     ComparisonOperator='GreaterThanThreshold',
#     EvaluationPeriods=1,
#     MetricName='CPUUtilization',
#     Namespace='AWS/EC2',
#     Period=60,
#     Statistic='Average',
#     Threshold=70.0,
#     ActionsEnabled=False,
#     AlarmDescription='Alarm when server CPU exceeds 70%',
#     Dimensions=[
#         {
#           'Name': 'InstanceId',
#           'Value': 'INSTANCE_ID'
#         },
#     ],
#     Unit='Seconds'
# )



response = cloudwatch.put_metric_data(
    Namespace='AWS/EC2',
    MetricData=[
        {
            'MetricName': 'CPUUtilization',
            'Dimensions': [
                {
                    'Name': 'InstanceId',
                    'Value': 'INSTANCE_ID'
                },
            ],
            'Timestamp': datetime(2015, 1, 1),
            'Value': 123.0,
            'StatisticValues': {
                'SampleCount': 123.0,
                'Sum': 123.0,
                'Minimum': 123.0,
                'Maximum': 123.0
            },
            'Values': [
                123.0,
            ],
            'Counts': [
                123.0,
            ],
            # 'Unit': 'Seconds'+|+'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
            'Unit' : 'Seconds'+'|'+'Microseconds'+'|'+'Milliseconds',
            'StorageResolution': 123
        },
    ]
)

print response

# For EC2
ec2 = boto3.client('ec2')
data = ec2.describe_instance_status()

# while launching ec2 instance 
1.we have to create IAM role
2.security group


# {
#     'Reservations': [
#         {
#             'Groups': [
#                 {
#                     'GroupName': 'string',
#                     'GroupId': 'string'
#                 },
#             ],
#             'Instances': [
#                 {
#                     'AmiLaunchIndex': 123,
#                     'ImageId': 'string',
#                     'InstanceId': 'string',
#                     'InstanceType': 't1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'t2.xlarge'|'t2.2xlarge'|'t3.nano'|'t3.micro'|'t3.small'|'t3.medium'|'t3.large'|'t3.xlarge'|'t3.2xlarge'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.8xlarge'|'r5.12xlarge'|'r5.16xlarge'|'r5.24xlarge'|'r5.metal'|'r5a.large'|'r5a.xlarge'|'r5a.2xlarge'|'r5a.4xlarge'|'r5a.12xlarge'|'r5a.24xlarge'|'r5d.large'|'r5d.xlarge'|'r5d.2xlarge'|'r5d.4xlarge'|'r5d.8xlarge'|'r5d.12xlarge'|'r5d.16xlarge'|'r5d.24xlarge'|'r5d.metal'|'x1.16xlarge'|'x1.32xlarge'|'x1e.xlarge'|'x1e.2xlarge'|'x1e.4xlarge'|'x1e.8xlarge'|'x1e.16xlarge'|'x1e.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'i3.large'|'i3.xlarge'|'i3.2xlarge'|'i3.4xlarge'|'i3.8xlarge'|'i3.16xlarge'|'i3.metal'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.18xlarge'|'c5d.large'|'c5d.xlarge'|'c5d.2xlarge'|'c5d.4xlarge'|'c5d.9xlarge'|'c5d.18xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'g3.4xlarge'|'g3.8xlarge'|'g3.16xlarge'|'g3s.xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'p3.2xlarge'|'p3.8xlarge'|'p3.16xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.4xlarge'|'f1.16xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.12xlarge'|'m5.24xlarge'|'m5a.large'|'m5a.xlarge'|'m5a.2xlarge'|'m5a.4xlarge'|'m5a.12xlarge'|'m5a.24xlarge'|'m5d.large'|'m5d.xlarge'|'m5d.2xlarge'|'m5d.4xlarge'|'m5d.12xlarge'|'m5d.24xlarge'|'h1.2xlarge'|'h1.4xlarge'|'h1.8xlarge'|'h1.16xlarge'|'z1d.large'|'z1d.xlarge'|'z1d.2xlarge'|'z1d.3xlarge'|'z1d.6xlarge'|'z1d.12xlarge'|'u-6tb1.metal'|'u-9tb1.metal'|'u-12tb1.metal',
#                     'KernelId': 'string',
#                     'KeyName': 'string',
#                     'LaunchTime': datetime(2015, 1, 1),
#                     'Monitoring': {
#                         'State': 'disabled'|'disabling'|'enabled'|'pending'
#                     },
#                     'Placement': {
#                         'AvailabilityZone': 'string',
#                         'Affinity': 'string',
#                         'GroupName': 'string',
#                         'HostId': 'string',
#                         'Tenancy': 'default'|'dedicated'|'host',
#                         'SpreadDomain': 'string'
#                     },
#                     'Platform': 'Windows',
#                     'PrivateDnsName': 'string',
#                     'PrivateIpAddress': 'string',
#                     'ProductCodes': [
#                         {
#                             'ProductCodeId': 'string',
#                             'ProductCodeType': 'devpay'|'marketplace'
#                         },
#                     ],
#                     'PublicDnsName': 'string',
#                     'PublicIpAddress': 'string',
#                     'RamdiskId': 'string',
#                     'State': {
#                         'Code': 123,
#                         'Name': 'pending'|'running'|'shutting-down'|'terminated'|'stopping'|'stopped'
#                     },
#                     'StateTransitionReason': 'string',
#                     'SubnetId': 'string',
#                     'VpcId': 'string',
#                     'Architecture': 'i386'|'x86_64',
#                     'BlockDeviceMappings': [
#                         {
#                             'DeviceName': 'string',
#                             'Ebs': {
#                                 'AttachTime': datetime(2015, 1, 1),
#                                 'DeleteOnTermination': True|False,
#                                 'Status': 'attaching'|'attached'|'detaching'|'detached',
#                                 'VolumeId': 'string'
#                             }
#                         },
#                     ],
#                     'ClientToken': 'string',
#                     'EbsOptimized': True|False,
#                     'EnaSupport': True|False,
#                     'Hypervisor': 'ovm'|'xen',
#                     'IamInstanceProfile': {
#                         'Arn': 'string',
#                         'Id': 'string'
#                     },
#                     'InstanceLifecycle': 'spot'|'scheduled',
#                     'ElasticGpuAssociations': [
#                         {
#                             'ElasticGpuId': 'string',
#                             'ElasticGpuAssociationId': 'string',
#                             'ElasticGpuAssociationState': 'string',
#                             'ElasticGpuAssociationTime': 'string'
#                         },
#                     ],
#                     'NetworkInterfaces': [
#                         {
#                             'Association': {
#                                 'IpOwnerId': 'string',
#                                 'PublicDnsName': 'string',
#                                 'PublicIp': 'string'
#                             },
#                             'Attachment': {
#                                 'AttachTime': datetime(2015, 1, 1),
#                                 'AttachmentId': 'string',
#                                 'DeleteOnTermination': True|False,
#                                 'DeviceIndex': 123,
#                                 'Status': 'attaching'|'attached'|'detaching'|'detached'
#                             },
#                             'Description': 'string',
#                             'Groups': [
#                                 {
#                                     'GroupName': 'string',
#                                     'GroupId': 'string'
#                                 },
#                             ],
#                             'Ipv6Addresses': [
#                                 {
#                                     'Ipv6Address': 'string'
#                                 },
#                             ],
#                             'MacAddress': 'string',
#                             'NetworkInterfaceId': 'string',
#                             'OwnerId': 'string',
#                             'PrivateDnsName': 'string',
#                             'PrivateIpAddress': 'string',
#                             'PrivateIpAddresses': [
#                                 {
#                                     'Association': {
#                                         'IpOwnerId': 'string',
#                                         'PublicDnsName': 'string',
#                                         'PublicIp': 'string'
#                                     },
#                                     'Primary': True|False,
#                                     'PrivateDnsName': 'string',
#                                     'PrivateIpAddress': 'string'
#                                 },
#                             ],
#                             'SourceDestCheck': True|False,
#                             'Status': 'available'|'associated'|'attaching'|'in-use'|'detaching',
#                             'SubnetId': 'string',
#                             'VpcId': 'string'
#                         },
#                     ],
#                     'RootDeviceName': 'string',
#                     'RootDeviceType': 'ebs'|'instance-store',
#                     'SecurityGroups': [
#                         {
#                             'GroupName': 'string',
#                             'GroupId': 'string'
#                         },
#                     ],
#                     'SourceDestCheck': True|False,
#                     'SpotInstanceRequestId': 'string',
#                     'SriovNetSupport': 'string',
#                     'StateReason': {
#                         'Code': 'string',
#                         'Message': 'string'
#                     },
#                     'Tags': [
#                         {
#                             'Key': 'string',
#                             'Value': 'string'
#                         },
#                     ],
#                     'VirtualizationType': 'hvm'|'paravirtual',
#                     'CpuOptions': {
#                         'CoreCount': 123,
#                         'ThreadsPerCore': 123
#                     },
#                     'CapacityReservationId': 'string',
#                     'CapacityReservationSpecification': {
#                         'CapacityReservationPreference': 'open'|'none',
#                         'CapacityReservationTarget': {
#                             'CapacityReservationId': 'string'
#                         }
#                     }
#                 },
#             ],
#             'OwnerId': 'string',
#             'RequesterId': 'string',
#             'ReservationId': 'string'
#         },
#     ],
#     'NextToken': 'string'
# }