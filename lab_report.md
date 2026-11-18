# Introduction to Blockchain – Practical Lab 01

## Lab Title
SQLite Ledgers and Conflicting Copies

## 1. Objective
To understand how SQLite stores records and how two copies of a ledger can contain different information.

## 2. Tools Used
- Python
- SQLite
- Google Colab
- GitHub

## 3. Introduction
SQLite is a database system used to store and manage data. In this lab, we created a ledger containing certificate records. We also created two copies of the ledger to demonstrate how conflicting information can occur.

## 4. Database Structure

The database contains three columns:

| Column | Data Type | Purpose |
|---|---|---|
| seq | INTEGER | Record number |
| event | TEXT | Certificate event |
| approved_by | TEXT | Person approving the event |

## 5. Records Inserted

1. Issue certificate C-001
2. Issue certificate C-002
3. Revoke certificate C-001
4. Issue certificate C-003

All records were approved by the Registrar.

## 6. Shared-Copy Experiment

Two copies were created:
- Registrar Copy
- Employer Copy

The second record in the Employer Copy was changed from C-002 to C-999.

The program compared both copies and detected a conflict.

## 7. CSV Export

The database records were exported into a CSV file named `week01_ledger.csv`.

## 8. Verification

The program used an assertion to check that four records were present.

Expected verification message:

`PASS: All four records are present.`

## 9. Conclusion

This practical demonstrated how SQLite stores ledger records and how two copies can contain conflicting information. It also showed that having multiple copies alone does not make a system a blockchain.
