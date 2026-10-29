\# Lab 5 — Static Code Analysis



| Issue | Type | Line(s) | Description | Fix Approach |

|---|---|---|---|---|

| Shell command execution | Security | Fill from Bandit report | `os.system()` executes a constructed shell command. | Remove the unused helper or replace unsafe command construction with a safer approach. |

| Hard-coded password | Security | Fill from Bandit report | A password is stored directly in the source code. | Remove the unused credential or use an appropriate external configuration mechanism. |

| MD5 usage | Security / design | Fill from Bandit report | MD5 is unnecessary for comparing normalized exam answers. | Compare normalized answer strings directly. |

| Mutable default argument | Bug / quality | Fill from Pylint report | A default dictionary can retain state across calls. | Use `None` as the default and initialize a new dictionary inside the function. |

| Function naming | Style / quality | Fill from Pylint report | Function names do not follow the conventional Python naming style. | Rename functions using `snake\_case`. |

| Formatting violations | Style | Fill from Flake8 report | Whitespace, blank lines, or indentation do not follow the expected style. | Correct the reported formatting issues. |





