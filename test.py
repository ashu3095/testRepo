import boto3

def main():
    client=boto3.client('sts')
    print(client.get_caller_identity().get('Account'))
main()