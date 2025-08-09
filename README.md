# gender
A simple Python script to demonstrate a robust input validation loop. It repeatedly prompts a user to enter a specific value (M, F, or O) and will not proceed until a valid entry is received.

# User Input Validation Script

This project contains a basic Python script that showcases a common programming pattern: validating user input. The script asks the user to enter their gender ('M', 'F', or 'O') and uses a `while` loop to ensure the program only proceeds after receiving one of the expected inputs. It's a foundational example of how to create robust programs that can handle incorrect user data gracefully.

## Features

-   **Input Validation:** Continuously prompts the user until a valid option is entered.
-   **Robust Handling:** The input is automatically converted to uppercase and stripped of leading/trailing whitespace, making the validation case-insensitive and flexible.
-   **Clear Feedback:** Provides an error message for invalid attempts and a confirmation message for successful input.

## How to Run

1.  Make sure you have [Python 3](https://www.python.org/downloads/) installed on your system.
2.  Save the code as a Python file (e.g., `gender.py`).
3.  Open your terminal or command prompt.
4.  Navigate to the directory where you saved the file.
5.  Run the script using the command:
    ```bash
    python gender.py
    ```

## Usage Example

The program will reject any input that is not 'M', 'F', or 'O' (regardless of case or whitespace) and ask the user to try again.

**Scenario 1: Invalid input followed by a valid one**

```
Enter your gender, M for male, F for female or O for other:
test
Invalid option, try again!
Enter your gender, M for male, F for female or O for other:
 m
Gender: Male registered
```

**Scenario 2: Immediate valid input**

```
Enter your gender, M for male, F for female or O for other:
F
Gender: Female registered
```
