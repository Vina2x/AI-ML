def avg(a,b,c):
    result= (a+b+c)/3
    return result

yourAvg= avg(3,3,3)
print(yourAvg)

# default value in a func

def add(a,b=1):
    result2= a+b
    return result2

sum= add(5)
print(sum)