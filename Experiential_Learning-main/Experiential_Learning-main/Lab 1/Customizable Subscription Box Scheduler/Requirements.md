# Requirements Table
## Customizable Subscription Box Scheduler

### Problem Context

The Customizable Subscription Box Scheduler is a subscription-box portal that allows subscribers to customize the products included in their upcoming monthly box and pause eligible deliveries. The Fulfillment Lead uses the resulting subscription information to prepare accurate fulfillment manifests.

## Functional Requirements

| ID | Requirement Description | Priority | Acceptance Criteria | Rationale |
|---|---|---|---|---|
| FR-001 | The system shall allow subscribers to add, remove, or replace products in their upcoming subscription box. | High | **Pass:** The subscriber modifies product selections and the updated selections are saved and displayed. **Fail:** The previous selections remain unchanged or the modification is not saved. | Customization is the core functionality of the subscription box service. |
| FR-002 | The system shall allow subscribers to pause an upcoming delivery up to 48 hours before its scheduled fulfillment time. | High | **Pass:** The delivery status changes to Paused and the paused subscription is excluded from the fulfillment manifest. **Fail:** A late pause request is accepted or the paused box remains in the active manifest. | Subscribers need flexibility to skip a delivery when necessary. |
| FR-003 | The system shall allow subscribers to view their current subscription, selected products, delivery schedule, and subscription status. | Medium | **Pass:** Current subscription information and upcoming delivery details are displayed correctly. **Fail:** Information is missing, outdated, or belongs to another subscription. | Subscribers need visibility into their current subscription configuration. |
| FR-004 | The system shall allow the Fulfillment Lead to generate a fulfillment manifest containing active subscriptions and their latest customized product selections. | High | **Pass:** The manifest contains all eligible active subscriptions and their latest valid selections. **Fail:** Paused subscriptions are included or updated selections are missing. | Accurate fulfillment data is required to prepare the correct monthly boxes. |
| FR-005 | The system shall validate subscription changes against product availability and the customization deadline before saving them. | High | **Pass:** Valid changes are accepted and saved. **Fail:** Unavailable products or changes submitted after the deadline are accepted. | Validation prevents fulfillment errors and invalid subscription changes. |

## Non-Functional Requirements

| ID | Type | Requirement Description | Priority | Acceptance Criteria | Rationale |
|---|---|---|---|---|---|
| NFR-001 | Performance | The system shall process a subscriber's box customization request and display the updated result within 2 seconds under a load of up to 1,000 concurrent users. | High | **Pass:** At least 95% of customization requests complete within 2 seconds during load testing. **Fail:** More than 5% of requests exceed the 2-second threshold. | Fast feedback provides a responsive customization experience. |
| NFR-002 | Security | The system shall restrict subscription and fulfillment information to authenticated users according to their assigned role. | High | **Pass:** Subscribers can access only their own subscription data, while Fulfillment Leads can access authorized fulfillment data. **Fail:** Unauthorized subscription or fulfillment information can be accessed. | Subscription and customer-related information must be protected from unauthorized access. |
