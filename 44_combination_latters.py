import itertools

a = {'1': ['a', 'b'], '2': ['c', 'd']}

for combo in itertools.product(*[a[b] for b in sorted(a.keys())]):
    print(''.join(combo))
