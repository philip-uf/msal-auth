### Instructions on usage

1. Update .env with credentials from either a sandbox environment or production in Azure AD

2. Open shell

3. Install Docker Desktop, e.g. `winget install Docker.DockerDesktop` or `brew install --cask docker`

4. Go to [Docker personal access tokens](https://app.docker.com/settings/personal-access-tokens) and create your token

5. Back to shell and run `docker login -u <username>` and enter your personal access token as password

6. Go to directory, e.g. `cd $HOME/msgraph-auth`

7. Run docker-compose, e.g. `docker-compose up`

[MSAL doc](https://learn.microsoft.com/en-us/python/api/msal/msal.application.clientapplication?view=msal-py-latest)