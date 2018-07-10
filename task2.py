a = map(int, input("Enter numbers for a list a using spaces: ").split())
b = map(int, input("Enter numbers for a list b using spaces: ").split())
c = list(set(a) & set(b))
print(c)
