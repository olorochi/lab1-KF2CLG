class Robot:
    def __init__(self, gauche, droit, vitesse):
        self.__gauche = gauche
        self.__droit = droit

    def gauche(self):
        self.__gauche.arret()
        self.__droit.avant()

    def droite(self):
        self.__gauche.avant()
        self.__droit.arriere()

    def avant(self):
        self.__droit.avant()
        self.__gauche.avant()

    def arret(self):
        self.__droit.arret()
        self.__gauche.arret()

    def avancer(self):
        self.avant()

    def arriere(self):
        self.__droit.arriere()
        self.__gauche.arriere()

    def get_vitesse(self):
        return self.gauche.en.value

    def set_vitesse(self, vitesse):
        self.gauche.en.value = max(min(1, vitesse), 0)
        self.droite.en.value = max(min(1, vitesse), 0)
