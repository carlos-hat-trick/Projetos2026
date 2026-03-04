import random

class Personagem:
    
    def __init__(self, nome:str, vida:int, forca:int, mana:int , esquivar:int)->None:
        self.nome = nome
        self.vida = vida
        self.forca = forca
        self.mana = mana
        self.esquivar = esquivar

    def status(self):
        print(f"--- {self.nome} | Vida: {self.vida} | Força: {self.forca} | Mana: {self.mana} ---")

    def esta_vivo(self)->bool:
        return self.vida > 0
        
    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"☠️ {self.nome} foi derrotado!☠️")

    def atacar(self, oponente):
        dano = self.forca + random.randint(1, 5)
        #esquivar = dano - random.randint(0,5)
        if oponente.tentar_esquivar():
            print(f"{oponente.nome} esquivou do seu ataque")
        else:
            print(f"⚔️ {self.nome} atacou {oponente.nome} e causou {dano} de dano!")
            oponente.receber_dano(dano)
        
    #def esquivar(self,esquivar, dano):
     #   if oponente.receber_dano(dano) :
      #      dano - random.randint(0,5)

    def tentar_esquivar(self) -> bool : # porcentual
        return random.randint(1,100) <= self.esquivar
    
    def contra_ataque(self,oponente):
        self.atacar(oponente)

    def pocao(self, vida, uso_pocoes=0):
        if uso_pocoes >= 3:
            print("Você já usou o máximo de poções (3)!")
            return uso_pocoes
        
        pocao = vida + random.randint(1, 6)
        if self.vida < 30:
            print("Usar poção para se curar ?")
            print("1.Sim, usar")
            print("2.Não, esperar pra usar")
            escolha = input("O que quer fazer ?")
            if escolha == "1":
                self.vida = pocao
                uso_pocoes += 1
                print(f" Poção usada! Vida: {self.vida} | Usos restantes: {3 - uso_pocoes}")
        
        return uso_pocoes