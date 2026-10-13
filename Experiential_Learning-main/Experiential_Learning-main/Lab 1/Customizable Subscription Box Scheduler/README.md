# Lab 1 — Requirements Engineering & UML Use-Case Modelling

## Problem Statement

### Customizable Subscription Box Scheduler

A subscription box portal allows subscribers to customize monthly product selections based on their preferences. Subscribers can modify their upcoming box or pause eligible deliveries, while the Fulfillment Lead manages fulfillment information and customized subscription manifests.

## Actors

- **Subscriber** — manages and customizes their subscription.
- **Fulfillment Lead** — manages fulfillment information and generates fulfillment manifests.

## Deliverables

1. Requirements table containing exactly 5 Functional Requirements and 2 Non-Functional Requirements.
2. UML Use-Case Diagram containing the primary actors and use cases, including `<<include>>` and `<<extend>>` relationships.
3. Detailed Use-Case Flow Specification for the core use case, **Customize Monthly Box**.

## Files

- `Requirements.md` — Functional and Non-Functional Requirements.
- `Use-Case-Diagram.png` — UML Use-Case Diagram.
- `Use-Case-Flow.md` — Detailed use-case flow specification.

## UML Relationships Used

- `Customize Monthly Box` `<<include>>` `Validate Subscription Changes`
- `Pause Upcoming Delivery` `<<extend>>` `View Subscription`

## Core Use Case

The selected core use case is **UC-001 — Customize Monthly Box** because customization is the central interaction between the subscriber and the subscription-box system.
