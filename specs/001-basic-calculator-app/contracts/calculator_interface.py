# Internal API Contract: Calculator Core Logic

This document defines the internal interface for the core calculator logic module. The Graphical User Interface (GUI) will interact with the calculator's business logic through this contract. This is not an external API (e.g., REST/GraphQL) but rather a set of methods exposed by the calculator's logic to the presentation layer.

## `CalculatorLogic` Class Interface

This class will encapsulate the state and operations of the calculator.

```python
class ICalculatorLogic:
    """
    Interface for the calculator's core logic.
    """

    def process_digit(self, digit: str) -> None:
        """
        Processes a digit input (0-9).
        """
        pass

    def process_operator(self, operator: str) -> None:
        """
        Processes an operator input (+, -, *, /).
        """
        pass

    def process_equals(self) -> None:
        """
        Triggers the calculation of the current expression.
        """
        pass

    def process_clear(self) -> None:
        """
        Resets the calculator to its initial state (All Clear).
        """
        pass

    def process_backspace(self) -> None:
        """
        Removes the last digit from the current number.
        """
        pass

    def process_decimal(self) -> None:
        """
        Processes a decimal point input.
        """
        pass

    def get_display_value(self) -> str:
        """
        Returns the current value to be displayed on the calculator screen.
        """
        pass

    def reset_error_state(self) -> None:
        """
        Resets any error state the calculator might be in.
        """
        pass

```

## Functional Details

*   **Input Handling**: All input methods (`process_digit`, `process_operator`, `process_equals`, `process_clear`, `process_backspace`, `process_decimal`) will manage the internal state (`current_number`, `previous_number`, `operator`, `is_new_number`, `has_decimal`, `error_state`) as described in `data-model.md`.
*   **Display Value**: `get_display_value` will return a string representation of the `current_number` or an error message if `error_state` is true.
*   **Error Conditions**: The implementation of this interface must correctly handle error conditions such as "Division by Zero" (`FR-EH-001`) and update the `error_state` accordingly.
*   **Immediate Execution**: The `process_operator` method will implicitly trigger immediate calculations based on the `FR-CL-001` rule.

This contract ensures a clear separation of concerns between the GUI (presentation) and the calculator's core logic (business rules and state management).