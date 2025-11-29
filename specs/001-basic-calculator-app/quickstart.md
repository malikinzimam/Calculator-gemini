# Quickstart Guide: Basic Calculator Application

This guide provides instructions on how to set up and run the Basic Calculator Application.

## Prerequisites

*   **Python 3.x**: Ensure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## Installation

1.  **Clone the Repository**:
    First, clone the project repository to your local machine:
    ```bash
    git clone https://github.com/your-username/calculator.git
    cd calculator
    ```
    *(Note: Replace `https://github.com/your-username/calculator.git` with the actual repository URL once available.)*

2.  **Create a Virtual Environment (Recommended)**:
    It's good practice to create a virtual environment to manage project dependencies:
    ```bash
    python -m venv venv
    ```
    *   **On Windows**:
        ```bash
        .\venv\Scripts\activate
        ```
    *   **On macOS/Linux**:
        ```bash
        source venv/bin/activate
        ```

3.  **Install Dependencies**:
    Install the required Python packages. For this project, `pytest` will be used for testing, but Tkinter is built-in.
    ```bash
    pip install -r requirements.txt
    ```
    *(Initially, `requirements.txt` might only contain `pytest`.)*

## Running the Application

After installation, you can run the calculator application:

1.  **Ensure Virtual Environment is Active**:
    (If you followed step 2 in Installation, your virtual environment should still be active.)

2.  **Run the Main Script**:
    ```bash
    python src/calculator.py
    ```
    This will launch the graphical user interface of the calculator.

## Running Tests

To verify the functionality, you can run the unit tests:

1.  **Ensure Virtual Environment is Active**:

2.  **Run Pytest**:
    ```bash
    pytest tests/
    ```
    This will execute all tests located in the `tests/` directory and report the results.

## Troubleshooting

*   **`python` command not found**: Ensure Python is correctly installed and added to your system's PATH.
*   **Virtual environment issues**: Double-check the activation command for your operating system.
*   **GUI not appearing**: If the application runs but no window appears, check your Python installation and Tkinter setup.
