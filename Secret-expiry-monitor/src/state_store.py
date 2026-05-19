import json
from azure.identity import ClientSecretCredential
from azure.storage.blob import BlobServiceClient
from src.config import config


def get_blob_client():
    credential = ClientSecretCredential(
        tenant_id=config.tenant_id,
        client_id=config.client_id,
        client_secret=config.client_secret,
    )

    blob_service_client = BlobServiceClient(
        account_url=config.storage_account_url,
        credential=credential,
    )

    container_client = blob_service_client.get_container_client(
        config.state_container_name
    )

    return container_client.get_blob_client(config.state_blob_name)
    

def load_state() -> dict:
    blob_client = get_blob_client()

    try:
        data = blob_client.download_blob().readall()
        return json.loads(data)
    except Exception:
        # First run → no state yet
        return {}


def save_state(state: dict) -> None:
    blob_client = get_blob_client()

    blob_client.upload_blob(
        json.dumps(state, indent=2),
        overwrite=True,
    )