import numpy as np

from goph420_M1.integration import integrate_newton
from goph420_M1.integration import integrate_gauss


def trap_result(x1,x2,f1,f2):

    result1 = integrate_newton(x1,f1,'trap')
    result2 = integrate_newton(x2,f2,'trap')

    print(f"The result using dt = 2: {result1}")
    print(f"The result using dt = 1: {result2}")

def simp_result(x1,x2,f1,f2):
    result1 = integrate_newton(x1,f1,'simp')
    result2 = integrate_newton(x2,f2,'simp')

    print(f"The result using dt = 2: {result1}")
    print(f"The result using dt = 1: {result2}")

def gauss_result():
    def f(x):
        vf = 9.81*93/47
        v0 = 100
        c = 47
        m = 93
        return (vf) + (v0 - vf)*np.e**(-(c/m)*x)

    lims = [0, 20]
    npts = 5

    result = integrate_gauss(f, lims, npts)
    print(f"Result: {result}")

def main():
    x1 = np.linspace(0,20,11)
    x2 = np.linspace(0,20,21)

    vf = 9.81*93/47
    v0 = 100
    c = 47
    m = 93

    f1 = vf + (v0 - vf)*np.e**(-(c/m)*x1)
    f2 = vf + (v0 - vf)*np.e**(-(c/m)*x2)

    print("------Using Trapezoid Rule------")
    trap_result(x1,x2,f1,f2)

    print("------Using Simpson's rule------")
    simp_result(x1, x2, f1, f2)

    print("------Using Gauss Integration Rule------")
    gauss_result()

if __name__ == '__main__':
    main()
