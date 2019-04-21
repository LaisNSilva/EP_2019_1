# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Lais Nascimento da Silva, laisns@al.insper.edu.br
# - aluno B: William Augusto Reis da Silva, william.silva.ismart@gmail.com

def carregar_cenarios():
    cenarios = {
        "inicio": {
                "titulo": "Saguão do perigo",
                "descricao": "Você esta no saguão de entrada do Insper",
                "opcoes": {
                    "andar professor": "Tomar o elevador para o andar do professor",
                    "biblioteca": "Ir para a biblioteca",
                    "fab lab": "Ir ao FABLAB"
            }
        },
        "andar professor": {
                "titulo": "Andar do desespero",
                "descricao": "Você chegou ao andar da sala do seu professor",
                "opcoes": {
                    "return": "Tomar o elevador para o saguão de entrada",
                    "sala secreta":"Arriscar entrar em mais uma sala",
                    "professor": "Falar com o professor"
            }
        },
        "sala secreta": {
                "titulo": "Preparando para o combate",
                "descricao": "Aqui você pode comprar ferramentas para te auxiliar no combate final",
                "opcoes":{
                        "fotos de animais fofinhos":" Tente amolecer o coração do professor por 5 moedas",
                        "machado":"Agressividade para ameaçar por 10 moedas",
                        "comida":"professores de barriga vazia são muito mais crueis, tente deixá-lo feliz por 16 moedas",
                        "andar professor":"Caaso não tenho moedas volte ao andar no professor"
             }
        },
        "fotos de animais fofinhos":{
                "titulo":"Você ganhou fotos de animais fofinhos!",
                "descricao":"Pela suas moedas, você ganhou este presentão. Agora, vá descobir se o professor gosta de animais fofinhos",
                "opcoes":{
                        "andar professor":"o combate se aproxima"
            }
        },
        "machado":{
                "titulo":"escolha agressiva",
                "descricao":"descubra se causará medo no professor",
                "opcoes":{
                        "andar professor":"o combate se aproxima"
            }
        },
        "comida":{
                "titulo":"que delicia de escolha",
                "descricao":"encha o bucho do professor e veja qual será a reação",
                "opcoes":{"andar professor":"o combate se aproxima"
            }
        },
        "professor": {
                "titulo": "O monstro do Python",
                "descricao": "Você foi pedir para o professor adiar o EP. "
                             "O professor revelou que é um monstro disfarçado. "
                             "Se você tem mais de 16 pontos, pode tentar ir para o combate mais difícil do jogo. "
                             "Caso tenha menos que 16 pontos, não pode fazer e o monstro devotou sua alma",
                "opcoes": {}
        },
        "biblioteca": {
                "titulo": "Caverna da tranquilidade",
                "descricao": "Você está na biblioteca, há um monstro que taca livros nas pessoas",
                "opcoes": {
                        "recepcao": "Voltar para o saguão de entrada",
                        "combate":"Enfrentar o monstro para ganhar força para enfrentar o professor"
            }
        },
        "combate":{
                "titulo":"E aí, vai encarar?", 
                "descricao" : "Você deve escolher como golpear o monstro, caso deseje lutar, ou ir para outro local",
                "opcoes":{
                        "chute no calcanhar": "Você irá chutar o calcanhar do monstro",
                        "bicuda no pote":"você irá dar um chute na cabeça do monstro"
            }
        },
        "chute no calcanhar":{
                "titulo": "Trollamos você",
                "descricao":"O calcanhar do monstro é muito forte, você perdeu este combate :(",
                "opcoes": {}                              
        },
        "bicuda no pote":{
                "titulo": "Você acertou em cheio!",
                "descricao": "Esse golpe é fatal para o monstro, você venceu e ficou mais forte, GANHOU 8 PONTOS E 5 MOEDAS",
                "opcoes":{
                        "recepcao": "Voltar para o saguão de entrada"
            }
        },
        "fab lab":{
                "titulo": "O maior lab de engenhocas do país",
                "descricao": "Você está no FABLAB!",
                "opcoes":{
                        "tele": "Você irá se teletransportar para algum local. E aí, vai arriscar?!",
                        "recepcao": "Sou covarde, hehe. Quero voltar ao início"                        
            }
        },
        "tele":{
              "titulo": "VOCÊ É MUITO SORTUDO!!!!",
              "descricao": "Você ganhou 5 pontos E 6 moedas. Isso vai garantir que você tenha melhor possibilidade de conseguir o seu objetivo",
              "opcoes":{
                      "recepcao": "Voltar ao início",
                      "andar professor": "Ser corajoso e já ir enfrentar o professor",
                      "biblioteca": "Ir à biblioteca, sou uma pessoa estudiosa :D"
            }
        },
        "recepcao": {
                "titulo": "De volta ao saguão do perigo",
                "descricao": "Você esta no saguão de entrada do Insper",
                "opcoes":{
                    "andar professor": "Tomar o elevador para o andar do professor",
                    "fablab": "Ir ao FABLAB"
            }
        },
        "fablab":{
                "titulo": "Achou que ia ganhar pontos de novo, né?",
                "descricao": "Você está de novo no FABLAB, porém não vai conseguir pontos, hehe! (será?)",
                "opcoes":{
                    "andar professor": "Ir enfrentar o professor. A hora de entregar o EP está chegando!",
                    "andar das portas": "Ir ao andar desconhecido por todos"
            }
        },
        "andar das portas":{
                "titulo": "Andar de escolhas!!!!!",
                "descricao":"Você deve escolher uma das portas",
                "opcoes":{
                        "porta 1": "Desejo ir a esta porta a qual não possuo conhecimento sobre o que tem",
                        "porta 2": "Desejo ir a esta outra porta que também não tenho a mínima ideia"} 
        },
        "porta 1":{
                "titulo": "A PORTA DO MAL!!!!",
                "descricao": "Você não tem muita sorte, deu de cara com o monstro EIKOLAS!!!!!!. Você pode entrar em combate com o monstro ou se teletransportar",
                "opcoes":{
                        "combate1": "Enfrentar o monstro para tentar ganhar pontos",
                        "teletransporte": "Vou fugir desse monstro :O"
            }
        },
        "teletransporte":{
                "titulo": "SE DEU MAL!!",
                "descricao": "Você foi teletransportado para o mundo do nada :(",
                "opcoes": {}            
        },
        "porta 2":{
                "titulo": "VOCÊ É UM SORTUDO",
                "descricao": "Foi feliz em sua escolha, ganhou 5 pontos e 3 moedas",
                "opcoes":{
                        "return": "Voltar à recepção",
                        "andar professor": "Ir ao andar do professor para enfrentá-lo (ou não)!",
            }
        },
        "combate1":{
                "titulo": "O pequeno combate",
                "descricao": " Você foi muito corajoso em escolher enfrentrar esse monstro, escolha o golpe",
                "opcoes":{
                        "chute na barriga":"Você irá dar um chute muito forte na barriga do EIKOLAS",
                        "murro no olho":"Um soco muito forte"
            }
        },
        "chute na barriga":{
                "titulo": "Péssima escolha :(",
                "descricao": "Esse golpe não é capaz de matar o EIKOLAS, você perdeu 10 pontos ",
                "opcoes":{
                        "recepcao": "Voltar à recepção",
                        "andar das portas": "Ir ao andar desconhecido por todos"
            }
        },
        "murro no olho":{
                "titulo":"ACERTOU EM CHEIO!",
                "descricao": "O murro foi capaz de atingir o celebro do monstro e matá-lo na mesma hora, você ganhou 10 pontos e 5 moedas!!",
                "opcoes":{
                        "recepcao": "Voltar à recepção",
                        "andar das portas": "Ir ao andar desconhecido por todos"
            }
        },
        "return":{
                "titulo": "De volta ao saguão do perigo",
                "descricao": "Você esta no saguão de entrada do Insper",
                "opcoes":{
                    "andar professor": "Tomar o elevador para o andar do professor",
                    "teletransporte": "Quero me teletransportar para o mundo do nada"
            }
        },
        "professor2":{
                    "titulo": "VOCÊ VENCEU!!!! (mesmo? Acho que não...)",
                    "descricao": "Você possui mais de 16 pontos e, por conta disso, o professor adiou o EP para você!!",
                    "opcoes": {
                            "fim": "Consegui meu objetivo, estou livre agora e não quero fazer mais nada :D",
                            "lutar": "Não me contento com isso, quero conseguir mais coisas com o professor"
            }
        },
        "fim":{
                "titulo": "Você venceu uma luta e decidiu acabar assim? TEMOS QUE MUDAR ESSA ATITUDE! AS LUTAS NÃO ACABAM NUNCA",
                "descricao": "Venceu o RAULZÃO e conseguiu adiar o EP (mas não soube que é para amanhã, e valendo menos pontos hahahaha)",
                "opcoes": {}
        },
        "lutar":{
                "titulo": " é hora de usar a rama que você comprou ",
                "descricao": "Agora só porque adiou o EP, acha que vai conseguir mais coisa do Raul? Achou errado, infelizmente",
                "opcoes": {
                        "usar fotos de animais fofinhos":"teste a sensibilidade do professor",
                        "usar machado":" teste  a coragem desse monstro",
                        "usar comida":"teste sua fome"
                }
        },
        "usar fotos de animais fofinhos":{
                "titulo": "arma arriscada",
                "descricao":"o professor ignorou os fafuras, ele é uma criatura cruel",
                "opcoes":{
                        "terminar": "fim do jogo"
                }
        },
        "terminar":{
                "titulo":" HAHAHAHAHA ",
                "descricao":"Agora só porque adiou o EP, achou que ele iria amolecer com fotos fofas, achou errado",
                "opcoes":{}
        },
        "usar machado":{
                "titulo":"péssima escolha",
                "descricao":"o monstro ficou infurecido, e demorou sua alma",
                "opcoes":{}
        },
        "usar comida":{
                "titulo":"boa escolha",
                "descricao":"O monstro adorou esse mimo, e adiou o Ep sem perdas de pontos",
                "opcoes":{}
        }
    }
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
            
            
            if escolha in opcoes:
                nome_cenario_atual = escolha
                if nome_cenario_atual == "bicuda no pote":
                    pontos += 8
                    moedas+=5
                    
                if nome_cenario_atual == "tele":
                    pontos += 6
                    moedas+=3
                
                if nome_cenario_atual == "porta 2":
                    pontos += 5
                    moedas+=3
                    
                if nome_cenario_atual == "chute na barriga":
                    pontos -= 10
                
                if nome_cenario_atual == "murro no olho":
                    pontos += 10 
                    moedas += 5
                    
                if nome_cenario_atual == "professor":
                    if pontos > 16:
                        nome_cenario_atual = "professor2"                        
                
                if nome_cenario_atual == "sala secreta":
                    if moedas >= 5 and moedas < 10:
                        nome_cenario_atual = "fotos de animais fofinhos"
                        moedas -= 5
                        arma += "Fotos de animais fofinhos"
                        print("Você tem uma arma: Fotos de animais fofinhos")
                    
                    elif moedas >= 10 and moedas < 16:
                        nome_cenario_atual = "machado"
                        moedas -= 10
                        arma += "machado"
                        print("Você tem como arma: machado")
                    
                    elif moedas >= 16:
                        nome_cenario_atual = "comida"
                        moedas -= 16
                        arma += "comida"
                        print("Você tem como arma: comida")
                    else:
                        nome_cenario_atual = "andar professor"
                        print("Você não tem armas")
                        
                if nome_cenario_atual == "luta":
                    if arma == "fotos de animais fofinhos":
                        nome_cenario_atual = "usar fotos de animais fofinhos"
                    if arma == "machado":
                        nome_cenario_atual = "usar machado"
                    if arma == "comida":
                        nome_cenario_atual = "usar comida"
                        
                        
                        
                        
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True
    
    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()

