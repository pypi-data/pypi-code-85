import time


class Dhcp:
    def __init__(self, name):
        self.name = str(name)

    def run_collection(self):
        time.sleep(0.2)
