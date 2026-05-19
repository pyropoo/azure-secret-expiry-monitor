def build_state(expiring_secrets: list[dict]) -> dict:
    return {
        "secrets": [
            {
                "app_id": item["app_id"],
                "secret_key_id": item["secret_key_id"],
                "expires_at": item["expires_at"],
            }
            for item in expiring_secrets
        ]
    }


def find_new_or_updated_secrets(
    current_state: dict,
    previous_state: dict,
    expiring_secrets: list[dict],
) -> list[dict]:

    previous_secrets = previous_state.get("secrets", [])

    previous_lookup = {
        (
            item["app_id"],
            item["secret_key_id"],
            item["expires_at"],
        )
        for item in previous_secrets
    }

    changed = []

    for item in expiring_secrets:
        key = (
            item["app_id"],
            item["secret_key_id"],
            item["expires_at"],
        )

        if key not in previous_lookup:
            changed.append(item)

    return changed