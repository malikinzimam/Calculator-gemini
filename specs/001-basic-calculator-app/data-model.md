# Data Model: Basic Calculator Application

## Key Entities

### Entity: Calculator State

Represents the current operational state of the calculator.

*   **Attributes**:
    *   `current_number` (Type: `float` or `Decimal`, Default: `0.0`): The numerical value currently displayed or being actively entered by the user. This will be converted to a string for display purposes.
    *   `previous_number` (Type: `float` or `Decimal`, Default: `0.0`): Stores the first operand of a binary operation, waiting for the second operand and an equals operation.
    *   `operator` (Type: `str` or `enum`, Default: `None`): Represents the arithmetic operation selected by the user (e.g., `'+'`, `'-'`, `'*'`, `'/'`). `None` indicates no pending operation.
    *   `is_new_number` (Type: `bool`, Default: `True`): A flag indicating whether the next digit input should start a new number on the display (`True`) or append to the `current_number` (`False`). This becomes `True` after an operator or equals sign is pressed, or when the calculator is cleared.
    *   `has_decimal` (Type: `bool`, Default: `False`): A flag to track if a decimal point has already been entered for the `current_number`, preventing multiple decimal points.
    *   `error_state` (Type: `bool`, Default: `False`): A flag to indicate if the calculator is in an error state (e.g., division by zero). When `True`, most inputs should be ignored until cleared.

*   **Relationships**:
    *   Self-contained; no direct relationships with other entities.

*   **Validation Rules**:
    *   `current_number` should handle both integer and floating-point values.
    *   Only one decimal point is allowed per `current_number`.
    *   `operator` should be one of `'+'`, `'-'`, `'*'`, `'/'`.
    *   `is_new_number` and `has_decimal` states must be managed correctly to ensure proper number input and operation sequencing.

*   **State Transitions (High-level Examples)**:
    *   **Initial State**: `current_number = 0.0`, `previous_number = 0.0`, `operator = None`, `is_new_number = True`, `has_decimal = False`, `error_state = False`.
    *   **Digit Input**: Appends digit to `current_number` string, sets `is_new_number = False`.
    *   **Operator Input**: If `operator` is `None`, moves `current_number` to `previous_number`, sets `operator`, sets `is_new_number = True`, `has_decimal = False`. If `operator` is already set, performs the pending calculation first.
    *   **Equals Input**: Performs calculation using `previous_number`, `operator`, and `current_number`. Updates `current_number` with result, clears `previous_number` and `operator`, sets `is_new_number = True`, `has_decimal = False`.
    *   **Clear (`AC`)**: Resets to initial state.
    *   **Backspace**: Removes last digit from `current_number` string.
    *   **Division by Zero**: Sets `error_state = True`, displays "Error". Requires `AC` to clear.
