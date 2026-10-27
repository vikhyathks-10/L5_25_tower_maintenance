# Lab 5: Static Code Analysis — Telecom Tower Maintenance Tracker

## Overview

This project was completed as part of Lab 5: Static Code Analysis. The objective is to improve Python code quality, security, readability, and maintainability using Pylint, Bandit, and Flake8.

The project contains a Python program that manages basic telecom tower maintenance information, records servicing, identifies overdue towers, and determines tower risk based on reported faults.

## Features

- Add towers with site names, service years, and fault counts.
- Record tower servicing and reset faults after servicing.
- Identify sites overdue for maintenance by two or more years.
- Determine the risk level of a tower.
- Retrieve a snapshot of tower records.

The program uses an in-memory SQLite database. Data is available while the program runs and is not retained after the database connection closes.

## Technologies Used

- Python 3
- SQLite (`sqlite3`)
- Pylint
- Bandit
- Flake8

## Project Structure

```text
L5_25_tower_maintenance/
├── tower_maintenance.py
├── README.md
├── issues.md
├── reflection.md
├── pylint_report_before.txt
├── pylint_report_after.txt
├── bandit_report_before.txt
├── bandit_report_after.txt
├── flake8_report_before.txt
└── flake8_report_after.txt
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/vikhyathks-10/L5_25_tower_maintenance.git
cd L5_25_tower_maintenance
```

### 2. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

On Linux or macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the analysis tools

```bash
python -m pip install pylint bandit flake8
```

## Run the Program

```bash
python tower_maintenance.py
```

The program executes a sample maintenance scenario and prints the overdue sites, risk level, tower count, and service count.

Expected output:

```text
['Ridge-A'] high 2 1
```

## Static Analysis

### Pylint

Pylint identifies code quality issues, naming violations, missing documentation, and potential programming problems.

```powershell
pylint tower_maintenance.py > pylint_report_after.txt 2>&1
```

### Bandit

Bandit checks Python code for common security issues.

```powershell
bandit -r tower_maintenance.py -f txt -o bandit_report_after.txt
```

### Flake8

Flake8 checks Python style, formatting, whitespace, and line-length violations.

```powershell
flake8 tower_maintenance.py > flake8_report_after.txt 2>&1
```

The original reports use the `_before.txt` suffix, and the reports generated after corrections use `_after.txt`.

## Issues Addressed

The original code contained several issues identified during static analysis:

| Issue | Fix |
|---|---|
| Potential SQL injection | Replaced string-formatted SQL with parameterized queries. |
| Unsafe pickle usage | Removed unnecessary serialization and deserialization. |
| Hardcoded password | Removed the unused password constant. |
| Broad exception handling | Used the specific `sqlite3.Error` exception. |
| Missing tower validation | Handled queries that return no tower record. |
| Naming violations | Used Python's `snake_case` naming convention. |
| Missing docstrings | Added module and function documentation. |
| Formatting violations | Corrected line length, blank lines, and whitespace. |
| Global counter | Replaced the global service counter with a local counter. |

The file `issues.md` contains the detailed issue documentation table, including descriptions and fix approaches.

## Analysis Results

The results observed during the lab were:

| Tool | Before | After |
|---|---|---|
| Pylint | 5.14/10 | 10/10 |
| Bandit | 4 findings | 0 findings |
| Flake8 | 7 reported violations | No reported violations |

The six report files provide the before-and-after results for comparison.

## Reflection

The file `reflection.md` contains the answers to the lab's reflection questions. It discusses static code analysis, the issues found, the purposes of the three tools, and the lessons learned.

## Repository

GitHub: https://github.com/vikhyathks-10/L5_25_tower_maintenance
