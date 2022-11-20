import boto3
myclient = boto3.client('ec2')
myami = 'ami-07651f0c4c315a529'

vpc01 = '192.168.10.0/24'
vpc01id = myclient.create_vpc(CidrBlock=vpc01)['Vpc']['VpcId']

myclient.create_subnet(CidrBlock='192.168.10.0/28', VpcId=vpc01id)

mysub = myclient.create_subnet(CidrBlock='192.168.10.16/28', VpcId=vpc01id)['Subnet']['SubnetId']

myclient.run_instances(
    ImageId=myami,
    InstanceType='t2.micro',
    SubnetId=mysub,
    MinCount=1,
    MaxCount=1,
    )
