import numpy as np

def proj1():
   
   x = float(input("Enter a number: "))
   y = float(input("Enter a percentage 0.01-99.99: "))
   z = ((x)/(y/100))
   return x, y, z

def main():
    x, y, z = proj1()
    print(f'{x} is {y}% of {z}')


if __name__ == '__main__':
    main()