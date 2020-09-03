"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

q = (1, 3, 4, 7, 12)

def strings(A, n):
   if n == 0:
      return ['']
   return [s + c for s in strings(A, n - 1) for c in A]

options = strings(["0", "1", "2", "3", "4"], 4)

#q = set(range(1, 10))
#q = set(range(1, 200))

f_cashe = {}
def f(x):
    if x in f_cashe:
        return f_cashe[x]
    else:
        f_cashe[x] = x * 4 + 6
        return f_cashe[x]

for i in options:
    if f(q[int(i[0])]) + f(q[int(i[1])]) == f(q[int(i[2])]) - f(q[int(i[3])]):
        print(f"f({q[int(i[0])]}) + f({q[int(i[1])]}) = f({q[int(i[2])]}) - f({q[int(i[3])]})    {f(q[int(i[0])])} + {f(q[int(i[1])])} = {f(q[int(i[2])])} - {f(q[int(i[3])])}")

