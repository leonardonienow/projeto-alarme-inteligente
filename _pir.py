import time


class _PIR:
    def __init__(self):
        self.detectedPresence = False
        self.findPresence()

    def findPresence(self):
        presence = False

        while True:
            print('_PIR')
            self.detectedPresence = presence
            time.sleep(1)


