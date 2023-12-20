# import necessary packages
import uuid
from datetime import datetime, timezone
 
# Implement Expense class

class Expense:

    def __init__(self, title, amount):
        self.id= str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = self.created_at

    def update(self, title=None,amount=None):
        if title is not None:
            self.title = title 
        if amount is not None:
            self.amount = amount
        self.updated_at = datetime.now(timezone.utc)

    def to_dict(self):
        return {
            "id" : self.id, 
            "title" : self.title,
            "amount" : self.amount,
            "created_at" : self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at" : self.updated_at.strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def __repr__(self) -> str:
        return f"{self.title}_{self.amount}, created_at {self.created_at}"


# Implement ExpenseDB class

class ExpenseDB:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        """
        This function adds an expense to the ExpenseDB class
        """
        if isinstance(expense, Expense):
            self.expenses.append(expense)
            print(f'Expense {expense.title} : {expense.amount} added successfully')
            return expense.id
        else:
            raise ValueError("Invalid expense object!")


    def remove_expense(self, expense_id):
        """
        This function removes an expense from the ExpenseDB class
        """
        for expense in self.expenses:
            if expense.id == expense_id:
                self.expenses.remove(expense)
                print(f'Expense {expense.id} removed successfully')
                return True
        print("Expense not found by ID.")
        return None        


    def get_expense_by_id(self, expense_id):
        for expense in self.expenses:
            if expense.id == expense_id:
                print("Expense found by ID:")
                print(expense.to_dict())
                return expense
        print("Expense not found by ID.")
        return None


    def get_expense_by_title(self, title):
        matching_expenses = [expense for expense in self.expenses if expense.title == title]
        if matching_expenses:
            print(f"Expenses found by title '{title}':")
            for expense in matching_expenses:
                print(expense.to_dict())
        else:
            print(f"No expenses found by title '{title}'.")
        return matching_expenses


    def to_dict(self):
        """
        This function returns a list of dictionaries representing each expense in
        the database. 
        """
        return [expense.to_dict() for expense in self.expenses]
    

# Example 

if __name__ == "__main__":

    # Create an ExpenseDB instance
    expense_db = ExpenseDB()

    # Add expenses to the database
    expense1 = Expense("Data", 500)
    expense2 = Expense("Rent", 10000)

    # Add expenses to the database using add_expense method
    expense_db.add_expense(expense1)
    expense_db.add_expense(expense2)

    # Print the current state of the database
    print("Initial Database:")
    print(expense_db.to_dict())

    # Update an expense
    expense_db.get_expense_by_id(expense_db.expenses[0].id).update(title="Updated Groceries", amount=60.0)

    # Print the updated state of the database
    print("\nUpdated Database:")
    print(expense_db.to_dict())

    # Remove an expense
    expense_db.remove_expense(expense_db.expenses[1].id)

    # Print the final state of the database
    print("\nFinal Database:")
    print(expense_db.to_dict())
