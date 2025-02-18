# Control Class for the pins on the Raspberry Pi.
# As inputs the object gets all numbers in milliliters.

import RPi.GPIO as GPIO
import asyncio

class Control_RPI:
    def __init__(self):
        # Set GPIO pins: from Input1 to Input12
        self.pins = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13]
        
        # Reset all GPIO Pins
        self.reset_pins()
        
        # Set timing value (time per milliliter) # Standard value
        self.tpm = 0.4     # seconds
        
        # Set timspan (For the user to set the time per milliliter)
        self.timespan = 10     # seconds
        
    def reset_pins(self):
        # Set GPIO mode
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.HIGH)

    async def process_time(self, t, pin):
        print(f"Starting measuring process: {t}s on Pin {pin}")
        await self._start(self.pins[pin -1])
        await asyncio.sleep(t)
        await self._stop(self.pins[pin -1])
        return True
        
    
    def calc_tpm(self, amount_liquid) -> int:
        if(amount_liquid > 0):
            self.tpm = (self.timespan / amount_liquid) 
        return self.tpm
        
        
    # Check input values
    def check_values(self, value_list) -> None:       # value_list is a list of integers in ml
        if len(value_list) != 12:
            raise ValueError(f"Error: Expected 12 values, got {len(value_list)} values.")
        for value in value_list:
            if (value >= 0 and value <= 1000) == False:
                raise ValueError(f"Error: Input {value_list[value_list.index(value)]} has {value} ml. Expected value between 0 and 1000 ml.")
        self.values = value_list
        print("Values valid!")
    
    # Start the process (private function)
    async def _start(self, pin):
        GPIO.output(pin, GPIO.LOW)
        print(f"GPIO-Pin {pin} is ON. [Input {self.pins.index(pin) + 1}]")
    
    # Stop the process (private function)
    async def _stop(self, pin):
        GPIO.output(pin, GPIO.HIGH)
        print(f"GPIO-Pin {pin} is OFF. [Input {self.pins.index(pin) + 1}]")