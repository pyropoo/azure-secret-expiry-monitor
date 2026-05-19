import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    def __init__(self):
        # ===== Azure / Graph =====
        self.tenant_id = self._get_env("AZURE_TENANT_ID")
        self.client_id = self._get_env("AZURE_CLIENT_ID")
        self.client_secret = self._get_env("AZURE_CLIENT_SECRET")

        # ===== Graph =====
        self.graph_base_url = "https://graph.microsoft.com/v1.0"

        # ===== Email =====
        self.sender_email = self._get_env("SENDER_EMAIL")
        self.recipients = self._get_env("RECIPIENTS").split(",")

        # ===== Logic =====
        self.warning_days = int(os.getenv("WARNING_DAYS", "30"))
        # ===== Storage =====
        self.storage_account_url = self._get_env("STORAGE_ACCOUNT_URL")
        self.state_container_name = self._get_env("STATE_CONTAINER_NAME")
        self.state_blob_name = os.getenv("STATE_BLOB_NAME", "secret-expiry-state.json")

    def _get_env(self, key: str) -> str:
        value = os.getenv(key)
        if not value:
            raise ValueError(f"Missing required environment variable: {key}")
        return value


# Create a single config instance
config = Config()