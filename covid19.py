import math
import matplotlib.pyplot as plt

from data import data

# Предполагаем экспоненциальную зависимость, т.е. f(x)=c*a^x, где c = f(0)

c = data[0]
a = 1.112

def f(x):
    return c*(a**x)


sigmoid_params = {
    'numerator': 4500000,
    'shift': 83,
    'power_multiplier': 0.10
}


def sigmoid(x):
    return sigmoid_params['numerator']/(1+math.exp(1)**(-(x-sigmoid_params['shift'])*sigmoid_params['power_multiplier']))


data_model = []
sigmoid_model = []
derivative = []

s = 0
for i in range(len(data)):
    data_model.append(f(i))
    s += (data[i]-f(i))**2
    sigmoid_model.append(sigmoid(i))
    if i > 0:
        derivative.append(data[i]-data[i-1])

for i in range(len(data),len(data)+60):
    sigmoid_model.append(sigmoid(i))

for i in range(len(derivative)):
    print("+ ", derivative[i], " ", derivative[i]/data[i]*100, "% from cases")

s /= len(data)
s = math.sqrt(s)
print("Среднеквадратическое отклонение: ", s)

plt.gca().axes.xaxis.set_ticklabels([])
plt.gca().axes.yaxis.set_ticklabels([])
plt.plot(data)
plt.plot(data_model)
plt.plot(sigmoid_model)
plt.show()
