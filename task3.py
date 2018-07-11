N = int(input("Enter N = "))
if N == 0 or N == 1 or N >= 10 ** 9:
    print("Q = -1")
    exit(0)
if N < 10:
    print("Q = ", N + 10)
    exit(0)
reslist = []
for i in range(9, 1, -1):
    while N % i == 0:
        N /= i
        reslist.append(i)
if N > 10:
    print("Q = -1")
    exit(0)
n = reslist[len(reslist) - 1]
for i in range(len(reslist) - 2, -1, -1):
    n = 10 * n + reslist[i]
print("Q = ", n)
