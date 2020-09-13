from time import sleep
from threading import Thread
from xbox import XBoxController
import time

CONTROLLER_PATH = '/dev/input/event2'


class GarntCar:

    def __init__(self):
        self.ctrl = XBoxController(CONTROLLER_PATH)
        self.nav = {'steering': 0, 'throttle': 0}
        self.ctrl_thread = Thread(target=self.ctrl.run, args=())
        self.ctrl_thread.daemon = True

    def drive(self):
        self.ctrl_thread.start()
        self.nav['steering'] = self.ctrl.get_steering()
        self.nav['throttle'] = self.ctrl.get_throttle()




def main():


    navigate(controller)





if __name__ == "__main__":
    main()