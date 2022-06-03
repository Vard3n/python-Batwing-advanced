from abc import abstractmethod, ABC


class Laptop:
    @abstractmethod
    def screen(self):
        raise NotImplemented('This method was not implemented')

    @abstractmethod
    def keyboard(self):
        raise NotImplemented('This method was not implemented')

    @abstractmethod
    def touchpad(self):
        raise NotImplemented('This method was not implemented')

    @abstractmethod
    def webcam(self):
        raise NotImplemented('This method was not implemented')

    @abstractmethod
    def ports(self):
        raise NotImplemented('This method was not implemented')

    @abstractmethod
    def dynamics(self):
        raise NotImplemented('This method was not implemented')


class HPLaptop(Laptop):
    def screen(self):
        print('15 inch')

    def keyboard(self):
        print('Full size with Numpad')

    def touchpad(self):
        print('Glass with forcetouch')

    def webcam(self):
        print('5MP')

    def ports(self):
        print('USB-C')

    def dynamics(self):
        print('Bang & Olufsen')


pavilion = HPLaptop()
pavilion.screen()
pavilion.keyboard()
pavilion.touchpad()
pavilion.webcam()
pavilion.ports()
pavilion.dynamics()
