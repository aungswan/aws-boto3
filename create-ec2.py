import boto3
myclient = boto3.client('ec2')
myami = 'ami-0d43b5bf95246b21e'

vpc01 = '192.168.10.0/24'
vpc01id = myclient.create_vpc(CidrBlock=vpc01)['Vpc']['VpcID']

myclient.create_subnet(CidrBlock='192.168.10.10/16', VpcID=myvpcid)['Subnet']['SubnetId']

myclient.run_instance(
    ImageId=myami,
    InstanceType='t2.micro',
    SubnetId=mysub,
    MinCount=1
    MaxCount=1
)