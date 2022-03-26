import asyncio
import time
from multiprocessing import Process
import threading

from _pir import _PIR
from rfid import *
from _pir import *


class Main:
    def __init__(self):
        self.runProcesses()

    def runProcesses(self):
        threading.Thread(target=RFID).start()
        threading.Thread(target=_PIR).start()

    def RFID(self):
        self.RFID = RFID()

    def _PIR(self):
        self._PIR = _PIR()


Main()
