
#  Read from Aqualabo Conductivity sensor

## Introduction

This project provides a Python script for reading temperature and conductivity from a sensor using Modbus RTU protocol. The sensor is interfaced via a RS485 to USB converter connected to a computer.

## Setup

The code is designed to run on a machine with a serial port connection to the sensor. Ensure you have a RS485 to USB converter properly connected to both the sensor and the computer.

### Prerequisites

- Python 3.x
- `pymodbus` library

To install the required Python library, run:

```
pip install pymodbus[serial]         
```
## Sensor and Register Configuration
The script is configured to read the following parameters:

- Temperature (°C)
- C4E conductivity (µS/cm)
Other parameters like salinity (ppt) and TDS - Kcl (ppm) are mentioned in the code but not actively read in this example.

## Usage
Modify the serial port settings in the script to match your configuration (e.g., COM7, baud rate, parity, stop bits).
Set the Modbus slave ID to match your sensor's configuration (slave=30 in the example).

## Run the script:
```bash
Copy code
python sensor.py
```
The script initiates a measurement, waits for a delay to ensure data is ready, and then reads the temperature and conductivity values in a loop.

## Known problems
The modbus reports errors now and then.
```bash
Modbus Error: [Input/Output] No Response received from the remote slave/Unable to decode response
Error: Modbus Error: [Input/Output] No Response received from the remote slave/Unable to decode response
```
## Output
The script prints the temperature and conductivity readings to the console. In case of communication errors or no response, appropriate error messages are displayed.

## Customization
You can modify the script to change the number of readings, the parameters to be read, or add new functionalities like logging the data to a file or sending it to a server.

For more detailed information on the Modbus registers and their usage, refer to the sensor's documentation.
https://en.aqualabo.fr/   "Modbus SDI12 Sensor documentation.7z"