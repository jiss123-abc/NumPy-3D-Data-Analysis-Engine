import numpy as np
data = np.load("datasets/sensor_data.npy")
print(data[0])
print(data[:,9,:])
print(data[:,:,0])
print(data[:3,:7,:2])
