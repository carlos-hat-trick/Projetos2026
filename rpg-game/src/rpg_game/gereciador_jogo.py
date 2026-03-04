from .personagem import Personagem
from .guerreiro import Guerreiro
from .assasino import Assasino

heroi = Guerreiro("Arthur", 100, 15, 0 ,5)
vilao = Personagem("Orc Lider", 100, 12,50,30)
capanga = Assasino("murder" , 40 ,10, 15,60 )


#pra rodar no meu lapot tenho usado :
# "cd C:\Users\Usuario\projetos\rpg-game"
# "dir"
# "python -m src.rpg_game.gereciador_jogo" , 
# pois creio q instalei no lugar errado 😝


print("⚔️ A BATALHA COMEÇOU! ⚔️")

while heroi.esta_vivo() and vilao.esta_vivo():
    heroi.status()
    vilao.status()
    capanga.status()
    
    # Turno do Herói
    turnodoheroi = input("O que o heroi deseja fazer ? (atacar/poção)").lower()
    if turnodoheroi == "atacar":
        quematcar = input("Atacar o vilão ou o capanga ?").lower()
        if quematcar == "vilão":
            heroi.atacar(vilao)
        elif quematcar == "capanga":
            heroi.atacar(capanga)
    elif turnodoheroi == "poção":
        heroi.pocao(heroi.vida)


    if vilao.esta_vivo():
        import random
        turnovilao = random.choice(["atacar", "poção"])
        if turnovilao == "atacar":
          vilao.atacar(heroi)
        elif turnovilao == "poção":
         vilao.pocao(vilao.vida)

    if capanga.esta_vivo():
         turnodocapanga = random.choice(["atacar","poção","habilidade"])
         if turnodocapanga == "atacar":
            capanga.atacar(heroi)
    elif turnodocapanga == "poção":
         capanga.pocao(capanga.vida)
    elif turnodocapanga == "habilidade":
         capanga.aumentar_dano(capanga.aumentar_dano)

    #heroi.atacar(vilao)
    
#    if vilao.esta_vivo():
        # Turno do Vilão
#        vilao.atacar(heroi)
         print("-" * 30)

print("FIM DE JOGO!")

