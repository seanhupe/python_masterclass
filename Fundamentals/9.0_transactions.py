# Sum of all CC transactions for the month
from idlelib.pyparse import trans

# transaction1 = 10.20
# transaction2 = 31.32
# transaction3 = 5
# print(transaction1 + transaction2 + transaction3)

transactions = [10.2, 31.32, 5]

# transactions.pop()
print(transactions[len(transactions) - 1])
print(transactions[1])
print(len(transactions))

transactions.insert(1, 40.8)
transactions.pop(2)
print(transactions)
print(sum(transactions))
