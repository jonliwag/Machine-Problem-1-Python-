import numpy as np
import matplotlib.pyplot as plt

n = int(input("Please input a value for n: "))

if (n <= 9 and n >= 0):
    y1 = n**2 - 7
    n = np.linspace(0,99,100)
    y2 = n**2 - 7
    plt.stem(n, y2,'c', label='y', markerfmt='g-', use_line_collection = True)
    
elif (n >= 10 and n >= 0):
    y1 = n - 10
    n = np.linspace(0,99,100)
    y2 = n - 10
    plt.stem(n, y2,'c', label='y', markerfmt='g-', use_line_collection = True)
    
elif n < 0:
        print('error')

plt.title('Machine Problem 1')
plt.xlabel('values of n')
plt.ylabel('output of y')
plt.legend()
plt.grid()
plt.show()
