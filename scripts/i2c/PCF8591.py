#Read a value from analogue input 1 
#in A/D in the PCF8591P @ address 0x48
from smbus import SMBus
 
bus = SMBus(1)
 
print("Read the A/D")
print("Ctrl C to stop")
bus.write_byte(0x48, 0x03) 
last_reading =-1
 
while(0 == 0): # do forever
    reading = bus.read_byte(0x48) # read A/D

    # Write value if change of more than 2
    if(abs(last_reading - reading) > 2):
        print(reading)
        last_reading = reading
