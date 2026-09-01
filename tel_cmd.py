"""Telecommande clavier du robot."""

import sys

from ev_app_client_api import fermer_client, gen_ev_externe
from param import (
    APP_CTRL_ROBOT,
    IP_CTRL_ROBOT,
    MSG_ARRETER,
    MSG_AVANCER,
    MSG_PIVOTER_D,
    MSG_PIVOTER_G,
    MSG_RECULER,
    PAS_VITESSE,
    VITESSE_INITIALE,
    VITESSE_MAX,
    VITESSE_MIN,
)

NOM_FENETRE = "Controle robot - clavier actif"


class TelCmd:
    COMMANDES_MOUVEMENT = {
        ord("q"): MSG_PIVOTER_G,
        ord("w"): MSG_AVANCER,
        ord("e"): MSG_PIVOTER_D,
        ord("s"): MSG_RECULER,
    }

    def __init__(self, ip_robot, envoyer=gen_ev_externe):
        self.ip_robot = ip_robot
        self.vitesse = VITESSE_INITIALE
        self.derniere_commande = None
        self._envoyer = envoyer

    def envoyer_mouvement(self, type_message):
        self._envoyer(
            self.ip_robot,
            APP_CTRL_ROBOT,
            type_message,
            self.vitesse,
        )
        self.derniere_commande = type_message

    def arreter(self):
        self._envoyer(self.ip_robot, APP_CTRL_ROBOT, MSG_ARRETER)
        self.derniere_commande = None

    def modifier_vitesse(self, variation):
        nouvelle_vitesse = self.vitesse + variation
        self.vitesse = round(
            max(VITESSE_MIN, min(VITESSE_MAX, nouvelle_vitesse)),
            2,
        )
        print(f"Vitesse: {self.vitesse:.2f} m/s")
        if self.derniere_commande is not None:
            self.envoyer_mouvement(self.derniere_commande)

    def traiter_touche(self, touche):
        commande = self.COMMANDES_MOUVEMENT.get(touche)
        if commande is not None:
            self.envoyer_mouvement(commande)
        elif touche == ord(" "):
            self.arreter()
        elif touche == ord("."):
            self.modifier_vitesse(PAS_VITESSE)
        elif touche == ord(","):
            self.modifier_vitesse(-PAS_VITESSE)
        elif touche == ord("x"):
            self.arreter()
            return False
        else:
            print("Commande invalide")
        return True

    def executer(self, lire_touche):
        try:
            actif = True
            while actif:
                actif = self.traiter_touche(lire_touche())
        except KeyboardInterrupt:
            pass
        finally:
            self.arreter()


def main():
    ip_robot = sys.argv[1] if len(sys.argv) > 1 else IP_CTRL_ROBOT

    try:
        import cv2
        import numpy as np
    except ImportError as erreur:
        raise SystemExit(
            "OpenCV et NumPy ne sont pas fonctionnels"
        ) from erreur

    telecommande = TelCmd(ip_robot)
    image_vide = np.zeros((1, 1, 3), dtype=np.uint8)
    cv2.imshow(NOM_FENETRE, image_vide)
    print(f"Telecommande connecter a {ip_robot}:{APP_CTRL_ROBOT}.")

    try:
        telecommande.executer(lambda: cv2.waitKeyEx(0))
    finally:
        cv2.destroyAllWindows()
        fermer_client()


if __name__ == "__main__":
    main()
