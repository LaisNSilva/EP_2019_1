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
                    "recepcao": "Tomar o elevador para o saguão de entrada",
                    "professor": "Falar com o professor"
            }
        },
        "professor": {
                "titulo": "O monstro do Python",
                "descricao": "Você foi pedir para o professor adiar o EP. "
                             "O professor revelou que é um monstro disfarçado "
                             "e devorou sua alma.",
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
                "descricao": "Esse golpe é fatal para o monstro, você venceu e ficou mais forte, GANHOU 8 PONTOS!",
                "opcoes":{
                        "inicio": "Voltar para o saguão de entrada"
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
              "descricao": "Você ganhou 5 pontos. Isso vai garantir que você tenha melhor possibilidade de conseguir o seu objetivo",
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
                "descricao": "Você está de novo no FABLAB, porém não vai conseguir pontos, hehe! (será)",
                "opcoes":{
                    "andar professor": "Ir enfrentar o professor. A hora de entregar o EP está chegando!",
                    "biblioteca": "Ir à biblioteca",
                    "andar das portas": "Ir ao andar desconhecido por todos"
            }
        },
        "andar das portas":{
                "titulo":"andar de escolhas",
                "descricao":"você deve escolher uma das portas",
                "opcoes":{
                        "porta 1":"Desejo ir a esta porta a qual não possuo conhecimento sobre o que tem",
                        "porta 2":"Desejo ir a esta outra porta que também não tenho a mínima ideia"} 
        },
        "porta 1":{
                "titulo":"A PORTA DO MAL!!!!",
                "descricao":"Você não tem muita sorte, deu de cara com o monstro EIKOLAS!!!!!!. Você pode entrar em combate com o monstro ou se teletransportar",
                "opcoes":{
                        "combate":"enfrentar o monstro para tentar ganhar pontos",
                        "teletransporte":" você pode fugir do monstro"
            }
        },
        "teletransporte":{
                "titulo": "SE DEU MAL!!",
                "descricao": "Você foi teletransportado para o mundo do nada :(",
                "opcoes":{}            
        },
        "porta 2":{
                "titulo": "VOCÊ É UM SORTUDO",
                "descricao": "você foi feliz em sua escolha, ganhou 8 pontos",
                "opcoes":{
                        "recepcao": "Voltar à recepção",
                        "andar professor": "Ir ao andar do professor para enfrentá-lo (ou não)!",
            }
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
            print("Escolha sua opção: ")
            print()
            for ação, descrição in opcoes.items():
                print(f'{ação}: {descrição}')
            escolha = input("O que você quer fazer? ")

            
            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu! :(")


# Programa principal.
if __name__ == "__main__":
    main()

