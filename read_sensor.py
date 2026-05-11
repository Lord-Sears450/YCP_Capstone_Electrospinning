from time import sleep 
from time import strftime
import board
import busio
from adafruit_ms8607 import MS8607
import globalVar

i2c = busio.I2C(board.SCL, board.SDA)
sensor = MS8607(i2c)

def readPHT():
	globalVar.press = sensor.pressure
	globalVar.temp = sensor.temperature
	globalVar.hum = sensor.relative_humidity
	
	# globalVar.press = 1002.18
	# globalVar.temp = 27.28
	# globalVar.hum = 78.58
	globalVar.wind = 8.72	# placeholder value until anenometer is working
 
	# prints timestamp and sensor values in test log
	timestamp = strftime('%H:%M:%S %p')
	printString = f'''Time: {timestamp}; Pressure: {globalVar.press} hPa; Temperature: {globalVar.temp} C; Humidity: {globalVar.hum} rH
	'''
	with open(f"{globalVar.startTime}.txt", "a") as f:
		f.write(f"{printString} ")
	
