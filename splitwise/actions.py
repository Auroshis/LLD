from splitwise.entities import ExpenseSplitter, User, Expense
import heapq as hp


#TODO: CHECK FOR ZERO USERS, ZERO EXPENSE VALUE, NEGATIVE EXPENSE VALUE

class UnequalSplit(ExpenseSplitter):
    """class used for unequal splitting strategy"""
    __ratios = dict()

    @staticmethod
    def splitPayment(total, ratios):
        __total = total
        __ratios = ratios
        split_amounts = {user: __total*ratio for user, ratio in __ratios.items()}
        return split_amounts

class EqualSplit(ExpenseSplitter):
    """class used for equal splitting strategy"""
    __ratios = dict()

    @staticmethod
    def splitPayment(total, users):
        __total = total
        __users = users
        try:
            share = __total/len(__users)
        except ZeroDivisionError as err:
            raise ZeroDivisionError from err
        split_amounts = {user: share for user in __users}
        return split_amounts
       
class SplitManager:
    """
    Manager class to create splits
    """
    __strategies = {"equal": EqualSplit, "unequal": UnequalSplit}

    def __createNetSplit(self, split_pays, payments):
        net_split = {}
        for user, share in split_pays.items():
            net_split[user] = payments[user] - share
        return net_split
    
    def handleSplitting(self, strategy, total, user_payments, splits=None):
        split_payments = dict()
        if strategy == "equal":
            split_payments = self.__strategies[strategy]().splitPayment(total, user_payments)
        elif strategy == "unequal":
            split_payments = self.__strategies[strategy]().splitPayment(total, splits)

        #getting net split
        net_splits = self.__createNetSplit(split_pays=split_payments, payments=user_payments)
        return net_splits


class UserManager(User):
    """Manager class for user actions"""       
    def getUser(self):
        return self.__name, self.__age, self.__mail
    
    def getBalanceSheet(self):
        return self.__balance_sheet
    
    def getFriends(self):
        return self.__friends
    
    def addFriend(self, new_friend):
        if new_friend not in self.__friends:
            self.__friends.add(new_friend)
            return True
        return False
    
    def removeFriend(self, existing_friend):
        if existing_friend in self.__friends:
            self.__friends.remove(existing_friend)
            return True
        return False

class TransactionUtility:
    """
    Class to handle creation and settling of transactions
    """
    @staticmethod
    def createTransactions(payments):
        """
        Method to create settling transaction
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
            print(pos_heap, neg_heap)
            pos_high, pos_user = hp.heappop(pos_heap)
            neg_high, neg_user = hp.heappop(neg_heap)
            pos_high = -1*pos_high #adjusting for python heap rules
            neg_high = -1*neg_high
            amount_tranferred = min(pos_high, neg_high)
            pos_high -= amount_tranferred
            neg_high -= amount_tranferred
            transactions.append([neg_user, pos_user, amount_tranferred])

            if pos_high != 0:
                hp.heappush(pos_heap, [-1*pos_high, pos_user])
            if neg_high != 0:
                hp.heappush(neg_heap, [-1*neg_high, neg_user])
        
        return transactions

class ExpenseManager:
    """class to manage an expense related activities"""
    #TODO use factory pattern to get user input and split them
    pass