from flask import Flask, render_template
import datetime, os
import math
from gpiozero import CPUTemperature

#Import the ADS1x15 module.
import Adafruit_ADS1x15

cpu=CPUTemperature()


# Create an ADS1115 ADC (16-bit) instance. Remember!
adc = Adafruit_ADS1x15.ADS1115()

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
GAIN = 1

#NTC resistance @25C
ntcres = 10000

#NTC constants
A1 = 0.003354
B1 = 0.000257
C1 = 0.00000262
D1 = 0.0000000638

app = Flask(__name__)

@app.route('/')
def index():
    #read adc values
    var0 = adc.read_adc(0, gain=GAIN)
    var1 = adc.read_adc(1, gain=GAIN)
    var2 = adc.read_adc(2, gain=GAIN)
    var3 = adc.read_adc(3, gain=GAIN)
    
    #calculate NTC resistance 0
    if var0 > 5:
        vin0 = (3.3/26440)*var0
        ntc0 = (1000-(1000*(vin0/3.3)))/(vin0/3.3)
        #calculate temperature 0
        ntc0temp = round(1/(A1 +(B1*math.log(ntc0/ntcres)) +(C1*math.log(ntc0/ntcres)*math.log(ntc0/ntcres))+(D1*math.log(ntc0/ntcres)*math.log(ntc0/ntcres)*math.log(ntc0/ntcres))) - 273.15,1)
    else:
        ntc0temp = "NaN"
    if var1 > 5:
        #calculate NTC resistance 1
        vin1 = (3.3/26440)*var1
        ntc1 = (1000-(1000*(vin1/3.3)))/(vin1/3.3)
        #calculate temperature 1
        ntc1temp = round(1/(A1 +(B1*math.log(ntc1/ntcres)) +(C1*math.log(ntc1/ntcres)*math.log(ntc1/ntcres))+(D1*math.log(ntc1/ntcres)*math.log(ntc1/ntcres)*math.log(ntc1/ntcres))) - 273.15,1)
    else:
        ntc1temp = "NaN"
    if var2 > 5:
        #calculate NTC resistance 2
        vin2 = (3.3/26440)*var2
        ntc2 = (1000-(1000*(vin2/3.3)))/(vin2/3.3)
        #calculate temperature 2
        ntc2temp = round(1/(A1 +(B1*math.log(ntc2/ntcres)) +(C1*math.log(ntc2/ntcres)*math.log(ntc2/ntcres))+(D1*math.log(ntc2/ntcres)*math.log(ntc2/ntcres)*math.log(ntc2/ntcres))) - 273.15,1)
    else:
        ntc2temp = "NaN"
    if var3 > 5:
        #calculate NTC resistance 2
        vin3 = (3.3/26440)*var3
        ntc3 = (1000-(1000*(vin3/3.3)))/(vin3/3.3)
        #calculate temperature 2
        ntc3temp = round(1/(A1 +(B1*math.log(ntc3/ntcres)) +(C1*math.log(ntc3/ntcres)*math.log(ntc3/ntcres))+(D1*math.log(ntc3/ntcres)*math.log(ntc3/ntcres)*math.log(ntc3/ntcres))) - 273.15,1)

    else:
        ntc3temp = "NaN"

    #cpu temperature
    cputemp = round(cpu.temperature,1)
    
    
    data = {
        'ntc0temp': ntc0temp,
        'ntc1temp': ntc1temp,
        'ntc2temp': ntc2temp,
        'ntc3temp': ntc3temp,
        'cputemp': cputemp,
        'var0': var0,
        'var1': var1,
        'var2': var2,
        'var3': var3
        }
    return render_template('index.html', **data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
