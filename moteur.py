class Moteur:
    def __init__(self, en, avant, arriere, vitesse=1, freq=10):
        self.en = en
        self.__avant = avant
        self.__arriere = arriere
        self.freq = freq
        self.en.value = vitesse

    def avant(self):
        self.__avant.on()
        self.__arriere.off()

    def arriere(self):
        self.__avant.off()
        self.__arriere.on()

    def frein(self):
        self.__avant.on()
        self.__arriere.on()

    def arret(self):
        self.__avant.off()
        self.__arriere.off()
