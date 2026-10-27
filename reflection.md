# Lab 5 – Static Code Analysis Reflection

## 1. What is static code analysis?

Static code analysis is the process of checking source code without executing the program. It helps identify coding mistakes, security vulnerabilities, and formatting problems. In this lab, I used Pylint, Bandit, and Flake8 to improve my Python program.

## 2. What issues did you identify and fix?

I identified several issues, including a hardcoded password, unsafe pickle usage, SQL injection risk, broad exception handling, missing docstrings, inconsistent naming, and formatting errors. I fixed these issues by using parameterized SQL queries, removing unnecessary unsafe code, handling database errors more specifically, and following Python naming and formatting conventions.

## 3. How did Pylint, Bandit, and Flake8 help?

Pylint helped me improve code quality, naming conventions, documentation, and maintainability. Bandit identified potentially unsafe coding practices and security risks. Flake8 helped me identify formatting problems, including long lines, extra blank lines, and missing whitespace. Using all three tools gave me a more complete view of the code.

## 4. What did you learn from this lab?

I learned that code can run successfully and still contain security, quality, and style issues. Static analysis tools help identify these problems early. I also learned the importance of parameterized SQL, specific exception handling, meaningful names, and documenting functions. After making the corrections, my Pylint score increased from 5.14/10 to 10/10, Bandit reported no issues, and Flake8 reported no formatting errors.
