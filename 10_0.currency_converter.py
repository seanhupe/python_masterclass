transactions_aed = [23.45, 67.89, 12.34, 78.90, 54.21, 11.22, 33.44, 55.66, 77.88, 99.00]

us_dollar = round(transactions_aed[0] * .27, 2)
print(us_dollar)

transactions_usd = []
for item in transactions_aed:
    item_usd = round(item * .27, 2)
    transactions_usd.append(item_usd)
print(transactions_usd)
