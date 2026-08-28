#!/bin/python

import cv2
import numpy as np
from ev_app_client_api import *
from messages import *
from param import *

def send(T, *args):
    gen_ev_externe(IP, PORT, T.CODE, *args)

img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow('Labo 1',img)

actif = True
while actif:
    key = cv2.waitKeyEx(0) # 0: bloque l'exécution
    if key==ord('w'):
        send(Avancer)
    elif key == ord('s'):
        send(Reculer)
    elif key == ord('q'):
        send(PivotG)
    elif key == ord('e'):
        send(PivotD)
    elif key == ord(' '):
        send(Arreter)
    elif key == ord('.'):
        send(Accel)
    elif key == ord(','):
        send(Decel)
    elif key == ord('x'):
        send(Quitter)
        actif = False

cv2.destroyAllWindows()
