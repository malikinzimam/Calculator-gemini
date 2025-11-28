# Architectural Plan: Basic Calculator Application

## 1. Project Overview

This document outlines the architectural plan for the Basic Calculator Application, a desktop tool designed to provide fundamental arithmetic functions with a user-friendly graphical interface. The application adheres to the functional and non-functional requirements detailed in `spec.md`.

## 2. Architectural Goals

The primary goals for this architecture are:
*   **Reliability:** Ensure consistent and accurate calculation results.
*   **Responsiveness:** Provide immediate feedback to user interactions.
*   **Cross-Platform Compatibility:** Operate seamlessly on Windows, macOS, and Linux.
*   **Maintainability:** Design a modular and understandable codebase.
*   **Simplicity:** Keep the architecture straightforward given the application's basic functionality.

## 3. High-Level Design

The application will follow a Model-View-Controller (MVC) or a similar layered pattern, conceptually divided into three main components:

### 3.1. UI Layer (View)
*   **Responsibility:** Handles presentation to the user and captures raw user input events (button clicks).
*   **Components:** Main application window, display widget, numerical buttons, operator buttons, control buttons (AC, Backspace, =).

### 3.2. Controller/Event Handler
*   **Responsibility:** Acts as the intermediary between the UI and the Calculator Engine. Translates UI events into actions for the engine and updates the UI based on engine responses. Manages the overall application flow.
*   **Components:** Event listeners/handlers for UI buttons, logic to interpret input sequence.

### 3.3. Calculator Engine (Model/Core Logic)
*   **Responsibility:** Encapsulates the core arithmetic logic and manages the calculator's internal state. Performs calculations and handles numerical precision.
*   **Components:** State variables (`current_number`, `previous_number`, `operator`, `is_new_number`), methods for performing arithmetic operations, error detection logic (e.g., division by zero).

### 3.4. Component Interaction Flow

```
+------------+        +-------------------+        +-----------------+
|   UI Layer | <----> | Controller/Events | <----> | Calculator Engine |
+------------+        +-------------------+        +-----------------+
  ^        ^                 |                            |
  |        |                 |                            |
  +--------+ Updates UI      +----------------------------+
             Display                                 Requests calculation
```

## 4. Key Technology Choices

*   **Programming Language:** Python (as per NFR-TS-001).
*   **GUI Framework:** Tkinter.
    *   **Rationale:** Tkinter is chosen for its simplicity, cross-platform compatibility, and inclusion in the Python standard library, which simplifies distribution and avoids external dependencies for basic UI needs. This aligns with the "simplicity" architectural goal.

## 5. Data Model

The core data model revolves around the `Calculator State` as defined in `spec.md`:
*   `current_number`: The value currently displayed or being entered.
*   `previous_number`: The first operand of a binary operation.
*   `operator`: The pending arithmetic operation (`+`, `-`, `*`, `/`).
*   `is_new_number`: A boolean flag indicating if subsequent digit inputs should start a new number or append to the current one.

## 6. Sequence Diagrams (Conceptual Flows)

### 6.1. User Enters a Number
1.  **User:** Clicks a digit button (e.g., `5`).
2.  **UI:** Emits a "digit_clicked" event to Controller.
3.  **Controller:** Receives event, passes digit to Calculator Engine.
4.  **Calculator Engine:** Appends digit to `current_number` (or starts new number if `is_new_number` is true).
5.  **Controller:** Retrieves updated `current_number` from Engine.
6.  **UI:** Updates its display with the new `current_number`.

### 6.2. User Enters an Operator
1.  **User:** Clicks an operator button (e.g., `+`).
2.  **UI:** Emits an "operator_clicked" event to Controller.
3.  **Controller:**
    *   If a `previous_number` and `operator` exist, requests Engine to perform `previous_number` `operator` `current_number`.
    *   Stores `current_number` as `previous_number`, sets the new `operator`.
    *   Sets `is_new_number` to true.
4.  **Calculator Engine:** If calculation requested, performs it and returns result.
5.  **Controller:** Retrieves result (if any), passes to UI to update display (if needed, e.g., after an intermediate calculation).

### 6.3. User Clicks Equals
1.  **User:** Clicks the `=` button.
2.  **UI:** Emits an "equals_clicked" event to Controller.
3.  **Controller:** Requests Engine to perform `previous_number` `operator` `current_number`.
4.  **Calculator Engine:** Performs the final calculation, handles errors (e.g., division by zero).
5.  **Controller:** Retrieves the final result or error state from Engine.
6.  **UI:** Updates its display with the result or "Error" message.

## 7. Error Handling

*   **Division by Zero (FR-EH-001):**
    *   The Calculator Engine will detect division by zero during the calculation process.
    *   The Engine will return an error flag or raise a specific exception to the Controller.
    *   The Controller will catch this, instruct the UI to display "Error", and then disable further calculations until the `AC` button is pressed to reset the state.
*   **Invalid Input (FR-EH-002):**
    *   The Controller will contain logic to filter or ignore redundant operator presses (e.g., `++` becomes `+`).
    *   Clicking `=` without a pending operation will be gracefully handled by the Controller, resulting in no change to the displayed value.

## 8. Non-Functional Considerations

*   **Responsiveness (NFR-UI-003):** The event-driven nature of GUI frameworks (like Tkinter) naturally supports responsive UIs. As all operations are simple and fast, no complex threading or asynchronous processing is anticipated.
*   **Cross-Platform (NFR-PL-001):** Tkinter's inherent cross-platform capabilities ensure the application functions across Windows, macOS, and Linux without platform-specific UI code.

## 9. Deployment Considerations

The application will be packaged as a standalone executable for target platforms. `PyInstaller` is a suitable tool for this purpose, allowing the Python interpreter and Tkinter dependencies to be bundled with the application.

## 10. Open Questions / Architectural Decision Records (ADRs)

*   **ADR: GUI Framework Selection - Tkinter:**
    *   **Decision:** Use Tkinter as the GUI framework for the Basic Calculator Application.
    *   **Context:** The application requires a simple, cross-platform graphical user interface. Python offers several GUI toolkits, including Tkinter, PyQt, Kivy, and WxPython.
    *   **Alternatives Considered:**
        *   **PyQt:** Offers more advanced features and a richer widget set but comes with a steeper learning curve and a more restrictive licensing model for commercial use (though LGPL is fine for open source).
        *   **Kivy:** Good for touch-enabled UIs and mobile, but might be overkill and less "native" for a traditional desktop calculator.
        *   **WxPython:** Mature and native-looking, but often perceived as slightly more complex than Tkinter for basic tasks.
    *   **Decision Drivers:**
        *   **Simplicity and Learning Curve:** Tkinter is generally easier to learn and use for straightforward UIs.
        *   **Included with Python:** No external installation required, simplifying development setup and final distribution.
        *   **Cross-Platform:** Works natively across target operating systems.
        *   **Sufficiency for Requirements:** Tkinter provides all necessary widgets and event handling for a basic calculator.
    *   **Chosen Option:** Tkinter.
*   **Numerical Precision:** The spec implies floating-point numbers. Should Python's native `float` type be used, or should the `decimal` module be employed for exact decimal arithmetic to avoid floating-point inaccuracies?
    *   **Consideration:** For a "basic" calculator, `float` is generally acceptable and simpler, but `decimal` offers higher precision for financial or scientific uses (though out of scope for *this* basic app, it's a good decision point).
    *   **Proposed Default:** Start with native `float` for simplicity, and consider `decimal` if precision issues arise or are explicitly requested.
