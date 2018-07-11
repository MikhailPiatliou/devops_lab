from collections import defaultdict
d = defaultdict(list)
n, m = list(map(int, input("Enter n and m separated by space: ").split()))
if n < 1 or n > 10000 or m < 1 or m > 100:
    print("Out of range. Try again.")
    exit(1)

for i in range(n):
    aword = str(input("Enter words for the group A: "))
    if len(aword) < 1 or len(aword) > 100:
        print("Out of range. Try again.")
        exit(1)
    d[aword].append(i + 1)

for i in range(m):
    bword = str(input("Enter words for the group B: "))
    if len(bword) < 1 or len(bword) > 100:
        print("Out of range. Try again.")
        exit(1)
    print(' '.join(map(str, d[bword])) or -1)
