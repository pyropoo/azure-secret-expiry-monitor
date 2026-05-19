# Architecture Overview

## Purpose

Azure Secret Expiry Monitor is an automation tool designed to detect expired or soon-to-expire Azure App Registration client secrets.

The goal is to reduce operational risk by identifying expiring credentials before they cause outages in applications, integrations, or CI/CD pipelines.

## High-Level Architecture

```text
Scheduled Trigger
      ↓
Python Application
      ↓
Microsoft Graph API
      ↓
Azure App Registrations
      ↓
Secret Expiry Evaluation
      ↓
Report / Alert / Ticket