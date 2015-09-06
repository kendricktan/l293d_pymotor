import RPi.GPIO as GPIO

class l293d_pymotor:
    def __init__(self, enable_left_pin, enable_right_pin, in1_left_pin, in2_left_pin, in3_right_pin, in4_right_pin):
        # Setup GPIO ports
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(enable_left_pin, GPIO.OUT)
        GPIO.setup(enable_right_pin, GPIO.OUT)
        GPIO.setup(in1_left_pin, GPIO.OUT)
        GPIO.setup(in2_left_pin, GPIO.OUT)
        GPIO.setup(in3_right_pin, GPIO.OUT)
        GPIO.setup(in4_right_pin, GPIO.OUT)
        
        # Initial motor direction
        GPIO.output(in1_left_pin, 1)
        GPIO.output(in2_left_pin, 0)
        
        GPIO.output(in3_right_pin, 1)
        GPIO.output(in4_right_pin, 0)
        
        # Motor API (for motor speed)
        self.motor_left = GPIO.PWM(enable_left_pin, 50)
        self.motor_right = GPIO.PWM(enable_right_pin, 50)
        self.motor_left.start(0)
        self.motor_right.start(0)
        
        # Enable pins (for speed)
        self.enable_left_pin = enable_left_pin
        self.enable_right_pin = enable_right_pin

        # Input pins (for direction)
        self.in1_left_pin = in1_left_pin
        self.in2_left_pin = in2_left_pin
        self.in3_right_pin = in3_right_pin
        self.in4_right_pin = in4_right_pin
        
    # Toggles motor turning direction
    def toggle_direction(self):
        GPIO.output(self.in1_left_pin, (not GPIO.input(self.in1_left_pin)))
        GPIO.output(self.in2_left_pin, (not GPIO.input(self.in2_left_pin)))
        GPIO.output(self.in3_right_pin, (not GPIO.input(self.in3_right_pin)))
        GPIO.output(self.in4_right_pin, (not GPIO.input(self.in4_right_pin)))
        
    # Changes left motor settings
    # Speed is 0-9
    def motor_left(self, direction, speed):
        if direction == 'forwards':
            GPIO.output(self.in1_left_pin, 1)
            GPIO.output(self.in2_left_pin, 0)
        else:
            GPIO.output(self.in1_left_pin, 0)
            GPIO.output(self.in2_left_pin, 1)
            
        if speed > 0 and speed < 10:
            self.motor_left.ChangeDutyCycle(speed*99)
        else:
            self.motor_left.ChangeDutyCycle(50)
            
    # Changes right motor settings
    # Speed is 0-9
    def motor_right(self, direction, speed):
        if direction == 'forwards':
            GPIO.output(self.in3_right_pin, 1)
            GPIO.output(self.in4_right_pin, 0)
        else:
            GPIO.output(self.in3_right_pin, 0)
            GPIO.output(self.in4_right_pin, 1)
            
        if speed > 0 and speed < 10:
            self.motor_right.ChangeDutyCycle(speed*99)
        else:
            self.motor_right.ChangeDutyCycle(50)
            
            
            

