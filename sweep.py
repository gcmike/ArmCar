import mraa

pin = mraa.Pwm(18)
pin.period_ms(20)
pin.enable(True)

while True:
	for x in range(180):
		pin.write(0.05+float(x)/1800)
	for x in range(180):
		pin.write(0.15-float(x)/1800)
