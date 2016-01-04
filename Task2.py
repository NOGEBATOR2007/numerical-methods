import matplotlib.pyplot as plt
import math


# my function
def f(x):
    return (x / 2 + 1) * math.sin(x)

# init data
a = 1.0
b = 3.0
N = 20
h = (b - a) / N
n = N // 2

# arrays
differences = []
x_arr = []
y_arr = []
newton_arr = []
gauss_arr = []
newton_fluff = []
gauss_flaff = []

for i in range(N + 1):
    x_arr.append(a + (i * h))
    y_arr.append(f(x_arr[i]))

differences.append(y_arr)
for i in range(1, N + 1):
    differences.append([])
    for j in range(0, N - i + 1):
        differences[i].append(differences[i - 1][j + 1] - differences[i - 1][j])


# newton backward method finite_diff(I, m - I)
def newton(x):
    t = (x - x_arr[N]) / h
    result = y_arr[N]
    mult = 1
    for I in range(1, N + 1):
        mult *= t
        add = mult * differences[I][N - I] / math.factorial(I)
        result += add
        t += 1
    return result


def gauss(x):
    t = (x - x_arr[n]) / h
    result = y_arr[n]
    mult = 1
    for m in range(1, n + 1):
        mult *= (t - m + 1) / (2 * m - 1)
        result += mult * differences[2 * m - 1][n - m]
        mult *= (t + m) / (2 * m)
        result += mult * differences[2 * m][n - m]
    return result

for i in range(N + 1):
    gauss_arr.append(gauss(x_arr[i]))
    newton_arr.append(newton(x_arr[i]))


print("FLUFF FOR NEWTON: ")
for i in range(n + 1):
    newton_fluff.append(math.fabs(y_arr[i] - newton_arr[i]))
print(newton_fluff)

print("FLUFF FOR GAUSS: ")
for i in range(n + 1):
    gauss_flaff.append(math.fabs(y_arr[i] - gauss_arr[i]))
print(gauss_flaff)

plt.plot(x_arr, gauss_arr)
plt.plot(x_arr, y_arr)
plt.plot(x_arr, newton_arr)

plt.show()
