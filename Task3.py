import matplotlib.pyplot as plt
import numpy
import Task2 as Task2

def phi(x, i):
    return x ** i

def f(x):
    return numpy.cos(x)

# Input data
a = 0
b = numpy.pi
N = 20
m = 2
n = N // 2
h = (b - a) / N
x_arr = []
y_arr = []
for i in range(N + 1):
    x_arr.append(a + i * h)
    y_arr.append(f(a + i * h))


def mult_phik_phij(k, j):
    result = 0
    for i in range(N + 1):
        result += phi(x_arr[i], k) * phi(x_arr[i], j)
    return result


def mult_f_phi(j):
    result = 0
    for i in range(N + 1):
        result += f(x_arr[i]) * phi(x_arr[i], j)
    return result


A = []
for i in range(m + 1):
    A.append([])
    for j in range(m + 1):
        A[i].append(mult_phik_phij(i, j))
B = []
for i in range(m + 1):
    B.append(mult_f_phi(i))


class MatrixSolving:
    def __init__(self, a, b):
        self.A = a
        self.b = b

    def t_matrix(self, k):
        t_matr = []
        for i in range(m + 1):
            t_matr.append([])
            for j in range(m + 1):
                if i == j:
                    t_matr[i].append(1)
                else:
                    t_matr[i].append(0)
        for i in range(m + 1):
            t_matr[i][k] = -self.A[i][k] / self.A[k][k]
        t_matr[k][k] = 1. / self.A[k][k]
        return t_matr

    def matrix_mult(self, matr):
        mult = []
        for i in range(m + 1):
            mult.append([])
            for j in range(m + 1):
                sum = 0
                for k in range(m + 1):
                    sum += self.A[k][j] * matr[i][k]
                mult[i].append(sum)
        self.A = mult
        mult = []
        for i in range(m + 1):
            sum = 0
            for k in range(m + 1):
                sum += matr[i][k] * self.b[k]
            mult.append(sum)
        self.b = mult

    def solve(self):
        for i in range(m + 1):
            t = self.t_matrix(i)
            self.matrix_mult(t)
        return self.b


ololo = MatrixSolving(A, B)
resultB = ololo.solve()


def F(x):
    result = 0
    for i in range(m + 1):
        result += resultB[i] * phi(x, i)
    return result

NFORF = 10
HFORF= (b - a) / NFORF
XFORF = []
YFORF = []

for i in range(NFORF + 1):
    XFORF.append(a + i * HFORF)
    YFORF.append(F(XFORF[i]))


def NormFunction(f1, f2):
    result = 0
    for i in range(N):
        result += ((f1(x_arr[i + 1]) - f2(x_arr[i + 1])) ** 2 + (f1(x_arr[i]) - f2(x_arr[i])) ** 2) * (x_arr[i + 1] - x_arr[i]) / 2.
    return numpy.sqrt(result)

print("ERROR FOR THE LEAST SQUARES")
print(abs(NormFunction(f, F)))

# The least square Graphic
plt.plot(XFORF, YFORF)
plt.plot(Task2.x_arr, Task2.gauss_arr)
plt.plot(Task2.x_arr, Task2.y_arr)
plt.plot(Task2.x_arr, Task2.newton_arr)
plt.show()