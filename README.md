# Bank Account Management System

A command-line banking project built with Python and MySQL, accompanied by a small desktop loan calculator and the original project records.

## At a glance

| Component | What it does |
| --- | --- |
| Full banking program | Checking and savings accounts, applications, account management, transactions, and administrator options |
| Basic banking program | Earlier, simpler account-management version |
| Loan calculator | Tkinter window for estimating monthly and total loan payments |
| Project records | Archived school project documents in PDF and Word formats |

## Project layout

```text
.
├── src/
│   ├── bank_management.py       # Main version with checking and savings accounts
│   ├── bank_management_basic.py # Simpler earlier version
│   ├── loan_calculator.py       # Desktop loan calculator
│   └── delete.py                # Temporary-password helper (experimental)
├── data/
│   ├── START-MENU.txt           # Main menu text
│   ├── ADMIN-OPTIONS.txt        # Administrator menu text
│   ├── EMIRATES.txt             # Accepted emirates
│   ├── IDNO.txt                 # Account ID sequence data
│   └── TEMPASS.txt              # Temporary application passwords
└── docs/
    └── project-records/         # Original project PDFs and Word documents
```

## Banking features

- Apply for a checking or savings account and check application progress
- View account information and edit customer details
- Deposit, withdraw, and transfer funds
- Administrator options for reviewing and editing accounts
- Interest-crediting functionality for savings accounts

The basic version uses a single customer table and offers a smaller set of account operations. The two banking programs are separate alternatives; use one at a time against its matching database structure.

## Requirements

- Python 3
- MySQL Server running locally
- `mysql-connector-python`
- Tkinter, included with many Python installations, for the loan calculator

Install the MySQL connector with:

```bash
python -m pip install mysql-connector-python
```

## Configure MySQL

The banking scripts connect to a local MySQL server and create the `bank_management` database and required tables when they start. Before running, open the selected script and set the connection host, username, and password to match your MySQL installation. The current source contains a sample local password; replace it with your own credentials.

## Run

From the project folder, start either banking version:

```bash
python src/bank_management.py
```

or

```bash
python src/bank_management_basic.py
```

To open the loan calculator:

```bash
python src/loan_calculator.py
```

The banking menus and data files are loaded from `data/`, so run the programs from any working directory after configuring the database connection.

## Data and project records

The files in `data/` support the menu display and the account application flow. `TEMPASS.txt` and `IDNO.txt` may contain active local values; keep them private and do not publish real customer or account information.

`docs/project-records/` contains the collected project write-ups and cover pages. Some documents are alternate or overlapping versions retained for reference.

## Notes

This is an educational project, not a production banking system. It uses simple account handling and should not be used to store real financial or personal data.
