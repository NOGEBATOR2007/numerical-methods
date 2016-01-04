import matplotlib.pyplot as plt
import math

def f(x):
	return x ** 2
	return (x / 2 + 1) * math.sin(x)

a = 1.0
b = 3.0
N = 20
h = (b - a) / N

def rectangles(eps, m, iterations = 0, count = 0, result1 = 0):
	count += 1
	result2 = result1
	result1 = 0
	deltax = (b - a) / m
	for i in range(m):
		result1 += deltax * f(a + (i + 0.5) * deltax)
		iterations += 1
	if abs(result1 - result2) / (pow(2, 2) - 1) > eps:
		return rectangles(eps, m * 2, iterations, count, result1)
	return result1, result2, iterations, count

def trapezies(eps, m, iterations = 0, count = 0, result1 = 0):
	h = (b - a) / m
	count += 1
	result2 = result1
	result1 = 0
	result1 += (h / 2) * (f(a) + f(b))
	for i in range(1, m):
		result1 += h * f(a + i * h)
		iterations += 1
	if (abs(result1 - result2) / (pow(2, 2) - 1) > eps):
		return trapezies(eps, m * 2, iterations, count, result1)
	return result1, result2, iterations, count

def simpsons(eps, m, iterations = 0, count = 0, result1 = 0):
	h = (b - a) / m
	count += 1
	result2 = result1
	result1 = 0
	result1 += (h / 6) * (f(a) + f(b))
	for i in range(1, m):
		result1 += (h / 3) * (f(a + i * h) + 2 * f(a + (i - 0.5) * h))
		iterations += 1
	result1 += 4 * f(a + (m - 0.5) * h) * (h / 6)
	iterations += 1
	if (abs(result1 - result2) / (pow(2, 4) - 1) > eps):
		return simpsons(eps, m * 2, iterations, count, result1)
	return result1, result2, iterations, count

def xi(ti):
	return (((b + a) / 2) + ((b - a) / 2) * ti)

def gauss4():
	t1 = t4 = 0.861136
	t2 = t3 = 0.339981
	t1 *= -1
	t2 *= -1
	c1 = c4 = 0.347855
	c2 = c3 = 0.652145
	result = ((b - a) / 2) * (c1 * f(xi(t1)) + c2 * f(xi(t2)) + c3 * f(xi(t3)) + c4 * f(xi(t4)))
	return result

def gauss5():
	t1 = t5 = 0.90618
	t2 = t4 = 0.538469
	t3 = 0
	t1 *= -1
	t2 *= -1
	c1 = c5 = 0.23693
	c2 = c4 = 0.47863
	c3 = 0.56889
	result = ((b - a) / 2) * (c1 * f(xi(t1)) + c2 * f(xi(t2)) + c3 * f(xi(t3)) + c4 * f(xi(t4)) + c5 * f(xi(t5)))
	return result



eps = 0.0000001
print("Rectangles")
print(rectangles(eps, 20))
print("Trapezies")
print(trapezies(eps, 20))
print("Simpsons")
print(simpsons(eps, 20))
print("Gauss 4")
print(gauss4())
print("Gauss 5")
print(gauss5())


#plot initialization and drawing
x_arr = []
y_arr = []
for i in xrange(N + 1):
	x_arr.append(a + i * h)
	y_arr.append(f(x_arr[i]))
plt.plot(x_arr, y_arr)
#plt.show()
