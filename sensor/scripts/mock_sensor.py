# Mock sensor based on stadistical distributions
import numpy as np

class MockSensor():
    def __init__(self):
        self.distribution = 'normal'
        self.temperature = 0
        self.pressure = 0
        self.humidity = 0
        self.air_quality = 0
        self.param_temperature = [20, 2]
        self.param_pressure = [27, 0.3]
        self.param_humidity = [26, 5]
        self.param_air_quality_score = [100, 20]

    def get_sensor_temperature(self):
        # normal distribution
        temp = np.random.normal(self.param_temperature[0], self.param_temperature[1], 1)
        self.temperature = temp
        return True

    def get_sensor_pressure(self):
        # normal distribution
        temp = np.random.normal(self.param_pressure[0], self.param_pressure[1], 1)
        self.pressure = temp
        return True

    def get_sensor_humidity(self):
        # normal distribution
        temp = np.random.normal(self.param_humidity[0], self.param_humidity[1], 1)
        self.humidity = temp
        return True

    def get_sensor_air_quality(self):
        # normal distribution
        temp = np.random.normal(self.param_air_quality_score[0], self.param_air_quality_score[1], 1)
        self.air_quality_score = temp
        return True


def get_readings(sensor):

    sensor.get_sensor_temperature()
    sensor.get_sensor_pressure()
    sensor.get_sensor_humidity()
    sensor.get_sensor_air_quality()

    return [
        {
            'measurement': 'balena-sense',
            'fields': {
                'temperature': float(sensor.temperature),
                'pressure': float(sensor.pressure),
                'humidity': float(sensor.humidity),
                'air_quality_score': float(sensor.air_quality_score)
            }
        }
    ]
