import serial

ser = serial.Serial('COM5', baudrate = 9600, timeout=1)
'''def getvalue():
    ser.write(b'g')
    arduonoData = ser.readline().decode('ascii')
    return arduonoData'''
while (1):
    #userInput = input('get data :')
    #if userInput=='y':
        #print(getvalue())
    print(ser.readline())