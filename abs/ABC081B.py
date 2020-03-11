def is_even(arr):
    for i in arr:
        if i % 2 == 1:
            return False
    return True

n = int(input())
a = [int(i) for i in input().split()]

count = 0
while is_even(a):
    count += 1
    for i in range(len(a)):
        a[i] = a[i] / 2

print(count)
