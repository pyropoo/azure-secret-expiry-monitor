import requests

from src.config import config


def get_applications(access_token: str) -> list[dict]:
    url = f"{config.graph_base_url}/applications"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    params = {
        "$select": "id,appId,displayName,passwordCredentials",
        "$top": 100,
    }

    applications: list[dict] = []

    while url:
        response = requests.get(url, headers=headers, params=params, timeout=30)

        if response.status_code != 200:
            raise RuntimeError(
                f"Graph request failed: {response.status_code} - {response.text}"
            )

        data = response.json()
        applications.extend(data.get("value", []))

        url = data.get("@odata.nextLink")
        params = None

    return applications