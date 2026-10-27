# Lab 5: Static Code Analysis — Telecom Tower Maintenance Tracker

## Overview

This project is part of Lab 5: Static Code Analysis. It focuses on improving Python code quality, security, readability, and maintainability using Pylint, Bandit, and Flake8.

The project contains a Python-based telecom tower maintenance tracker that stores tower details, records servicing, identifies overdue towers, and evaluates tower fault risk.

## Program Features

- Add telecom towers with their site names, last service years, and fault counts.
- Record tower servicing and reset the fault count.
- Identify towers overdue for maintenance by two or more years.
- Determine the risk level of a tower based on its fault count.
- Retrieve a snapshot of the tower records.

The program uses an in-memory SQLite database, so its records are available during the program's execution and are not permanently stored in a database file.

## Technologies Used

- Python 3
- SQLite (`sqlite3`)
- Pylint — code quality analysis
- Bandit — security analysis
- Flake8 — code style and formatting analysis

## Project Structure

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
└── flake8_report_after.txt
```

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/vikhyathks-10/L5_25_tower_maintenance.git
cd L5_25_tower_maintenance
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

On Linux or macOS:

```bash
source venv/bin/activate
```

### 3. Install the static analysis tools

```bash
python -m pip install pylint bandit flake8
```

## Run the Program

Execute the Python script:

```bash
python tower_maintenance.py
```

The program runs a sample maintenance scenario and prints the overdue sites, risk level, total number of towers, and service count.

Expected output:

```text
['Ridge-A'] high 2 1
```

## Static Code Analysis

The program was analyzed using three static analysis tools.

### Pylint

Pylint checks code quality, naming conventions, documentation, and common programming mistakes.

Run the analysis:

```bash
pylint tower_maintenance.py
```

Save the report:

```powershell
pylint tower_maintenance.py > pylint_report.txt 2>&1
```

### Bandit

Bandit identifies potentially unsafe coding patterns and common security vulnerabilities.

Run the analysis:

```bash
bandit -r tower_maintenance.py
```

Save the report:

```powershell
bandit -r tower_maintenance.py -f txt -o bandit_report.txt
```

### Flake8

Flake8 checks Python formatting, whitespace, line length, and PEP 8 style violations.

Run the analysis:

```bash
flake8 tower_maintenance.py
```

Save the report:

```powershell
flake8 tower_maintenance.py > flake8_report.txt 2>&1
```

## Issues Identified and Fixed

The original program contained code quality, security, reliability, and formatting issues. The following improvements were made:

| Issue | Fix Applied |
|---|---|
| SQL injection risk | Replaced SQL string formatting with parameterized queries. |
| Unsafe pickle usage | Removed unnecessary serialization and deserialization. |
| Hardcoded password | Removed the unused password constant. |
| Broad exception handling | Caught the specific `sqlite3.Error` exception. |
| Missing tower validation | Handled nonexistent tower IDs safely in the risk calculation. |
| Naming convention violations | Renamed functions using `snake_case`. |
| Missing docstrings | Added documentation for the module and functions. |
| Global counter | Replaced the global service counter with a local counter in `main()`. |
| Long lines and formatting problems | Improved line wrapping, whitespace, and blank-line usage. |

More detailed findings and their original line numbers are documented in `issues.md`.

## Analysis Results

The reported analysis results after the fixes were:

| Tool | Before Fixes | After Fixes |
|---|---|---|
| Pylint | 5.14/10 | 10/10 |
| Bandit | 4 findings | 0 findings |
| Flake8 | 7 reported violations | No reported violations |

The before-and-after reports are included in the repository for comparison.

## Reflection

The reflection questions and answers are provided in `reflection.md`. They cover the purpose of static code analysis, the issues identified, the roles of the three tools, and the lessons learned from improving the program.

## Git Commits

The work was recorded in three commits:

1. `Fix code quality issues identified by Pylint`
2. `Fix security issues identified by Bandit`
3. `Fix formatting issues identified by Flake8`

These commits document the code quality, security, and formatting stages of the lab work.

## Learning Outcomes

Through this lab, I learned how static analysis tools help identify potential security vulnerabilities, programming mistakes, and style violations without executing the source code. I also learned the importance of parameterized SQL queries, specific exception handling, consistent naming, documentation, and verification after making changes.

## Repository

GitHub: https://github.com/vikhyathks-10/L5_25_tower_maintenance
