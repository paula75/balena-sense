#!/usr/local/bin/python

# This script detects for the presence of either a BME680 sensor on the I2C bus or a Sense HAT
# The BME680 includes sensors for temperature, humidity, pressure and gas content
# The Sense HAT does not have a gas sensor, and so air quality is approximated using temperature and humidity only.

import sys
import bme680
import serial
import serial_sensor
import time
from sense_hat import SenseHat
from influxdb import InfluxDBClient
from mock_sensor import MockSensor

readfrom = 'unset'

if readfrom == 'unset':
    try:
        print 'Try serial sensor'
        sensor = serial_sensor.SerialSensor("/dev/ttyACM0", 115200)
    except:
        print 'Serial sensor not found'
    else:
        readfrom = 'serial-sensor'
        print 'Using Serial data readings'
        get_readings = serial_sensor.get_readings
# If this is still unset, no sensors were found; Use a dummy sensor
if readfrom == 'unset':
    try:
        sensor = MockSensor()
    except:
        print 'MockSensor not found'
    else:
        readfrom = 'mock-sensor'
        print 'Using Mock Sensor for readings'
        import mock_sensor
        get_readings = mock_sensor.get_readings

# quit!
if readfrom == 'unset':
    sys.exit()

# Create the database client, connected to the influxdb container, and select/create the databasepressure
influx_client = InfluxDBClient('influxdb', 8086, database='balena-sense')
influx_client.create_database('balena-sense')


while True:
    measurements = get_readings(sensor)
    influx_client.write_points(measurements)
    time.sleep(1)
