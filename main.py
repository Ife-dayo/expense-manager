# import necessary packages
import uuid
from datetime import datetime, timezone
 
# Implement Expense class

class Expense:

    def __init__(self, title, amount):
        self.id= str(uuid.uuid4())
        self.title= title
        self.amount =amount
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

        """
        if isinstance(expense, Expense):
            self.expenses.append(expense)
            return expense.id
            print('Expense object added successfully')
        else:
            raise ValueError("Invalid expense object!")


    def remove_expense(self, expense_id):
        pass

    def get_expense_by_id(self, expense_id):
        pass

    def get_expense_by_title(self, expense_title):
        pass

    def to_dict(self):
        pass

expense = Expense(title="Groceries", amount=50.0)
expense1 = Expense(title="Fees", amount=200.0)
expense2 = Expense(title="Gas", amount=300.0)
expense3 = Expense(title="Rent", amount=4000.0)


