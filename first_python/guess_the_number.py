import random
from myModule import repeat

def generatRandome():
    rand = int(random.uniform(1,11)) # uniform(num1, num2) give you a random number between num1 and num2 and int() casting     
                                        # so we have to put the range from 1 to 11, where from 1 to 2 (1.1 1.2 .. 1.99) convert to 1
                                        # and from 10 to 11 (10.1 10.2 10.99) convert to 10 
    if int(input("Guess the number from 1 to 10: ")) == rand:
        print("Congratulations you gess")
    else:
        print(f"Unfortunately the true number is {rand}")

repeat(generatRandome)