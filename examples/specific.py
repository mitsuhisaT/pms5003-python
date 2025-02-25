#!/usr/bin/env python

from pms5003 import PMS5003

print(
    """specific.py - Continuously print a specific data value.

Press Ctrl+C to exit!

"""
)

# Configure the PMS5003 for Enviro+
# pins and ports may vary for your hardware!

# Raspberry Pi 4 (Raspberry Pi OS)
# GPIO22 and GPIO27 are enable and reset for Raspberry Pi 4
# use "raspi-config" to enable serial, or add
# "dtoverlay=uart0" to /boot/config.txt
# pms5003 = PMS5003(device="/dev/ttyAMA0", baudrate=9600, pin_enable="GPIO22", pin_reset="GPIO27")

# Raspberry Pi 5 (Raspberry Pi OS)
# PIN15 and PIN13 are enable and reset for Raspberry Pi 5
# use "raspi-config" to enable serial, or add
# "dtoverlay=uart0-pi5" to /boot/firmware/config.txt
pms5003 = PMS5003(device="/dev/ttyAMA0", baudrate=9600, pin_enable="PIN15", pin_reset="PIN13")

# ROCK 5B
# Use "armbian-config" to enable rk3568-uart2-m0
# Disable console on ttyS2 with:
# sudo systemctl stop serial-getty@ttyS2.service
# sudo systemctl disable serial-getty@ttyS2.service
# sudo systemctl mask serial-getty@ttyS2.service
# add "console=display" to /boot/armbianEnv.txt
# pms5003 = PMS5003(device="/dev/ttyS2", baudrate=9600, pin_enable="PIN_15", pin_reset="PIN_13")

try:
    while True:
        data = pms5003.read()
        print(f"PM2.5 ug/m3 (combustion particles, organic compounds, metals): {data.pm_ug_per_m3(2.5)}")

except KeyboardInterrupt:
    pass
