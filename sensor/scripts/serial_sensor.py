
class serialSensor():
    def __init__(self, port='/dev/ttyACM0', baudrate=115200):
        self.port = port
        self.baudrate = baudrate
        self.ser = serial.Serial(port=port, baudrate=baudrate, timeout=2)
        self.temperature = 0
        self.pressure = 0
        self.humidity = 0
        self.air_quality = 0

    def read_serial_sensor(self):
        # Change temp and light intensity from serial port
        line = readline()
        midline = line[:len(line)-4] + "}"
        dline = eval(midline)
        self.light = float(dline['light'])
        self.temperature = float(dline['temperature'])

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



def get_readings(sensor):

    sensor.read_serial_sensor()
    sensor.get_sensor_pressure()
    sensor.get_sensor_humidity()

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
