import boto3
import re
client = boto3.client('ec2')
response = client.describe_instances()

ec2_list = []
for a in response['Reservations']:
    for b in a['Instances']:
        regex = re.compile('(^192.168.10.*)', re.IGNORECASE)
        if regex.match(b['PrivateIpAddresses']):
            ec2_list.append(b['InstanceId'])
        
        print(b['InstanceId'], b['PrivateIpAddress'])

print(client.terminate_instances(InstanceIds=(ec2_list)))