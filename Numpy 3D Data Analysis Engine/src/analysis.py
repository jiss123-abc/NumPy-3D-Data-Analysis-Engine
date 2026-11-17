import numpy as np
def load_data():
    data=np.load("datasets/sensor_data.npy")
    return data
def station_average_temperature(data):
    temperature=data[:,:,0]
    avg_temperature=np.mean(temperature,axis=1)
    return avg_temperature
def daily_average_temperature(data):
    temperature=data[:,:,0]
    daily_avg_temperature=np.mean(temperature,axis=0)
    return daily_avg_temperature
def maximum_temperature(data):
    temperature=data[:,:,0]
    max_temperature=np.max(temperature,axis=1)
    return max_temperature
def minimum_temperature(data):
    temperature=data[:,:,0]
    min_temperature=np.min(temperature,axis=1)
    return min_temperature
def temperature_standard_deviation(data):
    temperature=data[:,:,0]
    std_temperature=np.std(temperature,axis=1)
    return std_temperature
def temperature_humidity_correlation(data):
    temperature=data[:,:,0]
    humidity=data[:,:,1]
    correlation=np.corrcoef(temperature.flatten(),humidity.flatten())[0,1]
    return correlation
def detect_temperature_outliers(data):
    temperature=data[:,:,0]
    q1=np.percentile(temperature,25)
    q3=np.percentile(temperature,75)
    IQR_temperature = q3 - q1
    upper_bound = q3 + (1.5 * IQR_temperature)
    lower_bound = q1 - (1.5 * IQR_temperature)
    outliers_temperature=temperature[(temperature<lower_bound)|(temperature>upper_bound)]
    return outliers_temperature