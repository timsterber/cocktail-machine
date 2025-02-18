class Control_RPI:
    def __init__(self):
        self.pins = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13]
        self.tpm = 0.4     # seconds
        self.timespan = 10     # seconds
        print("Class Control_RPI initiated")
    async def process_time(self, t, pin):
        print(f"Starting measuring process: {t}s on Pin {pin}")
        return True
    def calc_tpm(self, amount_liquid) -> int:
        if(amount_liquid > 0):
            self.tpm = (self.timespan / amount_liquid) 
        return self.tpm
    def check_values(self, value_list) -> None:
        print("Values valid!")
    async def _start(self, pin):
        print(f"GPIO-Pin {pin} is ON.")
    async def _stop(self, pin):
        print(f"GPIO-Pin {pin} is OFF.")