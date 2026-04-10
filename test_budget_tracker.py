import pytest
from budget_tracker import BudgetTracker

class TestBudgetTracker:

    def setup_method(self):
        self.tracker = BudgetTracker()

    def test_add_income(self):
        self.tracker.add_income(10000)
        assert self.tracker.get_balance() == 10000

    def test_add_expense(self):
        self.tracker.add_income(10000)
        self.tracker.add_expense(3000, "food")
        assert self.tracker.get_balance() == 7000
        
    def test_category_total(self):
        self.tracker.add_income(5000, "salary")
        self.tracker.add_expense(2000, "food")
        self.tracker.add_expense(500, "transport")
        assert self.tracker.get_category_total("food") == 2000
        assert self.tracker.get_category_total("transport") == 500
        assert self.tracker.get_category_total("salary") == 5000

    def test_delete_transaction(self):
        tx = self.tracker.add_expense(2000, "food")
        self.tracker.delete_transaction(tx.id)
        assert self.tracker.get_category_total("food") == 0

    def test_invalid_amount(self):
        with pytest.raises(ValueError):
            self.tracker.add_income(0)
        with pytest.raises(ValueError):
            self.tracker.add_expense(-100, "food")
    
    def test_savings(self):
        self.tracker.add_income(10000)
        self.tracker.savings((0.2 * 10000), "savings")
        assert self.tracker.get_balance() == 8000
    
    def test_budget_limits(self):
        self.tracker.add_expense(3000, "food")
        self.tracker.set_budget_limits(2000, "food")
        assert self.tracker.get_budget_limits("food") == 2000
