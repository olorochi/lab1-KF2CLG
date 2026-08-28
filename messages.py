class Message:
    def handler(self, ctx):
        print(f"message recu: {self}")


class Timeout(Message):
    CODE = 0

    def __init__(self, time):
        self.time = float(time)

    def handler(self, _):
        pass


class Avancer(Message):
    CODE = 10

    def handler(self, robot):
        robot.avant()


class Reculer(Message):
    CODE = 11

    def handler(self, robot):
        robot.arriere()


class PivotG(Message):
    CODE = 12

    def handler(self, robot):
        robot.gauche()


class PivotD(Message):
    CODE = 13

    def handler(self, robot):
        robot.droite()


class Arreter(Message):
    CODE = 14

    def handler(self, robot):
        robot.arreter()


class Accel(Message):
    CODE = 15

    def handler(self, robot):
        robot.set_vitesse(robot.get_vitesse() + 0.05)


class Decel(Message):
    CODE = 16

    def handler(self, robot):
        robot.set_vitesse(robot.get_vitesse() - 0.05)


class Quitter(Message):
    CODE = 17

    def handler(self, robot):
        raise KeyboardInterrupt # kinda hacky

messages = [Timeout, Avancer, Reculer, PivotG, PivotD, Arreter, Accel, Decel, Quitter]
