import  datetime
from dateutil.tz import tzutc
data = {u'Reservations': 
    			[{u'Instances': 
    				[{
    					u'Monitoring': {u'State': 'enabled'}, 
    					u'PublicDnsName': 'ec2-13-127-122-128.ap-south-1.compute.amazonaws.com', 
    					u'State': {u'Code': 16, u'Name': 'running'}, u'EbsOptimized': False, u'LaunchTime': datetime.datetime(2018, 11, 21, 10, 56, 9, tzinfo=tzutc()), 
    					u'PublicIpAddress': '13.127.122.128', u'PrivateIpAddress': '172.31.24.72', u'ProductCodes': [], u'VpcId': 'vpc-9a5c7df2', 
    					u'CpuOptions': {u'CoreCount': 1, u'ThreadsPerCore': 1}, 
    					u'StateTransitionReason': '', 
    					u'InstanceId': 'i-080e475888791c735', u'EnaSupport': True, u'ImageId': 'ami-0d773a3b7bb2bb1c1', u'PrivateDnsName': 'ip-172-31-24-72.ap-south-1.compute.internal', u'KeyName': 'swamy_testing_ec2', 
    					u'SecurityGroups': [{u'GroupName': 'default', u'GroupId': 'sg-9305f6fe'}], 
    					u'ClientToken': '', u'SubnetId': 'subnet-74004e1c', u'InstanceType': 't2.micro', 
    					u'CapacityReservationSpecification': {u'CapacityReservationPreference': 'open'}, 
    					u'NetworkInterfaces': [{u'Status': 'in-use', u'MacAddress': '02:1e:70:28:be:18', u'SourceDestCheck': True, u'VpcId': 'vpc-9a5c7df2', u'Description': 'Primary network interface', u'NetworkInterfaceId': 'eni-049859dbfa7479530', 
    					u'PrivateIpAddresses': [{u'PrivateDnsName': 'ip-172-31-24-72.ap-south-1.compute.internal', u'PrivateIpAddress': '172.31.24.72', u'Primary': True, 
    					u'Association': {u'PublicIp': '13.127.122.128', u'PublicDnsName': 'ec2-13-127-122-128.ap-south-1.compute.amazonaws.com', u'IpOwnerId': 'amazon'}}],
    					u'PrivateDnsName': 'ip-172-31-24-72.ap-south-1.compute.internal', u'Attachment': {u'Status': 'attached', u'DeviceIndex': 0, u'DeleteOnTermination': True, u'AttachmentId': 'eni-attach-04246f0fd2e1ce6d3', u'AttachTime': datetime.datetime(2018, 11, 21, 10, 56, 9, tzinfo=tzutc())}, 
    					u'Groups': [{u'GroupName': 'default', u'GroupId': 'sg-9305f6fe'}], 
    					u'Ipv6Addresses': [], u'OwnerId': '326718784130', u'PrivateIpAddress': '172.31.24.72', u'SubnetId': 'subnet-74004e1c', 
    					u'Association': {u'PublicIp': '13.127.122.128', u'PubllicDnsName': 'ec2-13-127-122-128.ap-south-1.compute.amazonaws.com', u'IpOwnerId': 'amazon'}}], 
    					u'SourceDestCheck': True, u'Placement': {u'Tenancy': 'default', u'GroupName': '', u'AvailabilityZone': 'ap-south-1a'}, 
    					u'Hypervisor': 'xen', u'BlockDeviceMappings': [{u'DeviceName': '/dev/sda1', 
    					u'Ebs': {u'Status': 'attached', u'DeleteOnTermination': True, u'VolumeId': 'vol-0fbb591f98ff74330', u'AttachTime': datetime.datetime(2018, 11, 21, 10, 56, 10, tzinfo=tzutc())}}], 
    					u'Architecture': 'x86_64', u'RootDeviceType': 'ebs', 
    					u'IamInstanceProfile': {u'Id': 'AIPAJJ5SQTJWKKBS6KYDM', u'Arn': 'arn:aws:iam::326718784130:instance-profile/swamy_role'}, 
    					u'RootDeviceName': '/dev/sda1', u'VirtualizationType': 'hvm', u'AmiLaunchIndex': 0}], 

                        u'ReservationId': 'r-03f595bed7541d7e4', u'Groups': [], u'OwnerId': '326718784130'

    			}],

    					'ResponseMetadata': {'RetryAttempts': 0, 'HTTPStatusCode': 200, 'RequestId': '246fa648-c65e-4335-be51-39d96bbe9a84', 
    					'HTTPHeaders': {'transfer-encoding': 'chunked', 'content-type': 'text/xml;charset=UTF-8', 'vary': 'Accept-Encoding', 'date': 'Wed, 21 Nov 2018 11:03:39 GMT', 'server': 'AmazonEC2'}}

			}


# print data['Reservations']
# print data['ResponseMetadata']



for i in data['Reservations']:
    # print i
    print type(i)
    
    # print i['Instances']
    for jj in i['Instances']:
        if jj['SubnetId']:
            # print jj['SubnetId']
            print "subnet is available"
        else:
            print "errorrrs f"

    # print i['Groups']
    # print i['ReservationId']
    # print i['OwnerId']
    break

        


    # print j
    # break