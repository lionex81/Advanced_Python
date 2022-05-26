"""
4.* Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
and create an HPLaptop class by using your interface.
"""
from abc import abstractmethod, ABC

class Laptop:
    @abstractmethod
    def screen(self):
        raise NotImplementedError

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def webcam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError

class HPLaptop(Laptop):
    def __init__(self, screen_type, keyboard_type, touchpad_type, webcam_type, ports_type, dynamics_type):
        self.screen_type = screen_type
        self.keyboard_type = keyboard_type
        self.touchpad_type = touchpad_type
        self.webcam_type = webcam_type
        self.ports_type = ports_type
        self.dynamics_type = dynamics_type

    def screen(self):
        print(f'Screen: {self.screen_type}')

    def keyboard(self):
        print(f'Keyboard language: {self.keyboard_type}')

    def touchpad(self):
        print(f'Touchpad: {self.touchpad_type}')

    def webcam(self):
        print(f'Webcam: {self.webcam_type}')

    def ports(self):
        print(f'Ports: {self.ports_type}')

    def dynamics(self):
        print(f'Dynamics: {self.dynamics_type}')

laptop = HPLaptop("15.6,Full HD HP Notebook 15-db0218ur", "English, Ukrainian", "Yes", "Yes",
                  "2 x USB 3.0 + 1 USB 2.0 + HDMI", "Yes")

laptop.screen()
laptop.keyboard()
laptop.touchpad()
laptop.webcam()
laptop.ports()
laptop.dynamics()
