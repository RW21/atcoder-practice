a, b = [int(i) for i in input().split()]

if a * b % 2 == 1:
    print('Odd')
else:
    print('Even')