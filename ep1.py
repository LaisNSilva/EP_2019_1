# EP 2019-1: Escape Insper

# Alunos: 
# - Aluno A: Lais Nascimento da Silva, laisns@al.insper.edu.br
# - Aluno B: William Augusto Reis da Silva, william.silva.ismart@gmail.com
import json
def carregar_cenarios():
    with open("cenarios.json", "r") as read_file:
        cenarios = json.load(read_file)
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
    
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()
    pontos = 0
    moedas = 0
    arma = ""
    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]      

        print(cenario_atual["titulo"])
        print('-'*len(cenario_atual["titulo"]))
        print(cenario_atual["descricao"])          
        
        opcoes = cenario_atual['opcoes']
        
        
        if len(opcoes) == 0: 
            if cenario_atual == "usar comida":
                print("Você conseguiu. O jogo acabou")
            else:
                print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            print(f"Pontos = {pontos}") 
            print(f"Moedas = {moedas}")
            print(f"Arma = {arma}")
            print("Escolha sua opção: ")
            print()
            for ação, descrição in opcoes.items():
                print(f'{ação}: {descrição}')
                         
            escolha = input("O que você quer fazer? ")
            
            if nome_cenario_atual == "pobre":
                moedas -= 5
                arma += "fotos de animais fofinhos"
                print("Você só pode ter uma arma: Fotos de animais fofinhos")  
        
            elif nome_cenario_atual == "médio":
                if escolha == "fotos de animais fofinhos":
                    moedas -= 5
                    arma += "fotos de animais fofinhos"
                    print("Você tem uma arma: Fotos de animais fofinhos")
                    
                elif escolha == "machado":
                    moedas -= 10
                    arma = "machado"
                    print("Você tem como arma: machado")     
            
            elif nome_cenario_atual == "rico":
                    if escolha == "fotos de animais fofinhos":
                         moedas -= 5
                         arma += "fotos de animais fofinhos"
                         print("Você tem uma arma: Fotos de animais fofinhos")  
                    elif escolha == "machado":
                         moedas -= 10
                         arma += "machado"
                         print("Você tem como arma: machado")     
                    elif escolha == "comida":
                         moedas -= 16
                         arma += "comida"
                         print("Você tem como arma: comida")     
                    else:
                        nome_cenario_atual = "andar professor"
                        print("Você não tem armas")
                
            
            if escolha in opcoes:
                nome_cenario_atual = escolha
                if nome_cenario_atual == "bicuda no pote":
                    pontos += 8
                    moedas += 5
                    
                if nome_cenario_atual == "tele":
                    pontos += 6
                    moedas += 3
                
                if nome_cenario_atual == "porta 2":
                    pontos += 5
                    moedas += 3
                    
                if nome_cenario_atual == "chute na barriga":
                    pontos -= 10
                
                if nome_cenario_atual == "murro no olho":
                    pontos += 10 
                    moedas += 5
                    

                if nome_cenario_atual == "professor":
                    if pontos >= 13:
                        nome_cenario_atual = "professor2"                        
                
                if nome_cenario_atual == "sala secreta":
                    if moedas >= 5 and moedas < 10:
                        nome_cenario_atual = "pobre"
                        
                    elif moedas >= 10 and moedas < 16:
                        nome_cenario_atual = "médio"
                            
                    elif moedas >= 16:
                        nome_cenario_atual = "rico"
                        
                    else:
                        print("Você tem menos de cinco moedas, não pode comprar nada :(")
                        nome_cenario_atual = "andar professor"
                                                
                if nome_cenario_atual == "lutar":
                    if arma == "fotos de animais fofinhos":
                        nome_cenario_atual = "usar fotos de animais fofinhos"
                    if arma == "machado":
                        nome_cenario_atual = "usar machado"
                    if arma == "comida":
                        nome_cenario_atual = "usar comida"
                    if arma == "":
                        nome_cenario_atual = "terminar"
                        
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True
    
    print("Fim de jogo!")


# Programa principal.
if __name__ == "__main__":
    main()
