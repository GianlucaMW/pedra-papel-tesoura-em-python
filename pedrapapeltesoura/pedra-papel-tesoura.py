import random
import time

def tabela(score_em, score_pc, score_pl):
    print("Tabela de Pontuação:\nJogador: ", score_pl, " ", "Computador: ", score_pc, "\n", "Empates: ", score_em)


def escolhas(score_em, score_pc, score_pl):
    escolha_jogo = ['PEDRA', 'PAPEL', 'TESOURA']
    print('''Escolha uma das opções:
    { 1 } PEDRA
    { 2 } PAPEL
    { 3 } TESOURA''')
    escolha_player = int(input('DIGITE SUA ESCOLHA: '))  # escolha do jogador
    escolha_pc = random.choice(escolha_jogo)  # escolha random do pc
    if escolha_player == 1:  # escolha 1 do jogador pedra
        print("PEDRA")
        time.sleep(0.7)
        print("PAPEL")
        time.sleep(0.7)
        print("TESOURA!!!")
        time.sleep(0.7)
        if escolha_pc == 'PEDRA':  # computador escolheu pedra
            print('\033[1;33m=-=-=-=-=-=-=-=-=-=-=EMPATE!!=-=-=-=-=-=-=-=-=-=-=-=\033[m '
                  '\nO computador escolheu {} \ne o jogador PEDRA!!.'.format(escolha_pc))
            score_em += 1

        elif escolha_pc == 'PAPEL':  # computador escolheu papel
            print('\033[1;31m=-=-=-=-=-=-=-=-=-=-=DERROTA!!!=-=-=-=-=-=-=-=-=-=-=\033[m '
                  '\nO computador escolheu {} \ne o jogador PEDRA!!.'.format(escolha_pc))
            score_pc += 1

        elif escolha_pc == 'TESOURA':  # computador escolheu tesoura
            print('\033[1;32m=-=-=-=-=-=-=-=-=-=-=VITÓRIA!!!=-=-=-=-=-=-=-=-=-=-=\033[m '
                  '\nO computador escolheu {} \ne o jogador PEDRA!!.'.format(escolha_pc))
            score_pl += 1

    elif escolha_player == 2:  # escolha 2 do jogador papel
        print("PEDRA")
        time.sleep(0.7)
        print("PAPEL")
        time.sleep(0.7)
        print("TESOURA!!!")
        time.sleep(0.7)
        if escolha_pc == 'PEDRA':  # computador escolheu pedra
            print('\033[1;32m=-=-=-=-=-=-=-=-=-=-=VITÓRIA-=-=-=-=-=-=-=-=-=-=-=-=\033[m '
                  '\nO computador escolheu {} \ne o jogador PAPEL!!.'.format(escolha_pc))
            score_pl += 1

        elif escolha_pc == 'PAPEL':  # computador escolheu papel
            print('\033[1;33m=-=-=-=-=-=-=-=-=-=-=-EMPATE=-=-=-=-=-=-=-=-=-=-=-=-=\033[m '
                  '\nO computador escolheu {} \ne o jogador PAPEL!!.'.format(escolha_pc))
            score_em += 1

        elif escolha_pc == 'TESOURA':  # computador escolheu tesoura
            print('\033[1;31m=-=-=-=-=-=-=-=-=-=-=-DERROTA=-=-=-=-=-=-=-=-=-=-=-=-=\033[m '
                  '\nO computador escolheu {} \ne o jogador PAPEL!!.'.format(escolha_pc))
            score_pc += 1

    elif escolha_player == 3:  # escolha 3 do jogador tesoura
        print("PEDRA")
        time.sleep(0.7)
        print("PAPEL")
        time.sleep(0.7)
        print("TESOURA!!!")
        time.sleep(0.7)
        if escolha_pc == 'PEDRA':#computador escolheu pedra
            print('\033[1;31m=-=-=-=-=-=-=-=-=-=-=-=DERROTA=-=-==-=-=-=-=-=-=-=-=-=-=-\033[m '
                  '\nO computador escolheu {} \ne o jogador TESOURA!!.'.format(escolha_pc))
            score_pc += 1

        elif escolha_pc == 'PAPEL':  # computador escolheu papel
            print('\033[1;32m=-=-=-=-=-=-=-=-=-=-=-=-VITORIA=-=-=-=-=-=-=-=-=-=-=--=-=\033[m '
                  '\nO computador escolheu {} \ne o jogador TESOURA!!.'.format(escolha_pc))
            score_pl += 1

        elif escolha_pc == 'TESOURA':# computador escolheu tesoura
            print('\033[1;33m=-=-=-=-=-=-=-=-=-=-=-=-=EMPATE=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[m '
                  '\nO computador escolheu {} \ne o jogador TESOURA!!.'.format(escolha_pc))
            score_em += 1

    else:  # nenhuma opção
        print('\033[31m{}ERROR{}\033[m'.format('=-=' * 10, '=-=' * 10))
        print('\033[31m                         OPÇÃO INVÁLIDA\033[m')
        print('\033[31m{}ERROR{}\033[m'.format('=-=' * 10, '=-=' * 10))
    keep = ' '
    while keep != 'sim' and keep != 's' and keep != 'n' and keep != 'não' and keep != 'nao':
        keep = str(input('Deseja continuar? [S/N]: ')).lower().strip()
        if keep == 'sim' or keep == 's':
            escolhas(score_em, score_pc, score_pl)
        else:
            tabela(score_em, score_pc, score_pl)
            break


if __name__ == '__main__':
    score_em = 0
    score_pl = 0
    score_pc = 0
    escolhas(score_em, score_pc, score_pl)
