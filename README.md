# Lab 5: Static Code Analysis — Telecom Tower Maintenance Tracker

## 1. Project Overview

This project demonstrates the use of static code analysis tools to identify and fix code quality, coding style, and security issues in a Python program for managing telecom tower maintenance.

The original program contained several issues, including unsafe SQL queries, hardcoded credentials, unnecessary use of pickle, naming convention violations, missing documentation, and formatting problems.

The program was improved using Pylint, Bandit, and Flake8.

## 2. Objectives

- Identify code quality issues using Pylint.
- Detect potential security vulnerabilities using Bandit.
- Identify coding style and formatting violations using Flake8.
- Fix the issues identified by the analysis tools.
- Compare reports generated before and after fixing the code.
- Document the identified issues and reflect on the analysis process.

## 3. Technologies Used

- Python
- SQLite
- Pylint
- Bandit
- Flake8
- Git
- GitHub

## 4. Project Structure

```text
L5_25_tower_maintenance/
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

The `tower_maintenance.py` program provides the following features:

- Add tower records to an SQLite database.
- Update tower maintenance information.
- Identify towers that are overdue for maintenance.
- Determine a tower's risk level based on its fault count.
- Retrieve a snapshot of tower records.
- Display the results of a sample maintenance scenario.

The program uses an in-memory SQLite database. Therefore, the sample records are not permanently stored after the program exits.

## 6. Installation and Setup

Ensure that Python is installed on your system.

Install the static analysis tools using:

```bash
pip install pylint bandit flake8
```

Navigate to the project directory:

```bash
cd L5_25_tower_maintenance
```

Run the program:

```bash
python tower_maintenance.py
```

The sample program displays the overdue towers, risk level, total number of towers, and service count.

Expected output:

```text
['Ridge-A'] high 2 1
```

## 7. Static Code Analysis

Three tools were used to analyze the Python program.

### 7.1 Pylint

Pylint checks Python code for programming errors, naming conventions, missing documentation, and other code quality issues.

Run the following command:

```bash
pylint tower_maintenance.py
```

### 7.2 Bandit

Bandit checks Python code for common security vulnerabilities and potentially unsafe programming practices.

Run the following command:

```bash
bandit -r tower_maintenance.py
```

### 7.3 Flake8

Flake8 checks Python code for style violations, whitespace problems, and formatting inconsistencies.

Run the following command:

```bash
flake8 tower_maintenance.py
```

## 8. Issues Identified and Fixes Applied

The following improvements were made after analyzing the original program:

- Added a module-level docstring and function docstrings.
- Updated function names to follow Python's `snake_case` convention.
- Replaced unsafe SQL string formatting with parameterized SQL queries.
- Removed the unused hardcoded password.
- Removed unnecessary pickle serialization and deserialization.
- Replaced broad exception handling with SQLite-specific error handling.
- Removed the unnecessary global service counter.
- Added handling for nonexistent tower IDs.
- Removed unnecessary `else` blocks following `return` statements.
- Corrected long lines, spacing, and blank-line violations.
- Added a main guard to control program execution when imported.

Detailed issue descriptions and their corresponding fixes are documented in `issues.md`.

## 9. Before and After Analysis Results

The analysis reports are included in the repository.

| Tool | Before Report | After Report |
| --- | --- | --- |
| Pylint | `pylint_report_before.txt` | `pylint_report_after.txt` |
| Bandit | `bandit_report_before.txt` | `bandit_report_after.txt` |
| Flake8 | `flake8_report_before.txt` | `flake8_report_after.txt` |

### 9.1 Pylint Results

- Before fixing: 5.14/10
- After fixing: 10/10

The corrected program achieved a perfect Pylint score, indicating that the issues detected by the tool were addressed.

### 9.2 Bandit Results

- Before fixing: 4 findings
- After fixing: 0 findings

The reported security issues were addressed, and Bandit did not identify any remaining findings in the corrected program.

### 9.3 Flake8 Results

- Before fixing: 7 reported violations
- After fixing: No reported violations

The formatting and coding style violations were corrected.

These results reflect the checks performed by the selected tools and do not guarantee that the program is entirely free of bugs or security vulnerabilities.

## 10. Git Commit History

Git was used to track and manage the project changes.

The original analysis and correction work was organized into the following commits:

1. `Fix code quality issues identified by Pylint`
2. `Fix security issues identified by Bandit`
3. `Fix formatting issues identified by Flake8`

An additional commit was created to update the project README documentation.

The changes were committed locally and prepared for pushing to the GitHub repository.

## 11. Reflection

Static code analysis helped identify issues that were not immediately obvious when reading or running the original program.

Pylint helped improve code quality and naming conventions. Bandit identified security concerns, while Flake8 helped maintain consistent formatting.

Fixing these issues made the program easier to read, maintain, and understand. The exercise also demonstrated the importance of using automated analysis tools as part of the software development process.

The detailed reflection answers are available in `reflection.md`.

## 12. Conclusion

This lab demonstrated how static code analysis tools can improve Python code quality, security, and consistency.

After correcting the identified issues, the program achieved a Pylint score of 10/10, had no reported Bandit findings, and passed Flake8 without reported violations.

The exercise reinforced the importance of writing secure, readable, maintainable code and verifying changes using automated analysis tools.

## 13. Reference Repositories

**Original Reference Repository:**

<https://github.com/SETAPESU26/L5_25_tower_maintenance>

**My Project Repository:**

<https://github.com/vikhyathks-10/L5_25_tower_maintenance>
