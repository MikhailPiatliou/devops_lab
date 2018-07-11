num = int(input("Enter num = "))
x = bin(num)[2:]
y = len(x)
if y <= 32:
    res = num ^ (2 ** y - 1)
    print("res = ", res)
