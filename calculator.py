import math
def calculator(a,b):
    addition=a+b
    subtraction=a-b
    multiplication=a*b
    division=a/b
    power=a**b
    square_root_1=math.sqrt(a)
    square_root_2 = math.sqrt(a)
    return addition,subtraction,multiplication,division,power,square_root_2, square_root_1
    #result is stored into a tuple

number_1=input("Insert first number \n")
number_1=float(number_1)
number_2=input("Insert second number \n")
number_2=float(number_2)
result=calculator(number_1,number_2)
print("The sum between two numbers is {}".format(result[0]))
print("The subtraction between two numbers is {}".format(result[1]))
print("The multiplication between two numbers is {}".format(result[2]))
print("The division between two numbers is {}".format(result[3]))
print("The power between two numbers is {}".format(result[4]))
print("The square root of number 1 is {} and of number 2 is {}".format(result[5],result[6]))