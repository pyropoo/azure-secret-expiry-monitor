from src.auth import get_access_token
from src.config import config
from src.graph_client import get_applications
from src.expiry_checker import find_expiring_secrets
from src.email_sender import send_expiry_email

from src.state_store import load_state, save_state
from src.state_helpers import (
    build_state,
    find_new_or_updated_secrets,
)


def main() -> None:
    print("Getting Graph token...")
    token = get_access_token()
    print("Token acquired.")

    print("Fetching app registrations...")
    applications = get_applications(token)

    print(f"Found {len(applications)} applications.")

    expiring_secrets = find_expiring_secrets(
        applications=applications,
        warning_days=config.warning_days,
    )

    print(f"Found {len(expiring_secrets)} expiring secrets.")

    if not expiring_secrets:
        print("No expiring secrets found.")
        return

    print("Loading previous state...")
    previous_state = load_state()

    current_state = build_state(expiring_secrets)

    new_or_updated_secrets = find_new_or_updated_secrets(
        current_state=current_state,
        previous_state=previous_state,
        expiring_secrets=expiring_secrets,
    )

    print(f"New or updated secrets: {len(new_or_updated_secrets)}")

    if not new_or_updated_secrets:
        print("No new alerts needed.")
        return

    send_expiry_email(
        access_token=token,
        expiring_secrets=new_or_updated_secrets,
        sender=config.sender_email,
        recipients=config.recipients,
    )

    print("Saving current state...")
    save_state(current_state)

    print("State saved successfully.")


if __name__ == "__main__":
    main()