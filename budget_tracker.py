from datetime import date

class Transaction:
    def __init__(self, tx_id, tx_type, amount, category, tx_date):
        self.id = tx_id
        self.type = tx_type      
        self.amount = amount
        self.category = category
        self.date = tx_date

class BudgetTracker:
    
    def __init__(self):
        self.transactions = []
        self.next_id = 1
        self.budget_limits = {}

    def add_income(self, amount, category="income", tx_date=None):
        self._validate_amount(amount)

        if tx_date is None:
            tx_date = date.today()

        self._add_transaction("income", amount, category, tx_date)

    def add_expense(self, amount, category, tx_date=None):
        self._validate_amount(amount)

        if tx_date is None:
            tx_date = date.today()

        return self._add_transaction("expense", amount, category, tx_date)
    
    def delete_transaction(self, tx_id):
        for i, tx in enumerate(self.transactions):
            if tx.id == tx_id:
                del self.transactions[i]
                return
        raise KeyError("Transaction not found")

    def get_balance(self):
        balance = 0
        for tx in self.transactions:
            if tx.type == "income":
                balance += tx.amount
            else:
                balance -= tx.amount
        return balance

    def get_category_total(self, category):
        total = 0
        for tx in self.transactions:
            if tx.category == category:
                total += tx.amount
        return total

    def get_transactions(self, month=None, year=None):
        result = self.transactions
        if month is not None:
            result = [t for t in result if t.date.month == month]
        if year is not None:
            result = [t for t in result if t.date.year == year]
        return result

    def _add_transaction(self, tx_type, amount, category, tx_date):
        tx = Transaction(self.next_id, tx_type, amount, category, tx_date)
        self.transactions.append(tx)
        self.next_id += 1
        return tx

    def _validate_amount(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        

    """def savings(self, amount, category, tx_date=None):
        self._validate_amount(amount)

        if tx_date is None:
            tx_date = date.today()

        return self._add_transaction("savings", amount, category, tx_date)"""
    
    #def set_budget_limits(self, amount, category):
        #self._validate_amount(amount)
        #self.budget_limits[category] = amount

    #def get_budget_limits(self, category):
        #return self.budget_limits.get(category)
