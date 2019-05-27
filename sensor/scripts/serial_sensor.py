import serial
import numpy as np


class SerialSensor():
    def __init__(self, port="/dev/ttyACM0", baudrate=115200):
        self.ser = serial.Serial(port, baudrate, timeout = 2)
        self.ser.port = port
        self.ser.baudrate = baudrate
        self.light = 0
        self.pressure = 0
        self.humidity = 0
        self.temperature = 0
        self.air_quality = 0
        self.param_pressure = [27, 0.3]
        self.param_humidity = [26, 5]
        self.param_air_quality_score = [100, 20]

    def read_serial_sensor(self):
        # Change temp and light intensity from serial port
        self.ser.flushInput()
        line = self.ser.readline()
        midline = str(line[:len(line)-4]) + "}"
        dline = eval(midline)
        self.air_quality = float(dline['light'])
        self.temperature = float(dline['temperature'])

    def get_sensor_pressure(self):
        # normal distribution
        temp = np.random.normal(self.param_pressure[0], self.param_pressure[1], 1)
        self.pressure = temp[0]
        return True

    def get_sensor_humidity(self):
        # normal distribution
        temp = np.random.normal(self.param_humidity[0], self.param_humidity[1], 1)
        self.humidity = temp[0]
        return True



def get_readings(sensor):

    sensor.read_serial_sensor()
    sensor.get_sensor_pressure()
    sensor.get_sensor_humidity()
    print("Light: " +str(sensor.air_quality))
    print("Temperature: " +str(sensor.temperature))
    print(type(sensor.temperature))
    print("Humidity: " +str(sensor.humidity))
    print("Pressure: " +str(sensor.pressure))

    return [
        {
            'measurement': 'balena-sense',
            'fields': {
                'temperature': float(sensor.temperature),
                'pressure': float(sensor.pressure),
                'humidity': float(sensor.humidity),
                'air_quality_score': float(sensor.air_quality)
            }
        }
    ]
