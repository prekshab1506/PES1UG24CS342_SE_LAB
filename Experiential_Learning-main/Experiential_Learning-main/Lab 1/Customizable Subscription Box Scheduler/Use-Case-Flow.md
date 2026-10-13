# Use-Case Flow Specification

## UC-001 — Customize Monthly Box

**Primary Actor:** Subscriber

**Goal:** Allow a subscriber to modify the products in their upcoming subscription box.

### Preconditions

1. The subscriber has an active account.
2. The subscriber is authenticated.
3. The subscriber has an active subscription.
4. The upcoming box is still within the permitted customization window.
5. The upcoming box has not already entered final fulfillment processing.

### Postconditions

1. The valid product selections are saved.
2. The updated selections are associated with the subscriber's upcoming box.
3. The updated selections are available to the fulfillment process.
4. The subscriber receives confirmation that the customization was successful.

### Main Success Scenario

1. The subscriber logs into the subscription portal.
2. The system authenticates the subscriber.
3. The subscriber opens their active subscription.
4. The system displays the upcoming subscription box and its current product selections.
5. The subscriber chooses to customize the upcoming box.
6. The subscriber adds, removes, or replaces one or more products.
7. The system validates the requested changes.
8. The system checks product availability and the customization deadline.
9. The system accepts the valid changes.
10. The system saves the updated product selections.
11. The system updates the upcoming box information.
12. The system displays a confirmation message to the subscriber.

### Alternative Flows

#### A1 — Selected Product Is Unavailable

1. During validation, the system detects that one or more selected products are unavailable.
2. The system identifies the unavailable product(s) to the subscriber.
3. The system does not save the invalid selection.
4. The subscriber chooses an alternative available product.
5. The system validates the new selection.
6. If valid, the system saves the updated box.

#### A2 — Customization Deadline Has Passed

1. The system detects that the customization deadline has passed.
2. The system rejects the requested modification.
3. The system informs the subscriber that the upcoming box can no longer be customized.
4. The existing box configuration remains unchanged.

#### A3 — Subscriber Cancels the Change

1. The subscriber selects Cancel before confirming the changes.
2. The system discards the unsaved changes.
3. The original product selections remain unchanged.

### Exception Flow

#### E1 — System Error While Saving

1. The system encounters an error while saving the customization.
2. The system does not confirm the change as successful.
3. The system informs the subscriber that the update could not be completed.
4. The subscriber may retry the operation.
