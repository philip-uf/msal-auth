import msal
from .config import client_id, client_secret, authority, scopes

def get_msal_app():
    return msal.ConfidentialClientApplication(
        client_id,
        authority=authority,
        client_credential=client_secret,
    )

def acquire_token():
    app = get_msal_app()
    result = app.acquire_token_silent(scopes, account=None)
    if not result:
        result = app.acquire_token_for_client(scopes=scopes)
    if 'access_token' in result:
        return result['access_token']
    else:
        raise Exception(f"Error acquiring token: {result.get('error')}, {result.get('error_description')}")
