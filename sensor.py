#!usr/bin/python3
import RPi.GPIO as GPIO
import cgi, cgitb
import os
import time
import datetime
import MySQLdb
from time import strftime
from w1thermsensor import W1ThermSensor
import requests
import json
import random
import sqlite3

def measure_temperature(sensor):

##    GPIO.setmode(GPIO.BCM)
##    TEMP = 21


    print "Temperature Measurement in progress"

##    GPIO.setup(TEMP,GPIO.IN)
    temperature=sensor.get_temperature()
                
##    else:
##            print "Waiting For Sensor To Settle"
##
##            temperature = int(random.gauss(27,0.9))

    time.sleep(2)

    return temperature

def write_to_db(sensor):
    # Get data from sensor
    temperature = measure_temperature(sensor)
    print "Content-type:text/html\r\n\r\n"
    print ""
    print ""
    print "Data Storage"
    print ""
    print "" 
    print temperature
  
    #Code to write the recorded temperature in the MYSQL database 'temperature_measurement' and table 'temperature_at_all_times'
##    db = MySQLdb.connect(host= "127.0.0.1",port= 3306,user= "root",passwd= "sangan",db= "temperature_measurement")
    db=sqlite3.connect('/home/pi/SampleProgram/data.db')
    cur = db.cursor()
    
    dateWrite = time.strftime("%Y-%m-%d")
    timeWrite = time.strftime("%H:%M:%S")
    try:
        cur.execute("INSERT INTO 'temperature' ('DATE', 'TIME', 'TEMPERATURE') VALUES (?,?,?)", (dateWrite,timeWrite,temperature))
        db.commit()
        result= cur.fetchone()
        print db
        print "\nProcess finished"
    except e:
        print e
        db.rollback()
        print "\nProcess Failed to Complete"
        cur.close()
        db.close()
        
    return temperature

def write_to_cloud(sensor):
    # Get data from server
    temperature = write_to_db(sensor)
  
    print ("Content-type:text/html\r\n\r\n")
    print ("")
    print ("")
    print ("Data Storage")
    print ("")
    print ("")
    print (temperature)
    firebase_url = 'https://istarmcs-997b1.firebaseio.com/'

    try:
        
        #current time and date
        timeWrite = time.strftime('%H:%M:%S')
        dateWrite = time.strftime('%d/%m/%Y')

        print (str(temperature)+ ',' + timeWrite + ',' + dateWrite)

        #insert record
        data = {'Date':dateWrite,'Time':timeWrite,'Value':temperature}
        result = requests.post(firebase_url+'/temperature.json', data=json.dumps(data))
        print 'Record inserted. Result Code = ' + str(result.status_code) + ',' + result.text
        
    except IOError:
        print('Error! Something went wrong.')

if __name__ == '__main__':
    sensor = W1ThermSensor()
    try:
        while True:
                finaltemp = write_to_cloud(sensor)
                print "finaltemp", finaltemp
                time.sleep(10)
                
    finally: GPIO.cleanup()

    
