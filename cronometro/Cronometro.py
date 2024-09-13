import time
import os

class Cronometro:
    def __init__(self, segundos = 0, minutos = 0, horas = 0):
        self.segundo = segundos
        self.minuto = minutos
        self.hora = horas

    def __repr__(self):
        return f'{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}'

    def incremento(self):
        self.segundo += 1
        if self.segundo >= 60:
            self.segundo = 0
            self.minuto += 1

        if self.minuto >= 60:
            self.minuto = 0
            self.hora += 1

    def start(self):
        while True:
            os.system('cls')
            print(self)
            self.incremento()
            time.sleep(1)

c = Cronometro()
c.start()