# Lab 5: Static Code Analysis — Telecom Tower Maintenance Tracker

## 1. Project Overview

This project demonstrates the use of static code analysis tools to identify and fix code quality, formatting, and security issues in a Python program for managing telecom tower maintenance.

The original program contained several issues, including unsafe SQL queries, hardcoded credentials, unsafe serialization, naming convention violations, missing documentation, and formatting problems.

The program was improved using **Pylint, Bandit, and Flake8**.

## 2. Project Objectives

- Identify code quality issues using Pylint.
- Detect potential security vulnerabilities using Bandit.
- Identify formatting and style violations using Flake8.
- Fix the issues identified by the analysis tools.
- Compare analysis reports before and after fixing the code.
- Document the issues and reflect on the static code analysis process.

## 3. Technologies Used

- Python
- SQLite
- Pylint
- Bandit
- Flake8
- Git and GitHub

## 4. Project Structure

```text
L5_25_tower_maintenance/
│
├── tower_maintenance.py
├── issues.md
├── reflection.md
├── pylint_report_before.txt
├── pylint_report_after.txt
├── bandit_report_before.txt
├── bandit_report_after.txt
├── flake8_report_before.txt
├── flake8_report_after.txt
└── README.md
```

## 5. Program Features

The `tower_maintenance.py` program provides the following functionality:

- Add tower records to an SQLite database.
- Update tower service information.
- Identify towers that are overdue for maintenance.
- Determine the risk level of a tower based on its fault count.
- Generate a snapshot of tower records.
- Display the results of a sample maintenance scenario.

The program uses an in-memory SQLite database, so the sample records are not permanently stored after the program exits.

## 6. Installation and Setup

Make sure Python is installed on your system.

Install the required static analysis tools using:

```bash
pip install pylint bandit flake8
```

Navigate to the project directory:

```bash
cd L5_25_tower_maintenance
```

Run the Python program:

```bash
python tower_maintenance.py
```

## 7. Static Code Analysis

Three static code analysis tools were used to examine the program.

### 7.1 Pylint

Pylint checks Python code for programming errors, naming conventions, missing documentation, and other code quality problems.

Run:

```bash
pylint tower_maintenance.py
```

### 7.2 Bandit

Bandit examines Python code for common security issues.

Run:

```bash
bandit -r tower_maintenance.py
```

### 7.3 Flake8

Flake8 checks Python code for style violations, whitespace problems, and formatting issues.

Run:

```bash
flake8 tower_maintenance.py
```

## 8. Issues Identified and Fixes Applied

The original program was analyzed using all three tools. The following improvements were made:

- Replaced unsafe SQL string formatting with parameterized SQL queries.
- Removed the hardcoded password because it was not required by the program.
- Removed the use of `pickle` for copying database results.
- Replaced broad exception handling with SQLite-specific error handling.
- Renamed functions to follow Python's snake_case naming convention.
- Added docstrings to explain the purpose of functions and the module.
- Improved variable naming and code readability.
- Corrected line-length, spacing, and blank-line issues.
- Added handling for cases where a requested tower does not exist.
- Added a main guard to prevent the demonstration from running automatically when the module is imported.

More details about the identified issues and their fixes are available in `issues.md`.

## 9. Before and After Analysis Reports

The analysis reports are included in the repository for comparison.

| Tool | Before Report | After Report |
|---|---|---|
| Pylint | `pylint_report_before.txt` | `pylint_report_after.txt` |
| Bandit | `bandit_report_before.txt` | `bandit_report_after.txt` |
| Flake8 | `flake8_report_before.txt` | `flake8_report_after.txt` |

### Results

- **Pylint:** The corrected program achieved a score of 10/10.
- **Bandit:** No issues were identified in the corrected program.
- **Flake8:** No style violations were reported.

These results show that the corrected program satisfies the checks performed by the selected tools. They do not guarantee that a program is entirely free of bugs or security risks.

## 10. Git Commit History

The project changes were organized into three commits:

1. `Fix code quality issues identified by Pylint`
2. `Fix security issues identified by Bandit`
3. `Fix formatting issues identified by Flake8`

Git was used to track the changes, and the commits were pushed to the GitHub repository.

## 11. Reflection

The static code analysis process helped identify issues that were not immediately obvious when reading or running the program. Pylint helped improve code quality and naming conventions, Bandit highlighted security concerns, and Flake8 helped maintain consistent formatting.

Fixing these issues made the program easier to read, maintain, and understand. This exercise also demonstrated the importance of checking code quality and security throughout software development.

The detailed reflection answers are provided in `reflection.md`.

## 12. Conclusion

This lab demonstrated how static code analysis tools can improve Python code quality, security, and consistency. By identifying and fixing the reported issues, the project achieved a Pylint score of 10/10, no reported Bandit issues, and no Flake8 violations.

The exercise reinforced the importance of using automated analysis tools alongside testing and careful code review.

## 13. Repository

GitHub repository: https://github.com/vikhyathks-10/L5_25_tower_maintenance
