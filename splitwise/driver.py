from actions import UserManager, ExpenseManager
from entities import User, Expense

if __name__ == "__main__":
    # This portion will be executed only when the current file is excuted directly and not imported as a module

    # creating 2 users and adding friend
    Auro = User("Auroshis", "auroshis@gmail.com", 23)
    Abhi = User("Abhi", "abhi@gmail.com", 23)
    friend_manager = UserManager(user=Auro)
    friend_manager.addFriend(Abhi)

    # Adding expense 1
    new_expense = Expense(Auro, 230, "INR", "Pizza Party", "equal")
    new_expense.setPayments({Auro:100, Abhi:130})
    new_expense.setSplits({Auro:0.5, Abhi:0.5})
    expense_manager = ExpenseManager(expense=new_expense)
    pizza_transactions = expense_manager.simplifyExpenses()
    
    print("PIZZA PARTY SPLIT\n", pizza_transactions)

    # Adding Expense 2
    new_expense = Expense(Auro, 550, "INR", "Biryani Party", "unequal")
    new_expense.setPayments({Auro:500, Abhi:50})
    new_expense.setSplits({Auro:0.6, Abhi:0.4})
    expense_manager = ExpenseManager(expense=new_expense)
    biryani_transactions = expense_manager.simplifyExpenses()

    print("BIRYANI PARTY\n", biryani_transactions)
    