import datetime, os, time, math, Adafruit_ADS1x15
from gpiozero import CPUTemperature
from time import sleep, strftime
from datetime import datetime
import RPi.GPIO as GPIO

#setup program LED
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)

# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115(address=0x49, busnum=1)

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
GAIN = 1

#NTC resistance @25C
ntcres = 10000

#NTC constants
A1 = 0.003354
B1 = 0.000257
C1 = 0.00000262
D1 = 0.0000000638

cpu=CPUTemperature()

#100% value
fullvar = 26270

file = open("/home/pi/Desktop/software/logs/data.csv", "a")
if os.stat("/home/pi/Desktop/software/logs/data.csv").st_size == 0:
    file.write("Time,NTC 0,NTC 1,NTC 2,NTC 3, CPU Temp\n")

print("Time,NTC 0,NTC 1,NTC 2,NTC 3, CPU Temp\n")

while True:
    now = datetime.now()
    #read adc values
    var0 = fullvar - adc.read_adc(0, gain=GAIN)
    var1 = fullvar - adc.read_adc(1, gain=GAIN)
    var2 = fullvar - adc.read_adc(2, gain=GAIN)
    var3 = fullvar - adc.read_adc(3, gain=GAIN)
    
    #calculate NTC resistance 0
    if var0 > 50:
        vin0 = (3.3/26440)*var0
        ntc0 = (1000-(1000*(vin0/3.3)))/(vin0/3.3)
        #calculate temperature 0
        ntc0temp = round(1/(A1 +(B1*math.log(ntc0/ntcres)) +(C1*math.log(ntc0/ntcres)*math.log(ntc0/ntcres))+(D1*math.log(ntc0/ntcres)*math.log(ntc0/ntcres)*math.log(ntc0/ntcres))) - 273.15,1)
    else:
        ntc0temp = "NaN"
    if var1 > 50:
        #calculate NTC resistance 1
        vin1 = (3.3/26440)*var1
        ntc1 = (1000-(1000*(vin1/3.3)))/(vin1/3.3)
        #calculate temperature 1
        ntc1temp = round(1/(A1 +(B1*math.log(ntc1/ntcres)) +(C1*math.log(ntc1/ntcres)*math.log(ntc1/ntcres))+(D1*math.log(ntc1/ntcres)*math.log(ntc1/ntcres)*math.log(ntc1/ntcres))) - 273.15,1)
    else:
        ntc1temp = "NaN"
    if var2 > 50:
        #calculate NTC resistance 2
        vin2 = (3.3/26440)*var2
        ntc2 = (1000-(1000*(vin2/3.3)))/(vin2/3.3)
        #calculate temperature 2
        ntc2temp = round(1/(A1 +(B1*math.log(ntc2/ntcres)) +(C1*math.log(ntc2/ntcres)*math.log(ntc2/ntcres))+(D1*math.log(ntc2/ntcres)*math.log(ntc2/ntcres)*math.log(ntc2/ntcres))) - 273.15,1)
    else:
        ntc2temp = "NaN"
    if var3 > 50:
        #calculate NTC resistance 2
        vin3 = (3.3/26440)*var3
        ntc3 = (1000-(1000*(vin3/3.3)))/(vin3/3.3)
        #calculate temperature 2
        ntc3temp = round(1/(A1 +(B1*math.log(ntc3/ntcres)) +(C1*math.log(ntc3/ntcres)*math.log(ntc3/ntcres))+(D1*math.log(ntc3/ntcres)*math.log(ntc3/ntcres)*math.log(ntc3/ntcres))) - 273.15,1)

    else:
        ntc3temp = "NaN"

    #cpu temperature
    cputemp = round(cpu.temperature,1)
    file = open("/home/pi/Desktop/software/logs/data.csv", "a")    
    file.write(strftime("%G,%m,%d,%H,%M,%S")+"," + str(ntc0temp)+"," + str(ntc1temp)+"," + str(ntc2temp)+"," + str(ntc3temp)+"," + str(cputemp)+"\n")
    file.flush()
    file.close()

    file = open("/home/pi/Desktop/software/logs/currentdata.csv", "w")
    file.write(strftime("%G,%m,%d,%H,%M,%S")+"," + str(ntc0temp)+"," + str(ntc1temp)+"," + str(ntc2temp)+"," + str(ntc3temp)+"," + str(cputemp)+"\n")
    file.flush()
    file.close()

    print(strftime("%G,%m,%d,%H,%M,%S")+"," + str(ntc0temp)+"," + str(ntc1temp)+"," + str(ntc2temp)+"," + str(ntc3temp)+"," + str(cputemp))
    
    time.sleep(10)

