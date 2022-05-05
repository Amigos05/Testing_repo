# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from fractions import Fraction
import cmath

def print_hi(a, b, c):
    d = (b ** 2) - (4 * a * c)
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)
    print('The solution are {0} and {1}'.format(Fraction(sol1), Fraction(sol2)))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(1,-2,-195)



