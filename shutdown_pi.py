import RPi.GPIO as GPIO
import os

gpio_pin_number=29
led_pin=40
GPIO.setmode(GPIO.BOARD)

GPIO.setup(gpio_pin_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin,GPIO.OUT)
GPIO.output(led_pin,GPIO.HIGH)
try:
    GPIO.wait_for_edge(gpio_pin_number, GPIO.FALLING)
    GPIO.output(led_pin,GPIO.LOW)    
    os.system("sudo shutdown -h now")
    GPIO.output(led_pin,GPIO.LOW)    
except:
    pass

GPIO.cleanup()

