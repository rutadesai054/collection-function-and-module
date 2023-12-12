from collections import Counter
item_list = [{'item': 'item1', 'amount': 400}, {
    'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

a = Counter()

for i in item_list:
    a[i['item']] = a[i['item']]+i['amount']

print(a)
