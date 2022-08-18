#Importação da função randint
from random import randint

#Função para deixar algumas mensagens mais bonitas e organizadas
def detalhe(tam):
    print("="*tam)
detalhe(20)
print("Jogo da adivinhação")
detalhe(20)

#Declarando variáveis
cont = 0
desistiu = False
venceu = False

#Valor máximo que a máquina pode escolher
Vmax = int(input("Escolha quantos caracteres serão possíveis: "))
Vmaquina = randint(1,Vmax)
detalhe(67)
Vjogador = int(input("Digite um número e tente acertar o valor escolhido pela máquina! "))
cont = 1
#Validando caracteres
while True:
    if Vjogador == 0:
        desistiu = True
        if desistiu:
            break
    if Vjogador==Vmaquina:
        venceu = True
        break
    if Vjogador > Vmaquina:
        detalhe(50)
        Vjogador = int(input("Menos! Tente novamente ou digite '0' para sair "))
    if Vjogador < Vmaquina:
        detalhe(50)
        Vjogador = int(input("Mais! Tente novamente ou digite '0' para sair "))
    cont+=1

#Mensagens de vitória ou desistência
if desistiu:
    print(f"Desistência! Você desistiu em {cont} tentativa(s). O número escolhido foi {Vmaquina}")
if venceu:
    print(f"Parabéns! Você adivinhou o número {Vmaquina} com {cont} Tentativas")










