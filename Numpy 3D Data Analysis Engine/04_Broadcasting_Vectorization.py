import numpy as np
data = np.load("datasets/sensor_data.npy")
temperature = data[:,:,0]
adjustment=np.array([1, -1, 2, 0, 0.5]).reshape(5,1)
print(f'{temperature.shape},{adjustment.shape}')
adjusted_temperature=temperature + adjustment
print("Adjusted temperature readings for all stations:\n",adjusted_temperature)
farenheit_temperature=temperature*9/5 + 32
print("Temperature readings in Fahrenheit for all stations:\n",farenheit_temperature)    
print(f'{temperature.shape},{farenheit_temperature.shape}')
normalization=(temperature-np.min(temperature))/(np.max(temperature)-np.min(temperature))
print("Normalized temperature readings for all stations:\n",normalization)
print(np.max(normalization),np.min(normalization),np.shape(normalization))
standardization=(temperature-np.mean(temperature))/np.std(temperature)
print("Standardized temperature readings for all stations:\n",standardization)
print(np.mean(standardization),np.std(standardization),np.shape(standardization))