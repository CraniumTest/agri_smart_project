import random

def collect_sensor_data():
    # Simulating sensor readings
    return {
        'temperature': random.uniform(15, 35),   # Temperature in Celsius
        'humidity': random.uniform(40, 90),      # Humidity percentage
        'soil_moisture': random.uniform(10, 60), # Soil moisture percentage
        'fertility_index': random.uniform(0, 100) # Fertility index
    }
