class Control:
    def __init__(self):
        print("Control initiated")
    def process_time(self, t, pin):
        print(f"Starting measuring process: {t}s on Pin {pin}")
        return True
    def calc_tpm(self, amount_liquid) -> int:
        return 1
    def check_values(self, value_list) -> None:
        print("Values valid!")
    def _start(self, pin):
        print(f"GPIO-Pin {pin} is ON.")
    def _stop(self, pin):
        print(f"GPIO-Pin {pin} is OFF.")