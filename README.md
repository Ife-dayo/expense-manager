### README file 
This file does the following
- Explains the project
- Explains how to clone it
- Explains how to run the code

The goal of this project is to exhibit a level of understanding of object oriented programming. It is a coursework that serves as a percentage of my semester grades for my Data Engineering diploma. 

# Expense Manager

Expense Manager is a simple Python project that provides classes for managing financial expenses. It includes an `Expense` class to represent individual expenses and an `ExpenseDB` class to manage a collection of expenses.

## Project Structure

ExpenseManager/
|-- expense_manager.py
|-- readme.md


## Features

- **Expense Class:**
  - Represents an individual financial expense.
  - Attributes:
    - `id`: Unique identifier generated as a UUID string.
    - `title`: String representing the title of the expense.
    - `amount`: Float representing the amount of the expense.
    - `created_at`: Timestamp indicating when the expense was created (UTC).
    - `updated_at`: Timestamp indicating the last time the expense was updated (UTC).
  - Methods:
    - `__init__`: Initializes the attributes.
    - `update`: Allows updating the title and/or amount, updating the `updated_at` timestamp.
    - `to_dict`: Returns a dictionary representation of the expense.

- **ExpenseDB Class:**
  - Manages a collection of `Expense` objects.
  - Attributes:
    - `expenses`: List storing `Expense` instances.
  - Methods:
    - `__init__`: Initializes the list.
    - `add_expense`: Adds an expense.
    - `remove_expense`: Removes an expense.
    - `get_expense_by_id`: Retrieves an expense by ID.
    - `get_expense_by_title`: Retrieves expenses by title.
    - `to_dict`: Returns a list of dictionaries representing expenses.


## How to Clone

To clone this repository, use the following command:

```bash
git clone https://github.com/Ife-dayo/oop-project.git

```
## How to Run

### Prerequisites

Ensure you have Python installed on your machine.

### Running the Code

1. **Navigate to the project directory:**

    ```bash
    cd ExpenseManager
    ```

2. **Run the example script:**

    ```bash
    python expense_manager.py
    ```

    This command will execute the example script and showcase the functionality of the implemented classes.

At the end of the implemetation, I've added an example usage to test the functionalities of the code. You can delete that part if you don't need it. 

Feel free to explore and customize the code to suit your requirements. If you have any questions or encounter any issues, don't hesitate to reach out or open an issue.

Thank you for your time!
