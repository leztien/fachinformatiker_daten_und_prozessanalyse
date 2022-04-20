"""
Seite 181, Aufgabe 3.1
"""

def fibonacci(n):
    a, b = 1, 1
    seq = [a,b]
    
    for _ in range(n):
        a, b = b, a+b
        seq.append(b)
    return seq[:n]


ans = fibonacci(10)
print(ans, len(ans))
