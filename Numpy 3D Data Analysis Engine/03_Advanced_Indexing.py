import numpy as np
data = np.load("datasets/sensor_data.npy")
print(data[[0,2,4], :, :])
temperature=data[:,:,0]
high_temperature=temperature[temperature>35]
print("Temperature above 35:",high_temperature)
print("Number of high temperature readings:",np.sum(temperature>35)) 
print("highest temperature reading:",np.max(temperature))
print("lowest temperature reading:",np.min(temperature))
temperature=data[0,:,0]
print("Temperature readings for station 1:",temperature)
print("Temperature above 35 for station 1:",temperature[temperature>35])
print("Temperature 35 and 38 for station 1:",temperature[(temperature>35) & (temperature<38)])

