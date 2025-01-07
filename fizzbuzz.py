"""
Um programa que escreve uma função fizzBuzz() com um parâmetro inteiro chamado upTo.
"""
def fizzBuzz(upTo):
    for n in range(1,upTo+1):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz",end =" ")
        elif n % 3 == 0:
            print("Fizz", end = " ")
        elif n % 5 == 0:
            print("Buzz", end = " ")
        else:
            print(n, end = " ")    


fizzBuzz(35)            