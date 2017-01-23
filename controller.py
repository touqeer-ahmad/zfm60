import MySQLdb
import time
import datetime
import RPi.GPIO as GPIO
from gpiozero import LED
import hashlib
import time
from pyfingerprint.pyfingerprint import PyFingerprint
from fingercode import enroll, search, info, delete

#Database Connection
db = MySQLdb.connect("localhost", "root", "stevens123", "fpd")
curs=db.cursor()

#LED indication Light
GPIO.setmode(GPIO.BCM)
led =LED(17)

#Sensor Initialization
try:
    f = PyFingerprint('/dev/ttyAMA0', 57600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)

#Required Functions

def insert(slot):
    curs.execute ("INSERT INTO myapp_employee(slot,date,timestamp)values(%s,CURRENT_DATE(), NOW())",(slot))
    db.commit()
    print "Data committed" + "\n"

def getenrollstatus():
    db = MySQLdb.connect("localhost", "root", "stevens123", "fpd")
    curs=db.cursor()
    curs.execute ("SELECT * FROM myapp_enroll")
    #print "\nID     	Status"
    #print "======================="
    for reading in curs.fetchall():
        pass#print str(reading[0])+"	"+str(reading[1])
    return reading[1]

def update():
    curs.execute ("UPDATE myapp_enroll SET event = 'off' WHERE iD =1")
    db.commit()
    #print "\nData Updated\n"

def delr():
    curs.execute ("DELETE FROM myapp_enroll WHERE iD = 3 LIMIT 1")
    db.commit()
    print "Row Deleted\n"

def read(slot):
    db = MySQLdb.connect("localhost", "root", "stevens123", "fpd")
    curs=db.cursor()
    curs.execute ("SELECT * FROM myapp_employee where slot=%s",(slot))
    for reading in curs.fetchall():
        fname = reading[4]
        lname = reading[5]
    return fname

def runsearch():
    while True:
        pass
    
def runController():
    currentMode = getenrollstatus()
    if currentMode == 'on':
        print "Enrollment Function Initiating"
        led.on()
        time.sleep(3)
        slot = enroll()
        message = "Already there!"
        if slot == message:
            pass
        else:
            insert(slot)
            print "Enrollment function successfully completed"
            time.sleep(1)
        update()
    elif currentMode == 'off':
        print "Normal Mode Running"
        #runsearch()
        led.off()
        message = 'No match found!'
        slot = search()
        if slot == message: 
            pass
            #print message
        else:
             fname = read(slot)
             print str(fname)
        time.sleep(2)
    return True

while True:
    try:
        runController()
        time.sleep(2)
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()


