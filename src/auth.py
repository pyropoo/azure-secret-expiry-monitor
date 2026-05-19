from azure.identity import ClientSecretCredential
from src.config import config


def get_access_token():
    credential = ClientSecretCredential(
        tenant_id=config.tenant_id,
        client_id=config.client_id,
        client_secret=config.client_secret,
    )

    token = credential.get_token("https://graph.microsoft.com/.default")

    return token.token