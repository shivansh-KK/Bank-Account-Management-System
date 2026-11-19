<div align="center">

# 🏦 Bank Account Management System

### A classroom banking project with account services, MySQL storage, and a desktop loan calculator

[Overview](#-the-project) · [What you can do](#-what-you-can-do) · [Get started](#-get-started) · [Using the programs](#-using-the-programs) · [Project map](#-project-map)

</div>

---

## ✨ The project

This project brings together two Python banking programs and a small graphical loan calculator. The banking menus connect to MySQL and demonstrate a range of everyday account operations, from creating an account to moving money between customers. A collection of original project documents is preserved alongside the source.

It is designed as an educational demonstration. It is a useful way to explore menu-driven Python programs, database tables, simple transaction flows, and a Tkinter interface.

## 💳 What you can do

| Area | Included capabilities |
|:--|:--|
| **Accounts** | Apply for checking or savings accounts, check application progress, view account details, and edit customer information |
| **Transactions** | Deposit funds, withdraw funds, and transfer money between accounts |
| **Administration** | Review account records, create or edit accounts, and run savings interest processing |
| **Loan calculator** | Enter an annual rate, loan amount, and term to estimate monthly and total payments |
| **Local data files** | Supply menu text, emirate names, account ID data, and temporary application codes |

## 🧭 Choose a program

There are two banking scripts because the project contains two different versions of the account model. They are alternatives and should be run separately.

| Program | Choose it for | Database tables |
|:--|:--|:--|
| `src/bank_management.py` | The more complete version, with checking and savings accounts, pending applications, and Emirates ID fields | `checking_acc`, `saving_acc`, `pending` |
| `src/bank_management_basic.py` | A simpler version with a single customer account table | `client_info` |
| `src/loan_calculator.py` | A separate desktop tool for loan payment estimates | None |

Each banking script creates or selects the `bank_management` database and creates its own table or tables when started. Because the versions use different schemas, select one version for a given database setup.

## 🚀 Get started

### 1. Check the requirements

- Python 3
- MySQL Server running on this computer
- The MySQL Connector package
- Tkinter for the desktop calculator (usually included with Python)

Install the connector:

```bash
python -m pip install mysql-connector-python
```

### 2. Set your MySQL connection

Open the banking script you intend to use and update the connection near the top of the file with your MySQL host, username, and password. The project currently contains a sample local connection; replace it with your own details before running.

### 3. Start a program

From the project folder, run one of these commands:

```bash
python src/bank_management.py
```

```bash
python src/bank_management_basic.py
```

Open the loan calculator in its own window with:

```bash
python src/loan_calculator.py
```

The banking programs read their menus and supporting files from `data/`, based on the script location. You can launch them from the project folder without changing directories into `src/`.

## 🪄 A quick tour

### Banking menu

The full banking program starts with a text menu. A customer can apply for an account, check an application, view account details, make a deposit or withdrawal, edit details, or transfer funds. The administrator options are accessed through the admin entry in the menu.

### Account applications

The full version accepts checking or savings applications, validates the emirate against the list in `data/EMIRATES.txt`, and records pending applications in MySQL. Temporary application codes are stored locally in `data/TEMPASS.txt` for the progression flow.

### Loan estimates

The calculator opens a Tkinter window. Enter the annual interest rate, number of years, and loan amount, then select **Compute Payment** to display estimated monthly and total payments.

## 🗂️ Project map

```text
Bank-Account-Management-System/
│
├── README.md
├── .gitignore
│
├── src/
│   ├── bank_management.py
│   ├── bank_management_basic.py
│   ├── loan_calculator.py
│   └── delete.py
│
├── data/
│   ├── ADMIN-OPTIONS.txt
│   ├── EMIRATES.txt
│   ├── START-MENU.txt
│   ├── IDNO.txt                 # Local runtime data; excluded from Git
│   └── TEMPASS.txt              # Local runtime data; excluded from Git
│
└── docs/
    └── project-records/         # Collected Word and PDF project write-ups
```

`IDNO.txt` and `TEMPASS.txt` are intentionally excluded from the repository because they may hold local account identifiers or temporary codes. Create empty files with those names in `data/` before running a banking program if they are missing from your copy. Do not commit real customer information or active codes.

The `delete.py` file is an experimental helper for removing a temporary code. Treat it as a work in progress; the main banking flow does not require it.

## 📚 Project records

The `docs/project-records/` folder keeps the collected Word and PDF write-ups, including alternate copies and versions with different cover-page arrangements. They are supporting references; the Python files are the runnable programs.

## 🔐 A note on safe use

This is a student project and is **not suitable for real banking or customer data**. It uses a basic educational account model and local credentials. Do not deploy it as a financial service or store real passwords, identity numbers, or balances in it.

## 🌱 Made for learning

Explore the code, compare the two banking versions, and follow how menu choices connect to database operations. The project is a starting point for learning; it can be extended with stronger validation, secure password handling, transaction records, and a more modern interface.

<div align="center">

**Python · MySQL · Tkinter**

</div>
