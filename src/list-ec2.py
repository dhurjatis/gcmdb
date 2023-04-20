import boto3
import json
from datetime import date, datetime

def json_datetime_serializer(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))



ec2 = boto3.resource('ec2')
instances = ec2.instances.all()
for instance in instances:
    print(f'EC2 instance {instance.id}" information:')
    print(f'Instance state: {instance.state["Name"]}')
    print(f'Instance AMI: {instance.image.id}')
    print(f'Instance platform: {instance.platform}')
    print(f'Instance type: "{instance.instance_type}')
    print(f'Public IPv4 address: {instance.public_ip_address}')
    print('-'*60)
    instance = ec2.Instance(instance.id)
    device_mappings = instance.block_device_mappings
    print(f'Volumes attached to the EC2 instance "{instance.id}":')
    for device in device_mappings:
        print(f"  - Volume {device['Ebs']['VolumeId']} attached as {device['DeviceName']}")
        print('.'*45)
   