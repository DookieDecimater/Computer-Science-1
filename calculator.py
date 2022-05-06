#jackson bauer
#calculator
one = int(input('whats the first number? ')) #assigns 'one' an integer
sign = input('whats the sign? +-*/ ') #assigns 'sign' a string
two = int(input('whats the second number? ')) #assigns 'two' an integer
def calculate(one, two, sign): #function
    if sign == '+':
        print((one)+(two))
    if sign == '-':
        print((one)-(two))
    if sign == '*':
        print((one)*(two))
    if sign == '/':
        print((one)/(two))
calculate(one,two,sign)