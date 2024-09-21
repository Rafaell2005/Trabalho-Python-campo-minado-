'''''''''''''''''''''''''''''''''''''''''''''''''''
Trabalho da M1(Campo mina) Introducao a python 

Professor sei que o codigo nao segue todas as suas exigências porem tive alguns problemas pessoais 
e pouco de tempo para fazer esse codigo, espero que compreenda e possa avaliar meu Trabalho 
'''''''''''''''''''''''''''''''''''''''''''''''''''
import random

LINHAS = 5
COLUNAS = 5
MINAS = 4

def criar_tabuleiro(linhas, colunas, minas):
    tabuleiro = [[' ' for _ in range(colunas)] for _ in range(linhas)]
    minas_colocadas = 0
    
    while minas_colocadas < minas:
        linha = random.randint(0, linhas - 1)
        coluna = random.randint(0, colunas - 1)
        
        if tabuleiro[linha][coluna] != '*':
            tabuleiro[linha][coluna] = '*'
            minas_colocadas += 1
    
    return tabuleiro

def contar_minas(tabuleiro, linha, coluna):
    contador = 0
    for i in range(max(0, linha - 1), min(LINHAS, linha + 2)):
        for j in range(max(0, coluna - 1), min(COLUNAS, coluna + 2)):
            if tabuleiro[i][j] == '*':
                contador += 1
    return contador

def revelar_adjacentes(tabuleiro, revelado, linha, coluna):
    for i in range(max(0, linha - 1), min(LINHAS, linha + 2)):
        for j in range(max(0, coluna - 1), min(COLUNAS, coluna + 2)):
            if not revelado[i][j]:  
                revelado[i][j] = True

def exibir_tabuleiro(tabuleiro, revelado):
    for i in range(LINHAS):
        for j in range(COLUNAS):
            if revelado[i][j]:
                if tabuleiro[i][j] == '*':
                    print('*', end=' ')
                else:
                    minas = contar_minas(tabuleiro, i, j)
                    if minas > 0:
                        print(minas, end=' ')
                    else:
                        print('-', end=' ')  
            else:
                print('#', end=' ')  
        print()

def verificar_vitoria(tabuleiro, revelado):
    for i in range(LINHAS):
        for j in range(COLUNAS):
            if tabuleiro[i][j] != '*' and not revelado[i][j]:
                return False
    return True

def jogar_campo_minado():
    tabuleiro = criar_tabuleiro(LINHAS, COLUNAS, MINAS)
    revelado = [[False for _ in range(COLUNAS)] for _ in range(LINHAS)]
    
    while True:
        exibir_tabuleiro(tabuleiro, revelado)
        
        while True:
            linha = input("Digite a linha (0 a 4): ")
            if linha.isdigit() and 0 <= int(linha) < LINHAS:
                linha = int(linha)
                break
            else:
                print("Valor inválido! Digite um número entre 0 e 4.")
        
        while True:
            coluna = input("Digite a coluna (0 a 4): ")
            if coluna.isdigit() and 0 <= int(coluna) < COLUNAS:
                coluna = int(coluna)
                break
            else:
                print("Valor inválido! Digite um número entre 0 e 4.")
        
        if tabuleiro[linha][coluna] == '*':
            print("Você pisou em uma mina! Fim de jogo.")
            exibir_tabuleiro(tabuleiro, [[True for _ in range(COLUNAS)] for _ in range(LINHAS)])
            break
        
        minas_proximas = contar_minas(tabuleiro, linha, coluna)
        
        if minas_proximas > 0:
            revelado[linha][coluna] = True  
        else:
            revelar_adjacentes(tabuleiro, revelado, linha, coluna) 
        
        if verificar_vitoria(tabuleiro, revelado):
            print("Parabéns! Você venceu!")
            exibir_tabuleiro(tabuleiro, [[True for _ in range(COLUNAS)] for _ in range(LINHAS)])
            break


def exibir_regras():
    print("\nRegras do Jogo:")
    print("(I) Se você escolher um campo com uma mina, o jogo termina e você perde.")
    print("(II) Se o campo tiver minas próximas, será mostrado o número correspondente de minas ao redor.")
    print("(III) Se o campo não tiver minas próximas, ele e seus 8 campos adjacentes serão revelados.\n")

def menu():
    while True:
        print("\n-----MENU-----")
        print("1. Começar o Jogo")
        print("2. Como funciona o Jogo")
        print("3. Sair")
        print("-----------------")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            jogar_campo_minado()
        elif escolha == '2':
            exibir_regras()
        elif escolha == '3':
            print("Até a proxima")
            print("Saindo do jogo......")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu()