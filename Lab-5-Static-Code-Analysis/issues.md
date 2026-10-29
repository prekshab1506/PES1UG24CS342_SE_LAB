# Lab 5 — Static Code Analysis

## Issues Identified and Fixes Applied

| Tool | Issue | Description | Fix Applied |
|---|---|---|---|
| Bandit | Shell command execution | `os.system()` executes a constructed shell command. | Removed the unused helper that executed the shell command. |
| Bandit | Hard-coded password | A password was stored directly in the source code. | Removed the unused hard-coded credential. |
| Bandit | MD5 usage | MD5 was used to compare normalized exam answers. | Removed hashing and compared normalized answer strings directly. |
| Bandit | Insecure random selection | `random.choice()` was used to select a bonus question. | Replaced it with `secrets.choice()`. |
| Pylint | Mutable default argument | A default dictionary could retain state across function calls. | Changed the default to `None` and initialized a dictionary inside the function. |
| Pylint | Function naming | Function names did not follow standard Python naming conventions. | Renamed functions using `snake_case`. |
| Pylint | Missing docstrings | Functions and the module lacked documentation. | Added a module docstring and function docstrings. |
| Pylint | Code quality | The code contained avoidable complexity and style issues. | Used clearer variable names, `enumerate()`, and simplified conditional logic. |
| Flake8 | Formatting violations | The original program contained whitespace and formatting violations. | Corrected formatting, spacing, and blank-line issues. |

## Validation Results

- **Pylint:** Final score was 10.00/10.
- **Bandit:** No issues reported in the final scan.
- **Flake8:** The final report was empty, indicating no violations were reported.

