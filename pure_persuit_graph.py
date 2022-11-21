import matplotlib.pyplot as plt
import numpy as np

vf = None
xb = []
yb = []

inputs = []

with open('./pp_input.txt') as file:
    for line in file.readlines():
        inputs.append(line.rstrip().rsplit(','))


vf = int(inputs[0][0])
xb = [int(x) for x in inputs[1]]
yb = [int(x) for x in inputs[2]]

xf = [0]
yf = [50]

for t in range(len(xb)):
    if t > 10:
        print("Time limit exceed!")
        break
        
    dist = np.sqrt( (xb[t] - xf[t])**2 + (yb[t] - yf[t])**2 )
    if dist <= 10:
        print("Target caught at Time: {}".format(t+1))
        break
    
    sin_theta = (yb[t] - yf[t]) / dist
    cos_theta = (xb[t] - xf[t]) / dist
    
    xf.append(xf[t] + vf * cos_theta)
    yf.append(yf[t] + vf * sin_theta)
    

plt.plot(xb, yb, label="Bomber", color="red")
plt.plot(xf,yf, label="Fighter", color="blue")
plt.legend()
plt.show()