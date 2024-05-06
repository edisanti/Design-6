import matplotlib.pyplot as plt
from pandas import *
from scipy import stats

data = read_csv('cpudata.csv')
x = data['CPU Usage']
y = data['Available Memory']

# Time series
plt.plot(y, 'r', lw=2, label='Available Memory')
plt.plot(x, 'b', lw=2, label='CPU Usage')
plt.xticks([209,333,452,703],['21:00','21:30','22:00','22:30'])
plt.xlabel('Time')
plt.legend(loc='lower center')
plt.title('EllaD 2024-05-06')

# Histogram of CPU usage
plt.figure()
num_bins = 35
n, bins, patches = plt.hist(x, num_bins, density=1, facecolor='blue', alpha=0.5)
plt.xlabel('CPU Usage')
plt.ylabel('Probability')
plt.title('EllaD 2024-05-06')

# Histogram of temperature
plt.figure()
num_bins = 30
n, bins, patches = plt.hist(y, num_bins, density=1, facecolor='red', alpha=0.5)
plt.xlabel('Available Memory')
plt.ylabel('Probability')
plt.title('EllaD 2024-05-06')

# Horizontal box plot of CPU usage
plt.figure()
plt.boxplot(x, 0, '+', 0)
plt.xlabel('CPU Usage')
plt.title('EllaD 2024-05-06')

# Vertical box plot of temperature
plt.figure()
plt.boxplot(y, 0, '+')
plt.ylabel('Available Memory')
plt.title('EllaD 2024-05-06')

# Scatter diagram with a linear regression line
plt.figure()
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
plt.xlabel('CPU Usage')
plt.ylabel('Available Memory')
plt.plot(x, y, 'bo')
l = [slope * i + intercept for i in x]
plt.plot(x, l, 'r', lw=2)
plt.title('EllaD 2024-05-06')

plt.show()
