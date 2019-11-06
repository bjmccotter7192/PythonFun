import numpy as np
import matplotlib.pyplot as plt

x = []
y = []

for i in range(100):
    x.append(i)
    y.append(i)

plt.plot(x, y)
plt.show()

# N = 500
# x = np.random.rand(N)
# y = np.random.rand(N)
# colors = (0,0,0)
# area = np.pi*3
# print(area)

# # Plot
# plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.title('Scatter plot pythonspot.com')
plt.xlabel('x')
plt.ylabel('y')
# plt.show()