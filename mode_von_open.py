"""
Seite 153
"""

f = open("file.txt", mode='w+')
n = f.write("0123456789ABCDEF\b")

for i in range(0, n+1, 3):
    f.seek(i)
    f.write('*')

f.seek(0)
s = f.read()
print(s)

f.close()
