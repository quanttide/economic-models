from sympy import Symbol, symbols, Eq, solveset, solve

'''
x1 = Symbol('x1')
x2 = Symbol('x2')
p1 = 7./11
p2 = 39./110
result = solve(
    [Eq(x1 + p1 * x2, p1),
     Eq(p1 * x1 + x2, p2)],
    (x1, x2),
)
print(result)
'''


# result = 1.96/10*(1+2*0.8**2+2*0.7**2+2*0.6**2+2*0.5**2)**0.5

# print(result)



from numpy import matrix
'''
paras = [0.8, 0.7, 0.6, 0.5, 0.4]

for i in range(1,6):
    print i
    m1 = []
    if i==1:
        m1 = [1]
    else:
        for j in range(i):
            m1.append()

    m2 = paras[0:i]

    x1 = matrix(m1)
    x2 = matrix(m2)

    result = x1.I*x2
    print(result)
'''

m1 = matrix([[1,1],[1,1]])
m2 = matrix([1,1])
result = m1.I*m2.T
print(result)
