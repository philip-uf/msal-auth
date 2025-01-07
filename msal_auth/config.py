import os

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
tenant_id = os.getenv('TENANT_ID')
authority = f'https://login.microsoftonline.com/{tenant_id}'
scopes = ["https://graph.microsoft.com/.default"]
