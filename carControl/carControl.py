from flask import Flask, render_template, Response
import cv2
import time
import sys
import numpy
import RPi.GPIO as GPIO

	
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index1.html')

@app.route('/right')
def right():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(16,GPIO.OUT)
	GPIO.output(16,GPIO.LOW)
	GPIO.setup(18,GPIO.OUT)
	GPIO.output(18,GPIO.HIGH)
	

	GPIO.setup(11,GPIO.OUT)
	GPIO.output(11,GPIO.HIGH)
	GPIO.setup(13,GPIO.OUT)
	GPIO.output(13,GPIO.LOW)
	
	

	
	time.sleep(0.25)
	GPIO.output(16,GPIO.LOW)
	GPIO.output(18,GPIO.LOW)

	GPIO.output(11,GPIO.LOW)
	GPIO.output(13,GPIO.LOW)	
	
	GPIO.cleanup()
	return "right"
	##return "hello right"
@app.route('/left')
def left():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(16,GPIO.OUT)
	GPIO.output(16,GPIO.HIGH)
	GPIO.setup(18,GPIO.OUT)
	GPIO.output(18,GPIO.LOW)
	

	GPIO.setup(11,GPIO.OUT)
	GPIO.output(11,GPIO.LOW)
	GPIO.setup(13,GPIO.OUT)
	GPIO.output(13,GPIO.HIGH)
	
	

	
	time.sleep(0.25)
	GPIO.output(16,GPIO.LOW)
	GPIO.output(18,GPIO.LOW)

	GPIO.output(11,GPIO.LOW)
	GPIO.output(13,GPIO.LOW)	
	
	GPIO.cleanup()
	#return render_template('index.html')
		
	return "hello left"
@app.route('/down')
def down():
	#return render_template('index.html')
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(16,GPIO.OUT)
	GPIO.output(16,GPIO.HIGH)
	GPIO.setup(18,GPIO.OUT)
	GPIO.output(18,GPIO.LOW)
	

	GPIO.setup(11,GPIO.OUT)
	GPIO.output(11,GPIO.HIGH)
	GPIO.setup(13,GPIO.OUT)
	GPIO.output(13,GPIO.LOW)
	
	

	
	time.sleep(0.5)
	GPIO.output(16,GPIO.LOW)
	GPIO.output(18,GPIO.LOW)

	GPIO.output(11,GPIO.LOW)
	GPIO.output(13,GPIO.LOW)


	
	
	GPIO.cleanup()
	return "Down"

@app.route('/up')
def up():

	
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(16,GPIO.OUT)
	GPIO.output(16,GPIO.LOW)
	GPIO.setup(18,GPIO.OUT)
	GPIO.output(18,GPIO.HIGH)
	

	GPIO.setup(11,GPIO.OUT)
	GPIO.output(11,GPIO.LOW)
	GPIO.setup(13,GPIO.OUT)
	GPIO.output(13,GPIO.HIGH)
	
	

	
	time.sleep(0.5)
	GPIO.output(16,GPIO.LOW)
	GPIO.output(18,GPIO.LOW)

	GPIO.output(11,GPIO.LOW)
	GPIO.output(13,GPIO.LOW)


	
	GPIO.cleanup()
	return "up"

@app.route('/reference')
def reference():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(15,GPIO.OUT)
	pwm=GPIO.PWM(15,100)                        ## PWM Frequency
	pwm.start(5)
 
	angle1=90
	duty= float(angle1)/10 + 2.5 
	pwm.ChangeDutyCycle(duty)
	time.sleep(1)
	GPIO.cleanup()
	return "0"

@app.route('/left90')
def left90():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(15,GPIO.OUT)
	pwm=GPIO.PWM(15,100)                        ## PWM Frequency
	pwm.start(5)
	angle1=180
	duty= float(angle1)/10 + 2.5 
	pwm.ChangeDutyCycle(duty)
	time.sleep(1)
	GPIO.cleanup()
	return "-90"

@app.route('/left45')
def left45():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(15,GPIO.OUT)
	pwm=GPIO.PWM(15,50)                       ## PWM Frequency
	pwm.start(5)
 
	angle1=110
	duty= float(angle1)/10 + 2.5 
	pwm.ChangeDutyCycle(duty)
	time.sleep(1)
	GPIO.cleanup()
	return "-45"

@app.route('/right90')
def right90():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(15,GPIO.OUT)
	pwm=GPIO.PWM(15,100)                        ## PWM Frequency
	##pwm.start(5)
 
	angle1=5
	duty= float(angle1)/10 + 2.5 
	pwm.start(duty)
	time.sleep(1)
	GPIO.cleanup()
	return "90"
		
@app.route('/right45')
def right45():
	
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(15,GPIO.OUT)
	pwm=GPIO.PWM(15,100)                        ## PWM Frequency
	pwm.start(5)
 
	angle1=45
	duty= float(angle1)/10 + 2.5 
	pwm.ChangeDutyCycle(duty)
	time.sleep(1)
	GPIO.cleanup()
	return "45"
	

if __name__ == '__main__':
    app.run(host='192.168.0.103',port=7000,debug=True,threaded = True)
    #192.168.0.103
