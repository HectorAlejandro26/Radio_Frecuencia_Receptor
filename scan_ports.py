import serial.tools.list_ports as puertos

for puerto in puertos.comports():
    print(puerto, f'Fabricante: {puerto.manufacturer}')
