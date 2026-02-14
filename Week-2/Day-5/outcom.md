# outcome: Exception Handling
## Try–Except Program

**Expected Outcome:**
The program should handle runtime errors gracefully without crashing and continue execution.

**Actual Outcome:**
When an error occurs inside the try block, the control moves to the except block and displays a friendly error message instead of terminating the program.

## Handling Division by Zero

**Expected Outcome:**
The program should prevent a crash when a number is divided by zero and notify the user about the mistake.

**Actual Outcome:**
When the denominator is zero, a ZeroDivisionError is caught and an appropriate message like “Cannot divide by zero” is displayed.

## Handling File Errors

**Expected Outcome:**
The program should safely handle cases where a file does not exist or cannot be accessed.

**Actual Outcome:**
If the file is missing, FileNotFoundError is caught and the program informs the user instead of stopping unexpectedly. The finally block executes cleanup or confirmation code.

## Custom Exception

**Expected Outcome:**
The program should enforce custom rules (like age validation) using user-defined exceptions.

**Actual Outcome:**
When the custom condition fails, the custom exception is raised and handled properly, making the logic clearer and more meaningful.

