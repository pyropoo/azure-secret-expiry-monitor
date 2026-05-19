from datetime import datetime, timezone


def find_expiring_secrets(applications: list[dict], warning_days: int) -> list[dict]:
    expiring_secrets = []
    now = datetime.now(timezone.utc)

    for app in applications:
        app_name = app.get("displayName") or "Unknown app"
        app_id = app.get("appId") or "Unknown appId"
        password_credentials = app.get("passwordCredentials") or []

        for secret in password_credentials:
            end_date_raw = secret.get("endDateTime")

            if not end_date_raw:
                continue

            end_date = parse_graph_datetime(end_date_raw)
            days_left = (end_date - now).days

            if days_left <= warning_days:
                expiring_secrets.append(
                    {
                        "app_name": app_name,
                        "app_id": app_id,
                        "secret_name": secret.get("displayName") or "Unnamed secret",
                        "secret_key_id": secret.get("keyId") or "Unknown keyId",
                        "expires_at": end_date_raw,
                        "days_left": days_left,
                        "status": get_status(days_left),
                    }
                )

    return sorted(expiring_secrets, key=lambda item: item["days_left"])


def parse_graph_datetime(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def get_status(days_left: int) -> str:
    if days_left < 0:
        return "EXPIRED"

    if days_left <= 7:
        return "CRITICAL"

    return "WARNING"