import boto3

# Create EMR client
emr_client = boto3.client('emr', region_name='us-west-2')  # Specify your region

# Define IAM roles
emr_role = 'EMR_DefaultRole'
ec2_role = 'EMR_EC2_DefaultRole'

# Spin up EMR cluster
response = emr_client.run_job_flow(
    Name='MyEMRCluster',
    ReleaseLabel='emr-6.3.0',
    Applications=[{'Name': 'Hadoop'}, {'Name': 'Spark'}],
    Instances={
        'InstanceGroups': [
            {
                'Name': 'Master node',
                'Market': 'ON_DEMAND',
                'InstanceRole': 'MASTER',
                'InstanceType': 'm5.xlarge',
                'InstanceCount': 1,
            },
            {
                'Name': 'Core nodes',
                'Market': 'ON_DEMAND',
                'InstanceRole': 'CORE',
                'InstanceType': 'm5.xlarge',
                'InstanceCount': 2,
            }
        ],
        'Ec2KeyName': 'my-key-pair',  # Replace with your key pair name
        'KeepJobFlowAliveWhenNoSteps': True,
        'TerminationProtected': False,
        'Ec2SubnetId': 'subnet-xxxxxxxx',  # Replace with your subnet ID
    },
    JobFlowRole=ec2_role,
    ServiceRole=emr_role,
    VisibleToAllUsers=True,
    EbsRootVolumeSize=30,
    LogUri='s3://my-emr-logs/',  # Replace with your S3 bucket for logs
)

print(f"Cluster created with the ID: {response['JobFlowId']}")
