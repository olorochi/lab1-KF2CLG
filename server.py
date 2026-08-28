#!/bin/python

from ev_app import *
from gpiozero import PWMOutputDevice, DigitalOutputDevice
from messages import messages
from moteur import Moteur
from param import *
from robot import Robot

class CtrlRobot(EvApp):
    def __init__(self, port_no, robot):
        super().__init__(port_no)
        self.robot = robot
        self.types = { M.CODE: M for M in messages }

    def dispatch_event(self, ev):
        # # Pour un message sans données (tous sauf timeout...)
        # # Dans ev_app_client_api.py
        # ev_data = ev_data.encode('utf-8') = ""
        # # Dans ev_app.py
        # return self.donnée.split(";") = ['']
        args = [] if ev.donnée == '' else ev.split()
        try:
            mes = self.types[ev.type](*args)
            mes.handler(self.robot)
        except KeyError:
            print(f"Invalid message type: {ev}.")
        except TypeError:
            print(f"Invalid message data: {ev}.")
        except err:
            print(f"Unhandled error '{err}' for: {ev}.")

    def quitter(self):
        print("Bye bye")


in1 = DigitalOutputDevice(6)
in2 = DigitalOutputDevice(5)
ena = PWMOutputDevice(13)
in3 = DigitalOutputDevice(15)
in4 = DigitalOutputDevice(14)
enb = PWMOutputDevice(18)

gauche = Moteur(ena, in1, in2, 1)
droit = Moteur(enb, in3, in4, 1)
robot = Robot(gauche, droit)

ctrl_robot = CtrlRobot(PORT, robot)
ctrl_robot.run()
