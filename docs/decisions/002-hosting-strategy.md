# 002 - Hosting Strategy

## Status

Proposed

## Context

The application should run automatically on a schedule and should not require a dedicated server.

## Decision

Azure Functions is the preferred hosting option.

## Reasoning

Azure Functions provides a serverless execution model suitable for scheduled automation tasks.

A timer-triggered function can run the monitor at regular intervals, such as daily or weekly.

## Consequences

### Positive

- No dedicated server required
- Cost-efficient
- Simple scheduled execution
- Good Azure integration
- Application Insights support

### Negative

- Requires deployment pipeline
- Function runtime configuration must be managed
