from pymodbus import Framer
from pymodbus.client import ModbusSerialClient as ModbusClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
import time

readings=["Temperatur", "Conductivity"]
# Initialize Modbus RTU client
client = ModbusClient('COM7',framer= Framer.RTU, baudrate=9600, timeout=3, bytesize=8,
            parity="N",
            stopbits=2)
connected=client.connect()
if connected:
    print("Connected")
else:
    print("No connection - exit")
    exit(1) 

# Read sensor delay time in ms
response = client.read_holding_registers(0x00A4, 1, slave=30)
if response is not None and not response.isError():
    delay=response.registers[0]
else:
    delay=500

# set averating to 1
response=client.write_register(0x00AA, 1, slave=30)

# Read values
for t  in range(0,100):
    # Initiate measurement
    response=client.write_register(0x0001, 3, slave=30)  # Example for temperature measurement. Adjust for others.

    time.sleep(delay*2/1000)


    reg_count=2
    response = client.read_holding_registers(0x0053, 4, slave=30)
    if  response is not None:
        if not response.isError():
            decoder = BinaryPayloadDecoder.fromRegisters(response.registers, Endian.BIG, wordorder=Endian.BIG)
            for i in range(0, reg_count):
                print(f"{readings[i]} = {decoder.decode_32bit_float()}")
        else:
            print(f"Error: {response}")
    else:
        print("No response")

client.close()
