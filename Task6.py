import matplotlib.pyplot as plt

def f(x):
	return x + 1

def p(x):
	return -x

def q(x):
	return 2

a = 0.9
b = 1.2

a0 = 1
a1 = -0.5
b0 = 1
b1 = 0
A = 2
B = 1
n = 20
h = (b - a) / n

x = []
x.append(a)
for i in range(1, n + 1):
	x.append(a + i * h)

m = []
m.append(0)
for i in range(1, n):
	result = (((h * h * q(x[i])) - 2) / (1 + h * p(x[i]) / 2))
	m.append(result)

k = []
k.append(0)
for i in range(1, n):
	result = ((1 - (h * p(x[i]) / 2)) / (1 + (h * p(x[i]) / 2)))
	k.append(result)

F = []
F.append(0)
for i in range(1, n):
	result = (f(x[i]) / (1 + (h * p(x[i]) / 2)))
	F.append(result)

c = []
c.append(a1 / ((h * a0) - a1))
d = []
d.append(A * h / a1)
for i in range(1 , n):
	cresult = 1 / (m[i] - (k[i] * c[i - 1]))
	dresult = ((h * h * F[i]) - (k[i] * c[i - 1] * d[i - 1]))
	c.append(cresult)
	d.append(dresult)

y = []
for i in range(0, n + 1):
	y.append(0.0)

yn = ((B * h) + (b1 * c[n - 1] * d[n - 1])) / ((b0 * h) + b1 * (c[n - 1] + 1))
y[n] = yn
for i in range(n - 1, 0, -1):
	yi = c[i] * (d[i] - y[i + 1])
	y[i] = yi

for i in range(1, n + 1):
	print x[i], y[i]

x.pop(0)
y.pop(0)
plt.plot(x, y)
plt.show()