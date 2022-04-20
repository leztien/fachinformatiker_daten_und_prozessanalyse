"""
Seite 181, Aufgabe 3.2
"""


from functools import reduce
from operator import mul
from math import pow


def get_input():
    print("Geben Sie Zahlen mit der Eingabe-Taset ein. "
          "Dann geben Sie 'q' ein.")
    
    seq = []
    while True:
        v = input(">> ")
        if 'q' in v.lower():
            break
        try:
            seq.append(float(v))
        except ValueError:
            print("bad input")
    return seq
        
        
def median(numbers):
    numbers = sorted(numbers)
    n = len(numbers)
    if n % 2:
        return numbers[n // 2]
    return (numbers[n // 2] + numbers[n // 2 - 1]) / 2


def geometrisches_mittel(numbers):
    return pow(reduce(mul, numbers), 1 / len(numbers))


def get_statistics():
    values = get_input()
    return {'Median': median(values),
            'geometrisches Mittel': geometrisches_mittel(values)}



output = get_statistics()
print(output)
