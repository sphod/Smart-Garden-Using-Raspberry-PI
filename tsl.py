import time
import board
import busio
import adafruit_tsl2561

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the TSL2561 instance, passing in the I2C bus
tsl = adafruit_tsl2561.TSL2561(i2c)

# Enable the light sensor
tsl.enabled = True
time.sleep(1)

# Set gain 0=1x, 1=16x
tsl.gain = 0

# Set integration time (0=13.7ms, 1=101ms, 2=402ms, or 3=manual)
tsl.integration_time = 1

# Get raw (luminosity) readings individually
broadband = tsl.broadband
infrared = tsl.infrared

# Get raw (luminosity) readings using tuple unpacking
# broadband, infrared = tsl.luminosity

# Get computed lux value (tsl.lux can return None or a float)
lux = tsl.lux

    print("{}".format(lux))
else:
    print("No Value")

# Disble the light sensor (to save power)
tsl.enabled = False