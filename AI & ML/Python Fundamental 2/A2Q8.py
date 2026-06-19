def calc(a,b, operator):
    if operator=="+":
        return a+b

    elif operator=="-":
        return a-b

    elif operator=="*":
        return a*b

    elif operator=="/":
        return a/b

print(calc(5,4,"*"))