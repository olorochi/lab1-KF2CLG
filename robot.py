"""Modele du robot mobile."""

from param import VITESSE_MAX, VITESSE_MIN


class Robot:
    def __init__(self, moteur_gauche, moteur_droit):
        self._moteur_gauche = moteur_gauche
        self._moteur_droit = moteur_droit

    @staticmethod
    def limiter_vitesse(vitesse):
        vitesse = float(vitesse)
        return max(VITESSE_MIN, min(VITESSE_MAX, vitesse))

    def avancer(self, vitesse):
        puissance = self.limiter_vitesse(vitesse)
        self._moteur_gauche.avancer(puissance)
        self._moteur_droit.avancer(puissance)

    def reculer(self, vitesse):
        puissance = self.limiter_vitesse(vitesse)
        self._moteur_gauche.reculer(puissance)
        self._moteur_droit.reculer(puissance)

    def pivoter_gauche(self, vitesse):
        puissance = self.limiter_vitesse(vitesse)
        self._moteur_gauche.reculer(puissance)
        self._moteur_droit.avancer(puissance)

    def pivoter_droite(self, vitesse):
        puissance = self.limiter_vitesse(vitesse)
        self._moteur_gauche.avancer(puissance)
        self._moteur_droit.reculer(puissance)

    def arreter(self):
        self._moteur_gauche.arreter()
        self._moteur_droit.arreter()

    def fermer(self):
        self.arreter()
        self._moteur_gauche.fermer()
        self._moteur_droit.fermer()
