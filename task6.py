import re
import operator

line = input("Enter your operation: ")
if len(line) > 100 or len(line) == 0:
    print("Out of range")
    exit(1)
matchObj = re.match(r'(-?)([0-9]{1,5})(\*|\/|\+)?(-)?(?(4)|(-)?)([0-9]{1,5})'
                    r'=(-?)([0-9]{1,5})', line, re.M | re.I)
if matchObj:
    if matchObj.group(1) is not None:
        first = matchObj.group(1) + matchObj.group(2)
    else:
        first = matchObj.group(2)
    if matchObj.group(3) is not None:
        oper = matchObj.group(3)
    else:
        oper = matchObj.group(4)
    if matchObj.group(3) is not None and matchObj.group(4) is not None:
        second = matchObj.group(4) + matchObj.group(6)
    else:
        second = matchObj.group(6)
    if matchObj.group(7) is not None:
        result = matchObj.group(7) + matchObj.group(8)
    else:
        result = matchObj.group(8)
else:
    print("ERROR")
    exit(1)


def get_operator(op):
    return {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }[op]


def operate(first, second, oper):
    first = int(first)
    second = int(second)
    return get_operator(oper)(first, second)


if operate(first, second, oper) == int(result) and int(result) <= 30000:
    print("YES")
elif int(result) > 30000:
    print("Out of range")
    exit(1)
else:
    print("NO")
