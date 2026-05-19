# Azure Secret Expiry Monitor

Python-based Azure automation platform used to monitor Azure App Registration secrets and generate alerts before expiration.

---

# Overview

Azure environments often contain large numbers of App Registrations and service principals that rely on client secrets for authentication.

Expired secrets can cause:

- Application outages
- Failed CI/CD pipelines
- Authentication failures
- Operational incidents
- Security and compliance risks

This project aims to improve operational visibility by automatically identifying secrets that are approaching expiration or already expired.

The platform is designed around automation, monitoring, and maintainability principles commonly used in modern cloud engineering and DevOps environments.

---

# Core Features

## Secret Expiration Monitoring

The application retrieves Azure App Registrations and checks the expiration dates of associated client secrets.

## Expiration Threshold Detection

Secrets nearing expiration are identified based on configurable thresholds.

Example thresholds:

- Expired
- Expiring within 7 days
- Expiring within 14 days
- Expiring within 30 days

## Reporting and Alerting

The platform is designed to support:

- Console reporting
- Email notifications
- HTML reporting
- Azure Monitor integration
- Ticketing integrations

## Automation Focus

The project is intended to run automatically through scheduled workflows such as:

- Azure Functions
- GitHub Actions
- Scheduled automation jobs

---

# Technologies

| Area | Technology |
|---|---|
| Language | Python |
| Cloud | Azure |
| API | Microsoft Graph API |
| Authentication | Azure Identity |
| CI/CD | GitHub Actions |
| Hosting | Azure Functions |
| Monitoring | Azure Monitor |
| Logging | Application Insights |

---

# Repository Structure

```text
azure-secret-expiry-monitor/
├── src/
│   ├── main.py
│   ├── config.py
│   ├── graph_client.py
│   ├── secret_checker.py
│   ├── notifier.py
│   └── models.py
├── scripts/
├── docs/
│   ├── architecture/
│   └── screenshots/
├── .github/workflows/
├── requirements.txt
├── .gitignore
└── README.md