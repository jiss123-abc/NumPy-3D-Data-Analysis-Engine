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
avg = station_average_temperature(data)
maximum = maximum_temperature(data)
minimum = minimum_temperature(data)
std = temperature_standard_deviation(data)
for i in range(5):
    print(f"Station {i+1}")
    print(f"Average: {avg[i]:.2f} °C")
    print(f"Maximum: {maximum[i]:.2f} °C")
    print(f"Minimum: {minimum[i]:.2f} °C")
    print(f"Standard Deviation: {std[i]:.2f} °C")
daily_avg = daily_average_temperature(data)
print("\nDAILY AVERAGE TEMPERATURE")
for i in range(30):
    print(f"Day {i+1}: {daily_avg[i]:.2f} °C")
correlation = temperature_humidity_correlation(data)
outliers = detect_temperature_outliers(data)
print("\nTEMPERATURE-HUMIDITY CORRELATION")
print(f"Correlation: {correlation:.4f}")
print("\nTEMPERATURE OUTLIER DETECTION")
print(f"Number of outliers: {len(outliers)}")
print("Outliers:", outliers)