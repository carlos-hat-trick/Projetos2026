from .personagem import Personagem
import random

class Assasino(Personagem):
    def aumentar_dano(self):
        print(f"{self.nome} usou a habilidade surdina e aumentou o seu dano base!")
        self.dano += random.randint(5,9)