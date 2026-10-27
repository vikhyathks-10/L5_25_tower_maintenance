# Lab 5 – Static Code Analysis

## Issue Documentation Table

| Issue | Type | Original Line(s) | Description | Fix Approach |
| --- | --- | ---: | --- | --- |
| Missing module docstring | Code quality | 1 | The program did not have a module-level description. | Added a module docstring. |
| Long lines | Code style | 5, 11, 18 | Several statements exceeded the recommended line length. | Split statements across multiple lines. |
| Incorrect naming conventions | Code quality | 7, 10, 15, 34 | Variable and function names did not follow Python conventions. | Used descriptive names and snake_case. |
| Missing function docstrings | Code quality | 10, 15, 25, 34, 42, 46 | Functions did not explain their purpose. | Added function docstrings. |
| Global statement | Maintainability | 16 | The service counter relied on a global variable. | Used a local counter in the main function. |
| Broad exception handling | Reliability | 20 | Catching every exception could hide unexpected errors. | Caught sqlite3.Error specifically. |
| Hardcoded password | Security | 6 | A password was stored directly in the source code. | Removed the unused password constant. |
| SQL injection risk | Security | 11 | SQL was constructed using string formatting. | Used parameterized SQL queries. |
| Unsafe pickle usage | Security | 1, 43 | Pickle was used unnecessarily to copy database results. | Removed pickle and returned the fetched rows directly. |
| Missing tower validation | Reliability | 35 | A nonexistent tower ID could cause an error. | Checked whether the query returned a row. |
| Unnecessary else | Code quality | 36 | An else block followed a return statement. | Removed the unnecessary else. |
| Formatting violations | Code style | 25, 35, 43, 50 | Extra blank lines, long lines, and missing whitespace were reported. | Corrected formatting and whitespace. |

## Verification Results

- Pylint before fixing: 5.14/10
- Pylint after fixing: 10/10
- Bandit before fixing: 4 findings
- Bandit after fixing: 0 findings
- Flake8 before fixing: 7 reported violations
- Flake8 after fixing: No reported violations

The original reports were saved before making changes, and the updated reports were generated after the corrections.
