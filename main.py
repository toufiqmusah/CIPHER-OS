import machine
from dht11 import *
from time import sleep
from lcd1602 import LCD1602
import linear_regression as ln
import logistic_regression as lg
from machine import ADC, Pin, I2C

i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)
d = LCD1602(i2c, 2, 16)

dht = DHT(18)
l_intense = ADC(0)

x = list()
temp_arr = list()
humid_arr = list()
y = 0

while True:
    light_val = int(l_intense.read_u16()/256)
    temp, humid = dht.readTempHumid()
    temp_arr.append(int(temp))
    humid_arr.append(int(humid))
    y += 1
    x.append(y)
    print(len(temp_arr))
        
    if len(temp_arr) >= 10:
        temp_pred = ln.linear_regressor(x, humid_arr, 0.005, 100)
        humid_pred = ln.linear_regressor(x,temp_arr, 0.005, 100)
        print(temp_pred)
        print(humid_pred)
        temp_arr = []
        humid_arr = []
        x = []
        y = 0
        
    print(f'Temperature: {temp}')
    print(f'Humidity: {humid}')
    print(f'Light Intesn. : {light_val}')
    
    d.display()
    sleep(1)
    d.clear()
    d.print(f'Temp: {temp}')
    sleep(0.6)
    d.setCursor(0, 1)
    d.print(f'Humid: {humid}')
    sleep(1)
    d.setCursor(0, 1)
    d.print(f'Light: {light_val}')
    

    sleep(1)
    
    
