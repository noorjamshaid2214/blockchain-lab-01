# Introduction to Blockchain – Lab 01

## Lab Title
SQLite Ledgers and Conflicting Copies

## Objective
To understand how a SQLite database stores records and how two copies can contain different information.

## Tools Used
- Python
- SQLite
- Google Colab

## Records
1. Issue certificate C-001
2. Issue certificate C-002
3. Revoke certificate C-001
4. Issue certificate C-003

## Experiment
Two copies of the ledger were created:
- Registrar Copy
- Employer Copy

The second record in the Employer Copy was changed to C-999 to demonstrate a conflict.

## Conclusion
This lab demonstrates how conflicting records can occur between two copies of a database.
