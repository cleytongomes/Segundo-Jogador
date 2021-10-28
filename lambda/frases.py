import random

# ********* CLASSE PARA MANIPULAÇÃO DO JSON ********* #
class Frases:
    
    # Array de frases de conversa
    def __init__(self):
        self.aMaisAjudas = ["Precisa de mais alguma coisa? responda com 'sim' ou 'não'", "Posso te ajudar em mais algo hoje? responda com 'sim' ou 'não' ou com a sua necessidade", "Precisa de mais ajuda? responda com 'sim' ou 'não' ou com a sua necessidade"]
        self.aDesculpa = ["Desculpe, mas acho que eu não posso te ajudar com isso, posso apenas te auxiliar com coisas específicas do league of legends, como as histórias, passivas, dicas e itens"]
        self.aAjuda = [
            '''Eu posso te ajudar dando dicas e explicando as habilidades dos campeões. Caso queira alguma dica sobre o seu campeão, diga
            'Dica mais o nome do campeão que deseja saber'. Além disso caso queira saber mais sobre minhas funcionalidades, visite o aplicativo da alexa e leia a descrição da skill''',
            
            "Você pode me perguntar as histórias dos campeões, runas, habilidades, passivas, dicas e até mesmo os itens",
            
            "Eu posso falar sobre as histórias dos campeões, dicas a favor e contra, passivas, habilidades e outras coisas, basta me perguntar"]

        self.aFim = ["Tudo bem. Até a próxima invocador", "Tudo bem. Qualquer coisa, estarei aqui", "Ok. Até logo invocador"]
        self.aRepetir = ["Você poderia repetir? Por favor, seja específico", "Pode repetir? Por favor, seja específico"]
        self.aInicio = ["como posso te ajudar?", "o que posso fazer por você?", "Como posso te ajudar hoje?"]

        self.aSaudacao = ["Seja bem-vindo a skill 'segundo jogador'. Espero que eu possa te ajudar a entender melhor league of legends, como as histórias dos campeões e suas habilidades. Caso tenha alguma dúvida, apenas diga 'ajuda'",
                          "Seja bem-vindo invocador. Estou aqui para te passar alguns conhecimentos do league of legends, como dicas para os campeões e os itens do game. Caso tenha alguma dúvida do que eu posso fazer, basta dizer 'ajuda'" ]
        
        self.aCancelarAcao = ["ok, ação cancelada. Precisa de mais alguma coisa? Caso não precise, peça para eu parar ou diga 'não'", "Ação cancelada, posso te ajudar em mais alguma coisa? Caso eu não possa, diga 'não', ou me peça para parar"]
        
        self.aPerguntaAjuda = ["Posso te ajudar em mais alguma coisa? responda com 'sim', 'não' ou com a sua necessidade", "Posso te ajudar em algo mais? responda com 'sim', 'não' ou com a sua necessidade"]
        
        self.aEmDesenv = ["Desculpe, mas essa funcionalidade ainda está em desenvolvimento"]
    
    def fimMensagemAjuda(self):
        return random.choice(self.aMaisAjudas)
    
    def desculpa(self):
        return random.choice(self.aDesculpa)
    
    def ajuda(self):
        return random.choice(self.aAjuda)

    def fim(self):
        return random.choice(self.aFim)
    
    def repetir(self):
        return random.choice(self.aRepetir)

    def inicio(self):
        return random.choice(self.aInicio)
    
    def saudacao(self):
        return random.choice(self.aSaudacao)
    
    def perguntaAjuda(self):
        return random.choice(self.aPerguntaAjuda)

    def cancelarAcao(self):
        return random.choice(self.aCancelarAcao)
    
    def emDesenvolvimento(self):
        return random.choice(self.aEmDesenv)
    
    def versaoLol(self):
        return "As informações são baseadas no patch 11.21.1 do LOL, atualizada em nosso sistema no dia vinte e seis de outubro de 2021"