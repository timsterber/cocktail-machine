class Control:
    def __init__(self):
        print("Control initiated")
    async def process_time(self, t, pin):
        print(f"Starting measuring process: {t}s on Pin {pin}")
        return True
    async def calc_tpm(self, amount_liquid) -> int:
        return 1
    async def check_values(self, value_list) -> None:
        print("Values valid!")
    async def _start(self, pin):
        print(f"GPIO-Pin {pin} is ON.")
    async def _stop(self, pin):
        print(f"GPIO-Pin {pin} is OFF.")