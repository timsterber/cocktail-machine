# Control Class for the pins on the Raspberry Pi.
# As inputs the object gets all numbers in milliliters.

import RPi.GPIO as GPIO
import time

class Control:
    def __init__(self):
        # Set GPIO mode
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        # Set GPIO pins: from Input1 to Input12
        self.pins = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13]
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
            
        # Set timing value (time per milliliter) # Standard value
        self.tpm = 0.1
        
        # Set timspan (For the user to set the time per milliliter)
        self.timespan = 10     # seconds
    
    # Starting the filling of the glass with self.timespan seconds
    def start_tpm(self) -> None:
        self._start(self.pins[0])
        time.sleep(self.timespan)
        self._stop(self.pins[0])
    
    def calc_tpm(self, amount_liquid) -> int:
        self.tpm = (self.timespan / amount_liquid) 
        return self.tpm
        
    #. Check input values
    def inputs(self, values) -> None:       # values is a list of integers in ml
        if len(values) != 12:
            raise ValueError(f"Error: Expected 12 values, got {len(values)} values.")
        for value in values:
            if (value >= 0 and value <= 1000) == False:
                raise ValueError(f"Error: Input {values[values.index(value)]} has {value} ml. Expected value between 0 and 1000 ml.")
        self.values = values
    
    # Start the process (private function)
    def _start(self, pin):
        GPIO.output(pin, GPIO.HIGH)
        print(f"Pin {pin} is ON. [Input {self.pins.index(pin) + 1}]")
    
    # Stop the process (private function)
    def _stop(self, pin):
        GPIO.output(pin, GPIO.LOW)
        print(f"Pin {pin} is OFF. [Input {self.pins.index(pin) + 1}]")