import boto3
import json
# Create IAM client
iam_client = boto3.client('iam')

# Create EMR Role
emr_role_name = 'EMR_DefaultRole'
emr_policy_arn = 'arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceRole'

# Create Role
try:
    iam_client.create_role(
        RoleName=emr_role_name,
        AssumeRolePolicyDocument=json.dumps({
            'Version': '2012-10-17',
            'Statement': [{
                'Effect': 'Allow',
                'Principal': {'Service': 'elasticmapreduce.amazonaws.com'},
                'Action': 'sts:AssumeRole'
            }]
        })
    )
    iam_client.attach_role_policy(RoleName=emr_role_name, PolicyArn=emr_policy_arn)
    print(f"Role {emr_role_name} created and policy attached.")
except iam_client.exceptions.EntityAlreadyExistsException:
    print(f"Role {emr_role_name} already exists.")

# Create EC2 Instance Profile Role
ec2_role_name = 'EMR_EC2_DefaultRole'
ec2_policy_arn = 'arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceforEC2Role'

# Create Role
try:
    iam_client.create_role(
        RoleName=ec2_role_name,
        AssumeRolePolicyDocument=json.dumps({
            'Version': '2012-10-17',
            'Statement': [{
                'Effect': 'Allow',
                'Principal': {'Service': 'ec2.amazonaws.com'},
                'Action': 'sts:AssumeRole'
            }]
        })
    )
    iam_client.attach_role_policy(RoleName=ec2_role_name, PolicyArn=ec2_policy_arn)
    iam_client.create_instance_profile(InstanceProfileName=ec2_role_name)
    iam_client.add_role_to_instance_profile(InstanceProfileName=ec2_role_name, RoleName=ec2_role_name)
    print(f"Role {ec2_role_name} created and policy attached.")
except iam_client.exceptions.EntityAlreadyExistsException:
    print(f"Role {ec2_role_name} already exists.")
