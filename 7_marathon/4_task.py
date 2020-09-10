class WashingMachine:
    def __init__(self):
        self.startWashing()
        
    def startWashing(self):
        Washing()
        Rinsing()
        Spinning()

class Washing:
    def __init__(self):
        print('Washing...')

class Rinsing():
    def __init__(self):
        print('Rinsing...')
    
class Spinning():
    def __init__(self):
        print('Spinning...')
