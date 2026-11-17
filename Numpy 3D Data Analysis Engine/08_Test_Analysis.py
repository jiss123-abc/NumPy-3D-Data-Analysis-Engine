from src.analysis import (
    load_data,
    station_average_temperature,
    daily_average_temperature,
    maximum_temperature,
    minimum_temperature,
    temperature_standard_deviation,
    temperature_humidity_correlation,
    detect_temperature_outliers
)
data = load_data()
station_avg = station_average_temperature(data)
print("Station averages:", station_avg)
print("Shape:", station_avg.shape)
daily_avg = daily_average_temperature(data)
print("Daily averages:", daily_avg)
print("Shape:", daily_avg.shape)
max_temp = maximum_temperature(data)
print("Maximum temperature:", max_temp)
print("Shape:", max_temp.shape)
min_temp = minimum_temperature(data)
print("Minimum temperature:", min_temp)
print("Shape:", min_temp.shape)
std_temp = temperature_standard_deviation(data)
print("Temperature standard deviation:", std_temp)
print("Shape:", std_temp.shape)
correlation = temperature_humidity_correlation(data)
print("Temperature-Humidity Correlation:", correlation)
outliers = detect_temperature_outliers(data)
print("Temperature outliers:", outliers)
print("Shape:", outliers.shape)