import numpy as np
import matplotlib.pyplot as plt

x = np.array([2,2.5,3,3.5,4,4.5,5,5.5,6])
x = x*1e3
x = 1.23e-9/np.sqrt(x)

y1 = np.array([15.9, 14.6, 12.4, 12.2, 11.4, 10.5, 10.2, 9.8, 8.6])
y2 = np.array([27.3, 25.5, 22.4, 21.8, 19.4, 18.6, 17.8, 15.4, 13.9])


print(np.sum(x)/(np.sum(y1)*1e-3))
print(np.sum(x)/(np.sum(y2)*1e-3))

# Plotting both the curves simultaneously
plt.plot(x, y1, color='r', label='d1')
plt.plot(x, y2, color='g', label='d2')
  
# Naming the x-axis, y-axis and the whole graph
plt.xlabel("Wavelength (m)")
plt.ylabel("Deviation from centre of beam (mm)")
plt.title("Sine and Cosine functions")
  
# Adding legend, which helps us recognize the curve according to it's color
plt.legend()
  
# To load the display window
plt.show()