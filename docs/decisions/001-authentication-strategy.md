# 001 - Authentication Strategy

## Status

Accepted

## Context

The application requires access to Microsoft Graph in order to read Azure App Registration credential metadata.

Authentication must be secure, automation-friendly, and suitable for both local development and cloud execution.

## Decision

The project is designed to support Azure Identity authentication patterns.

Local development may use Azure CLI authentication or service principal credentials.

Cloud execution should prefer Managed Identity where possible.

## Reasoning

Managed Identity avoids storing long-lived credentials in application configuration.

Azure CLI authentication makes local development easier without hardcoding secrets.

## Consequences

### Positive

- Reduced secret handling
- Better security posture
- Works well with Azure Functions
- Supports local and cloud execution

### Negative

- Requires correct Azure permissions
- Microsoft Graph permissions must be configured carefully
