from entities import User, Expense
import heapq as hp

#TODO: CHECK FOR ZERO USERS, ZERO EXPENSE VALUE, NEGATIVE EXPENSE VALUE, whether ratio is going less or more than 1
#TODO: ADD unit tests, logging, sending notification of expenses
#TODO: Check a user whether it's a friend or not before adding him/her to an expense
       
class SplitManager:
    """
    Manager class to create splits
    """

    def __createNetSplit(self, split_pays, payments):
        net_split = {}
        for user, share in split_pays.items():
            net_split[user] = payments[user] - share
        return net_split

    def __splitPayment(self, total, ratios):
        __total = total
        __ratios = ratios
        split_amounts = {user: __total*ratio for user, ratio in __ratios.items()}
        return split_amounts
    
    def handleSplitting(self, total, user_payments, splits):
        split_payments = self.__splitPayment(total, splits)
        #getting net split
        net_splits = self.__createNetSplit(split_pays=split_payments, payments=user_payments)
        return net_splits


class UserManager():
    """Manager class for user actions"""  
    def __init__(self, user:User) -> None:
        self.user = user

    def getUser(self):
        return self.user.__name, self.user.__age, self.user.__mail
    
    def getBalanceSheet(self):
        return self.user.__balance_sheet
    
    def getFriends(self):
        return self.user.getFriends()
    
    def addFriend(self, new_friend):
        if new_friend not in self.user.getFriends():
            self.user.setFriend(new_friend)
            return True
        return False
    
    def removeFriend(self, existing_friend):
        if existing_friend in self.user.getFriends():
            self.user.removeFriend(existing_friend)
            return True
        return False

class TransactionUtility:
    """
    Class to handle creation and settling of transactions
    """
    @staticmethod
    def createTransactions(payments):
        """
        Method to create transactions
        NOTE:- It's important to create transactions in a way that you minimise number of transactions
        """
        # declaring 2 max heaps - one for positive transactions and one for negative
        pos_heap, neg_heap = list(), list()
        transactions = list()
        for user, payment in payments.items():
            if payment > 0:
                hp.heappush(pos_heap, [-payment, user])
            else:
                hp.heappush(neg_heap, [payment, user])

        # while either of the heaps is not empty keep popping the highest element and negate before creating a transaction
        while pos_heap:
            pos_high, pos_user = hp.heappop(pos_heap)
            neg_high, neg_user = hp.heappop(neg_heap)
            pos_high = -1*pos_high #adjusting for python heap rules
            neg_high = -1*neg_high
            amount_tranferred = min(pos_high, neg_high)
            # In real world these will be database transactions Hence use locks or isolation or immutability with transaction to ensure data consistency.
            pos_high -= amount_tranferred
            neg_high -= amount_tranferred
            transactions.append([neg_user, pos_user, amount_tranferred])

            if pos_high != 0:
                hp.heappush(pos_heap, [-1*pos_high, pos_user])
            if neg_high != 0:
                hp.heappush(neg_heap, [-1*neg_high, neg_user])
        
        return transactions
    
    @staticmethod
    def formatTransactions(transactions):
        for trxn in transactions:
            trxn[0] = trxn[0].getName()
            trxn[1] = trxn[1].getName()
        return transactions

class ExpenseManager:
    """class to manage an expense related activities. Facade/Wrapper for expense splittling"""
    #TODO use strategy pattern to get user input and split them
    
    def __init__(self, expense: Expense) -> None:
        self.expense = expense
    
    def simplifyExpenses(self):
        # USAGE of FACADE DESIGN PATTERN - STRUCTURAL PATTERN
        # create appropriate net splits
        splitobj = SplitManager()
        total_value = self.expense.getTotal()
        net_splits = splitobj.handleSplitting(total=total_value, user_payments=self.expense.getPayments(), splits=self.expense.getSplits())
        # create transactions - expensive operation cache it once calculated.
        transactions = TransactionUtility.createTransactions(payments=net_splits)
        formatted_op = TransactionUtility.formatTransactions(transactions=transactions)
        return formatted_op

