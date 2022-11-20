import boto3
myclient = boto3.client('ec2')
myami = 'ami-07651f0c4c315a529'

myclient.run_instances(
    ImageId=myami,
    InstanceType='t2.micro',
    SubnetId='subnet-070cef202d6518dd3',
    MinCount=1,
    MaxCount=1,
    )
    