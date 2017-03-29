# -*-coding:utf-8-*-


# from scipy.optimize import fsolve
from sympy import Symbol, symbols, Eq, solveset

class AR(object):
    def __init__(self, paras):
        self.paras = paras

    @property
    def is_stationary(self):
        # with scipy
        # def f(x):
        #     new_paras = []
        #     for i, para in enumerate(self.paras):
        #         if i:
        #             new_paras.append(-para*(x**i))
        #         else:
        #             new_paras.append(1.)
        #     print(new_paras)
        #     return sum(new_paras)
        # return fsolve(f,[1])

        # with sympy
        x = Symbol('x')
        equ = []
        for i, para in enumerate(self.paras):
            if i:
                equ.append(-para*(x**i))
            else:
                equ.append(1.)
        return solveset(sum(equ), x)

    @property
    def acrr(self):
        # bad implements
        paras = self.paras[1:]
        n = len(paras)
        unknowns = symbols(['rho'+str(i+1) for i in range(n)])
        for i in range(n):
            pass




    @property
    def var(self):
        pass



if __name__=="__main__":
    model = AR([1,0.7,-0.1])
    # print(model.is_stationary)
    print(1/(1-0.7*7/11+0.1*39/110)*39/110)