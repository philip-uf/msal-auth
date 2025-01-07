from msal_auth.auth import acquire_token
import requests

def call_graph_api():
    token = acquire_token()
    headers = {'Authorization': f'Bearer {token}'}
    graph_endpoint = 'https://graph.microsoft.com/v1.0/users'
    response = requests.get(graph_endpoint, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error calling Graph API: {response.status_code} - {response.text}")

if __name__ == "__main__":
    try:
        user_info = call_graph_api()
        print(user_info)
    except Exception as e:
        print(e)
