# a
class Person:
    def __init__(self):
        right_arm = Arm("Usually people handshake with this arm")
        left_arm = Arm("This arm important as well")
        self.arms = (right_arm, left_arm)


class Arm:
    def __init__(self, handshake):
        self.handshake = handshake


hands = Person()
print(hands.arms[0].handshake)


# b
class CellPhone:
    def __init__(self, screen):
        self.screen = screen


class Screen:
    def __init__(self, type):
        self.type = type


screen = Screen('OLED')
phone = CellPhone(screen)