import requests

from src.config import config


def build_email_body(expiring_secrets: list[dict]) -> str:
    lines = [
        "The following app registration secrets are expiring or already expired:",
        "",
    ]

    for item in expiring_secrets:
        lines.extend(
            [
                f"Status: {item['status']}",
                f"App: {item['app_name']}",
                f"App ID: {item['app_id']}",
                f"Secret: {item['secret_name']}",
                f"Secret Key ID: {item['secret_key_id']}",
                f"Expires at: {item['expires_at']}",
                f"Days left: {item['days_left']}",
                "-" * 50,
            ]
        )

    return "\n".join(lines)


def send_expiry_email(
    access_token: str,
    expiring_secrets: list[dict],
    sender: str,
    recipients: list[str],
) -> None:
    if not expiring_secrets:
        print("No expiring secrets found. Email skipped.")
        return

    url = f"{config.graph_base_url}/users/{sender}/sendMail"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    payload = {
        "message": {
            "subject": "[WARNING] App registration secrets expiring soon",
            "body": {
                "contentType": "Text",
                "content": build_email_body(expiring_secrets),
            },
            "toRecipients": [
                {
                    "emailAddress": {
                        "address": recipient.strip()
                    }
                }
                for recipient in recipients
                if recipient.strip()
            ],
        },
        "saveToSentItems": True,
    }

    response = requests.post(url, headers=headers, json=payload, timeout=30)

    if response.status_code != 202:
        raise RuntimeError(
            f"Failed to send email: {response.status_code} - {response.text}"
        )

    print("Email sent successfully.")