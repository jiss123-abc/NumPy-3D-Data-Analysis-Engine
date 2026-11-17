import numpy as np
data = np.load("datasets/sensor_data.npy")
temperature=data[:,:,0]
avg_temperature=np.mean(temperature,axis=1)
print(f'Average temperature: {avg_temperature}')
daily_avg_temperature=np.mean(temperature,axis=0)
print(f'Daily average temperature: {daily_avg_temperature}')
print(f'Median temperature : {np.median(temperature)}',
      f'\nStandard deviation: {np.std(temperature)}',
      f'\nMinimum temperature: {np.min(temperature)}',
      f'\nMaximum temperature: {np.max(temperature)}',
      f'\nVariance: {np.var(temperature)}')
print("25th percentile:", np.percentile(temperature, 25))
print("50th percentile:", np.percentile(temperature, 50))
print("75th percentile:", np.percentile(temperature, 75))
humidity=data[:,:,1]
pressure=data[:,:,2]
wind_speed=data[:,:,3]
print(f'correlation between temperature and humidity: {np.corrcoef(temperature.flatten(),humidity.flatten())[0,1]}')
print(f'correlation between temperature and pressure: {np.corrcoef(temperature.flatten(),pressure.flatten())[0,1]}')
print(f'correlation between temperature and wind speed: {np.corrcoef(temperature.flatten(),wind_speed.flatten())[0,1]}')
print(f'Average temperature: {np.mean(temperature,axis=1)}',
      f'\nAverage humidity: {np.mean(humidity,axis=1)}',
      f'\nAverage pressure: {np.mean(pressure,axis=1)}',
      f'\nAverage wind speed: {np.mean(wind_speed,axis=1)}')
print(f'Average temperature across 30 days: {np.mean(temperature,axis=1)}',
      f'\nMaximum temperature across 30 days: {np.max(temperature,axis=1)}',
      f'\nMinimum temperature across 30 days: {np.min(temperature,axis=1)}',
      f'\nStandard deviation of temperature across 30 days: {np.std(temperature,axis=1)}')
print(f'Average humidity across 30 days: {np.mean(humidity,axis=1)}',
      f'\nMaximum humidity across 30 days: {np.max(humidity,axis=1)}',
      f'\nMinimum humidity across 30 days: {np.min(humidity,axis=1)}',
      f'\nStandard deviation of humidity across 30 days: {np.std(humidity,axis=1)}')
print(f'Average pressure across 30 days: {np.mean(pressure,axis=1)}',
      f'\nMaximum pressure across 30 days: {np.max(pressure,axis=1)}',
      f'\nMinimum pressure across 30 days: {np.min(pressure,axis=1)}',
      f'\nStandard deviation of pressure across 30 days: {np.std(pressure,axis=1)}')
print(f'Average wind speed across 30 days: {np.mean(wind_speed,axis=1)}',
      f'\nMaximum wind speed across 30 days: {np.max(wind_speed,axis=1)}',
      f'\nMinimum wind speed across 30 days: {np.min(wind_speed,axis=1)}',
      f'\nStandard deviation of wind speed across 30 days: {np.std(wind_speed,axis=1)}') 
print(f'the average of all 30 days for all four measurements at each station.: {np.mean(data,axis=1)}')   
highest_temp_station=np.argmax(np.mean(temperature,axis=1))
lowest_temp_station=np.argmin(np.mean(temperature,axis=1))
print(f'Station with the highest average temperature: Station {highest_temp_station+1}')
print(f'Station with the lowest average temperature: Station {lowest_temp_station+1}')
highest_avg_temperature_5stations=np.argmax(np.mean(temperature,axis=0))
lowest_avg_temperature_5stations=np.argmin(np.mean(temperature,axis=0))
print(f'Day with the highest average temperature across all stations: Day {highest_avg_temperature_5stations+1}')
print(f'Day with the lowest average temperature across all stations: Day {lowest_avg_temperature_5stations+1}')
q1=np.percentile(temperature,25)
q3=np.percentile(temperature,75)
IQR_temperature = q3 - q1
upper_bound = q3 + (1.5 * IQR_temperature)
lower_bound = q1 - (1.5 * IQR_temperature)
print(f'Interquartile range (IQR) of temperature readings: {IQR_temperature}'
      f'\nUpper bound for outliers: {upper_bound}',
      f'\nLower bound for outliers: {lower_bound}')
outliers_temperature=temperature[(temperature<lower_bound)|(temperature>upper_bound)]
print(f'Outliers in temperature readings: {outliers_temperature}',
      f'\nNumber of outliers:{len(outliers_temperature)}')

