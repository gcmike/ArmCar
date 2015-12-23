import web
import mraa
import thread
import val
import os

"""
    Set 4 pwm outputs for meArm
    Each servo requires the pwm period to be 20ms
"""
pinA = mraa.Pwm(18)
pinB = mraa.Pwm(19)
pinC = mraa.Pwm(20)
pinD = mraa.Pwm(21)
pinA.period_ms(20)
pinB.period_ms(20)
pinC.period_ms(20)
pinD.period_ms(20)
pinA.enable(True)
pinB.enable(True)
pinC.enable(True)
pinD.enable(True)

"""
    Set the control of 2 dc motors with 4 pins
    Using the H-bridge motor driver, the high or
    low of the pins control the rotation direction
    of the dc motors
"""
pinL1 = mraa.Gpio(12)
pinL2 = mraa.Gpio(13)
pinR1 = mraa.Gpio(45)
pinR2 = mraa.Gpio(46)
pinL1.dir(mraa.DIR_OUT)
pinL1.write(0)
pinL2.dir(mraa.DIR_OUT)
pinL2.write(0)
pinR1.dir(mraa.DIR_OUT)
pinR1.write(0)
pinR2.dir(mraa.DIR_OUT)
pinR2.write(0)

urls = (
	'/servo', 'servo'
)
app = web.application(urls,globals())

class servo:
	def GET(self):
        data = web.input(a='90',b='90',c='90',d='90',l='1',r='1') # get data from GET request with default value
        """
            Store the values in val.py for further usage
            This is the key for the servos to be controled at all times
            rather than running the server response with single execution
        """
        val.a = int(data.a)
		val.b = int(data.b)
		val.c = int(data.c)
		val.d = int(data.d)
		val.l = int(data.l)
		val.r = int(data.r)
        
        """
            Control servos and dc motors
        """
		pinA.write(0.05+float(val.a)/1800)
		pinB.write(0.05+float(val.b)/1800)
		pinC.write(0.05+float(val.c)/1800)
		pinD.write(0.05+float(val.d)/1800)
		if val.l == 0:
			pinL1.write(0)
			pinL2.write(1)
		elif val.l == 2:
			pinL2.write(0)
			pinL1.write(1)
		else:
			pinL1.write(0)
			pinL2.write(0)
		if val.r == 0:
			pinR1.write(0)
			pinR2.write(1)
		elif val.r == 2:
			pinR2.write(0)
			pinR1.write(1)
		else:
			pinR1.write(0)
			pinR2.write(0)
		return str(val.a) + ' , ' + str(val.b) + ' , ' + str(val.c) + ' , ' + str(val.d) + ' , ' + str(val.l) + ' , ' + str(val.r)

if __name__ == "__main__":
    thread.start_new_thread(app.run()) # start a new thread for running server
    """
        This part keeps running the execution so that the servos are under control
    """
	while 1:
		print val.a
		print val.b
		print val.c
		print val.d
