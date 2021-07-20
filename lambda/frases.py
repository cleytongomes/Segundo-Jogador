import random

# ********* CLASSE PARA MANIPULAÇÃO DO JSON ********* #
class Frases:
    
    # Array de frases de conversa
    def __init__(self):
        self.aMaisAjudas = ["Precisa de mais alguma coisa?", "Posso te ajudar em mais algo hoje?", "Precisa de mais ajuda?"]
        self.aDesculpa = ["Desculpe, mas acho que eu não posso te ajudar com isso, posso apenas te auxiliar com coisas específicas do league of legends, como as histórias, passivas, dicas e itens"]
        self.aAjuda = ["Eu posso te ajudar dando dicas e explicando as habilidades dos campeões. Caso queira alguma dica sobre o seu campeão, diga : 'Dica mais o nome do campeão que deseja saber'. Além dissom, caso queira saber mais sobre minhas funcionalidades, visite o aplicativo da alexa e veja mais o que eu posso fazer nas descrições da skill.", "Você, invocador, pode me perguntar desde a história de campeões, dicas, habilidades e até mesmo sobre os itens!", "Eu posso falar sobre as histórias dos campeões, dicas a favor e contra, passivas, habilidades e outras coisas, basta me perguntar"]
        self.aFim = ["Até a próxima", "Qualquer coisa, estarei aqui", "Até logo, invocador"]
        self.aRepetir = ["Você poderia repetir?", "Pode repetir?"]
        self.aInicio = ["como posso te ajudar?", "o que posso fazer por você?", "Como posso te ajudar hoje?"]
        self.aSaudacao = ["Seja bem-vindo a skill 'segundo jogador'. Espero que eu possa te ajudar a entender melhor league of legends, como as histórias dos campeões e suas habilidades", "Seja bem-vindo, invocador. Estou aqui para te passar alguns conhecimentos do league of legends, como dicas para os campeões e os itens do game" ]
        self.aCancelarAcao = ["ok, ação cancelada. Posso te auxiliar em mais algo hoje?. Caso eu não possa, peça para eu parar ou diga não", "cancelado, posso te ajudar em mais alguma coisa?. Caso não possa, diga não, ou me peça para parar"]
        self.aPerguntaAjuda = ["Posso te ajudar em mais alguma coisa?", "Posso te ajudar em algo mais?"]
        self.aEmDesenv = ["Desculpe, essa funcionalidade ainda está em em desenvolvimento"]
    
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
        return "As informações são baseadas no patch 11.13.1 do LOL, atualizada em nosso sistema no dia cinco de julho de 2021"