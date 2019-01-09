from flask import Flask, render_template
import datetime, os, time, subprocess
import math
from gpiozero import CPUTemperature
from time import sleep
from datetime import datetime

import RPi.GPIO as GPIO



cpu=CPUTemperature()

#setup ethernet LED
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)
#setup program LED
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
#setup fault LED
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)
#setup RPI LED
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)


app = Flask(__name__)

@app.route('/')

def index():

    f = open("/home/pi/Desktop/software/static/currentdata.csv", "r")
    dataStr = f.readline()
    out = []
    out = dataStr.split(',')

    data = {
        'ntc0temp': out[6],
        'ntc1temp': out[7],
        'ntc2temp': out[8],
        'ntc3temp': out[9],
        'cputemp': out[10],
        'sec': out [5],
        'min': out [4],
        'hour': out [3],
        'day': out[2],
        'month': out[1],
        'year': out[0],
        }
    return render_template('index.html', **data)
    file.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    print(dataStr)


