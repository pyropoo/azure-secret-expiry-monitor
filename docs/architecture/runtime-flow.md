# Runtime Flow

## Execution Flow

1. Application starts from a scheduled trigger.
2. Configuration is loaded from environment variables.
3. The application authenticates against Azure.
4. Microsoft Graph API is called to retrieve App Registrations.
5. Password credentials are checked for expiration dates.
6. Expired and soon-to-expire secrets are identified.
7. A report is generated.
8. Notifications are sent or logged.

## Secret Evaluation Logic

Secrets are grouped into categories:

| Status | Meaning |
|---|---|
| Expired | Secret expiration date is in the past |
| Critical | Secret expires within 7 days |
| Warning | Secret expires within 14 or 30 days |
| Healthy | Secret is outside configured threshold |

## Planned Runtime

The preferred runtime is Azure Functions using a timer trigger.

This allows the monitor to run on a schedule without requiring a dedicated server.
