def DoubleIt(number):
    return number * 2

def TimesFour(number):
    return DoubleIt(DoubleIt(number))

print(TimesFour(5))