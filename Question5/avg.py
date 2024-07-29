weather_data = [
    {'Date': '2024-07-22', 'MaxTemp': 32, 'MinTemp': 22, 'Humidity': 60},
    {'Date': '2024-07-23', 'MaxTemp': 31, 'MinTemp': 21, 'Humidity': 65},
    {'Date': '2024-07-24', 'MaxTemp': 33, 'MinTemp': 23, 'Humidity': 55},
    {'Date': '2024-07-25', 'MaxTemp': 30, 'MinTemp': 20, 'Humidity': 70},
    {'Date': '2024-07-26', 'MaxTemp': 29, 'MinTemp': 19, 'Humidity': 75},
    {'Date': '2024-07-27', 'MaxTemp': 34, 'MinTemp': 24, 'Humidity': 50},
    {'Date': '2024-07-28', 'MaxTemp': 35, 'MinTemp': 25, 'Humidity': 45}
]

def find_highest_lowest_temps(data):
    max_temp = float('-inf')
    min_temp = float('inf')

    for entry in data:
        if entry['MaxTemp'] > max_temp:
            max_temp = entry['MaxTemp']
        if entry['MinTemp'] < min_temp:
            min_temp = entry['MinTemp']

    return max_temp, min_temp

# Example usage
highest, lowest = find_highest_lowest_temps(weather_data)
print(f"Highest Temperature: {highest}°C")
print(f"Lowest Temperature: {lowest}°C")

def count_days_above_30(data):
    count = 0

    for entry in data:
        if entry['MaxTemp'] > 30:
            count += 1

    return count

# Example usage
days_above_30 = count_days_above_30(weather_data)
print(f"Number of Days with Max Temperature Above 30°C: {days_above_30}")

def average_humidity(data):
    total_humidity = 0
    count = 0

    for entry in data:
        total_humidity += entry['Humidity']
        count += 1

    if count == 0:
        return 0  # Avoid division by zero

    return total_humidity / count

# Example usage
avg_humidity = average_humidity(weather_data)
print(f"Average Humidity: {avg_humidity}%")
