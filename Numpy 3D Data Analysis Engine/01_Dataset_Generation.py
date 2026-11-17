import numpy as np
np.random.seed(42)
stations,days=5,30
temperature=np.random.uniform(15,40,(stations,days))
humidity=np.random.uniform(30,90,(stations,days))
pressure=np.random.uniform(980,1050,(stations,days))
wind_speed=np.random.uniform(0,25,(stations,days))
sensor_data = np.stack([temperature, humidity, pressure, wind_speed],axis=2)
# Save Dataset
import os
os.makedirs("datasets", exist_ok=True)
np.save("datasets/sensor_data.npy", sensor_data)
print("Dataset saved successfully!")