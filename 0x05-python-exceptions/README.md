**##Python Exceptions##**
Why Python programming is awesome
What’s the difference between errors and exceptions
What are exceptions and how to use them
When do we need to use exceptions
How to correctly handle an exception
What’s the purpose of catching exceptions
How to raise a builtin exception
When do we need to implement a clean-up action after an exception


1. Why Python programming is awesome:
   - Python has a simple and readable syntax, making it easy to learn and write code.
   - It has a vast ecosystem of libraries and frameworks for various purposes, allowing developers to leverage existing tools and resources.
   - Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming.
   - It has excellent community support and a large user base, making it easier to find help and resources.
   - Python is highly versatile and can be used for web development, data analysis, machine learning, scripting, and more.

2. Difference between errors and exceptions:
   - Errors are issues that occur at runtime and can cause the program to terminate abruptly. They indicate a severe problem that prevents the program from continuing.
   - Exceptions, on the other hand, are events that occur during the execution of a program but can be handled and recovered from. Exceptions allow the program to handle unexpected or exceptional conditions without terminating abruptly.

3. What are exceptions and how to use them:
   - Exceptions are special objects in Python that represent exceptional conditions or errors that occur during program execution.
   - Exceptions can be raised using the `raise` statement, and they propagate up the call stack until they are caught and handled.
   - To handle exceptions, you can use the `try-except` statement. Code that may raise an exception is placed inside the `try` block, and the corresponding exception handling code is placed in the `except` block.

4. When do we need to use exceptions:
   - Exceptions are useful when you anticipate that certain parts of your code may encounter errors or exceptional conditions that need to be handled gracefully.
   - They are particularly useful for error handling, input validation, and recovery from unexpected situations.
   - Exceptions allow you to separate the normal flow of your program from error handling logic, improving the overall robustness and maintainability of your code.

5. How to correctly handle an exception:
   - To handle an exception, you can use the `try-except` statement.
   - Place the code that may raise an exception inside the `try` block.
   - Specify the type(s) of exceptions you want to catch in the `except` block, along with the corresponding exception handling code.
   - You can have multiple `except` blocks to handle different types of exceptions.
   - Optionally, you can include an `else` block that is executed if no exceptions occur in the `try` block.
   - Finally, you can include a `finally` block that is always executed, regardless of whether an exception occurred or not. The `finally` block is typically used for clean-up actions.

6. Purpose of catching exceptions:
   - Catching exceptions allows you to handle exceptional conditions gracefully and provide appropriate responses or error messages to the user.
   - It helps prevent program termination and allows you to take control of the program flow when exceptions occur.
   - Catching exceptions also enables you to log error information, perform recovery actions, or display meaningful error messages to aid in debugging and troubleshooting.

7. How to raise a built-in exception:
   - To raise a built-in exception, you can use the `raise` statement followed by the name of the exception class.
   - For example, to raise a `ValueError` exception, you can use `raise ValueError("Invalid value")`.
   - You can also create custom exceptions by subclassing the built-in `Exception` class.

8. When to implement a clean-up action after an exception:
   - In some cases, you may need to perform certain clean-up actions even if an exception occurs.
   - You can use the `finally` block to ensure that specific code is executed regardless of whether an exception was raised or not.
   - Common use
