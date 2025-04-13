#06/11/2021------------------------------------------------------------------------------------------------------------------
from random import randint
from time import sleep
item = ('\033[32mPedra\033[m','\033[33mPapel\033[m','\033[34mTesoura\033[m')
pontos_computador = 0
pontos_jogador = 0
def jog(pontos_computador, pontos_jogador):
    item_computador = randint(0,2)
    item_jogador = int(input('Escolha:\n[0]-\033[32mPedra\033[m\n[1]-\033[33mPapel\033[m\n[2]-\033[34mTesoura\033[m\n'))
    if item_jogador > 2 or item_jogador < 0:
        print('\033[31mValores inválidos\033[m')
    else:
        a = '-=-' * 11
        t = '---' * 11
        print('Pedra...')
        sleep(0.5)
        print('Papel...')
        sleep(0.5)
        print('TESOURA')
        sleep(0.5)
        print('Você escolheu {} e o computador escolheu {}'.format(item[item_jogador],item[item_computador]))
        if item_computador == item_jogador: print(f'{a}\n         \033[33mHouve um empate\033[m\n{a}')
        elif item_computador == 0 and item_jogador == 1: 
            print(f'{a}\n           \033[32mVocê venceu\033[m\n{a}') 
            pontoJ+= 1
        elif item_computador == 1 and item_jogador == 2: 
            print(f'{a}\n           \033[32mVocê venceu\033[m\n{a}')
            pontoJ+= 1
        elif item_computador == 2 and item_jogador == 0: 
            print(f'{a}\n           \033[32mVocê venceu\033[m\n{a}')
            pontoJ+= 1
        elif item_jogador == 0 and item_computador == 1: 
            print(f'{a}\n           \033[31mVocê perdeu\033[m\n{a}')
            pontoC+= 1
        elif item_jogador == 1 and item_computador == 2: 
            print(f'{a}\n           \033[31mVocê perdeu\033[m\n{a}')
            pontoC+= 1
        elif item_jogador == 2 and item_computador == 0: 
            print(f'{a}\n           \033[31mVocê perdeu\033[m\n{a}')
            pontoC+= 1
        print(f'{t}\n          Computador: {pontos_computador}\n          Você: {pontos_jogador}\n{t}')
        s_n = int(input('Quer jogar outra vez?\n[0]-Sim\n[1]-Não\n'))
        if s_n == 0:
            jog(pontos_computador,pontos_jogador)
        elif s_n == 1:
            print(f'No final, você ficou com \033[36m{pontos_jogador}\033[m pontos e o computador ficou com \033[33m{pontos_computador}\033[m pontos.')
            if pontos_computador > pontos_jogador:
                print(f'{t}\n           \033[31mVocê perdeu\033[m\n{t}')
            elif pontos_computador > pontos_jogador:
                print(f'{t}\n           \033[32mVocê venceu\033[m\n{t}')
            else:
                print(f'{t}\n         \033[33mHouve um empate\033[m\n{t}')
        else:
            print('\033[31mVALOR INVÁLIDO\033[m')
jog(pontos_computador,pontos_jogador)