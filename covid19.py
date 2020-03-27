import math
import matplotlib.pyplot as plt

from data import data

# Предполагаем экспоненциальную зависимость, т.е. f(x)=c*a^x, где c = f(0)

c = data[0]
a = 1.112

def f(x):
    return c*(a**x)

data_model = []
derivative = []

s = 0
for i in range(len(data)):
    data_model.append(f(i))
    s += (data[i]-f(i))**2
    if i > 0:
        derivative.append(data[i]-data[i-1])

for i in range(len(derivative)):
    print("+ ", derivative[i], " ", derivative[i]/data[i]*100, "% from cases")

s /= len(data)
s = math.sqrt(s)
print("Среднеквадратическое отклонение: ", s)

plt.gca().axes.xaxis.set_ticklabels([])
plt.gca().axes.yaxis.set_ticklabels([])
plt.plot(data)
plt.plot(data_model)
plt.show()
