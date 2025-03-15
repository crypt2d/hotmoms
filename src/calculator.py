import time

class CPMCalculator:
    def __init__(self):
        self.total_checked = 0
        self.start_time = time.time()
    
    def increment(self):
        self.total_checked += 1
        
    def calculate(self):
        elapsed_time = time.time() - self.start_time
        minutes = elapsed_time / 60
        if minutes > 0:
            return int(self.total_checked / minutes)
        return 0
    
    def get_total(self):
        return self.total_checked

calculator = CPMCalculator()