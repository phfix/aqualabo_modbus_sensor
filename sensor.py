
#from pymodbus.constants import Endian
#from pymodbus.payload import BinaryPayloadDecoder
#from pymodbus.payload import BinaryPayloadBuilder
#from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus import Framer
from pymodbus.client import ModbusSerialClient as ModbusClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
import time

# Initialize Modbus RTU client
client = ModbusClient('COM7',framer= Framer.RTU, baudrate=9600, timeout=3, bytesize=8,
            parity="N",
            stopbits=2)
connected=client.connect()
if connected:
    print("Connected")
else:
    exit(1) 

response = client.read_holding_registers(0x00A4, 1, slave=30)
if response is not None and not response.isError():
    delay=response.registers[0]
else:
    delay=500

# set averating to 1
response=client.write_register(0x00AA, 1, slave=30)

for t  in range(0,100):
    # Initiate measurement
    response=client.write_register(0x0001, 3, slave=30)  # Example for temperature measurement. Adjust for others.
#    if response is not None:
#        print(response)
    # Assuming delay has been accounted for...
    # delay 1s
    
    #time.sleep(2)
    #delay 500 milliseconds
    time.sleep(delay*2/1000)
    # Read temperature (example)
    #response = client.read_coils(0x0001, 2, slave=30)
    reg_count=2
    response = client.read_holding_registers(0x0053, 4, slave=30)
    #floatvalue=client.read_float(0x53,2,slave=30)
    #response = client.read_input_registers(0x0053, 1, slave=30)
    temperature = None
    if  response is not None:
        print(response)
        
        if not response.isError():
            decoder = BinaryPayloadDecoder.fromRegisters(response.registers, Endian.BIG, wordorder=Endian.BIG)
            for i in range(0, reg_count):
                print(f"reg[{i}]= {decoder.decode_32bit_float()}")
        else:
            print(f"Error: {response}")

client.close()
