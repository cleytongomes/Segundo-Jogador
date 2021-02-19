import random

# ********* CLASSE PARA MANIPULAÇÃO DO JSON ********* #
class Frases:

    def __init__(self):
        self.aMaisAjudas = ["Precisa de mais alguma coisa?", "Como posso te ajudar mais hoje?", "Alguma dúvida?"]
        self.aDesculpa = ["Desculpa, não entendi", "Sinto muito, mas não entendi"]
        self.aAjuda = ["Caso queira alguma dica sobre o seu campeão, diga : 'Dica mais o nome do campeão que deseja saber'", "Você pode me perguntar desde a história de campeões, builds e até runas! Como eu posso te ajudar hoje?", "Você pode começar me pergundatnado pela história dos campeões"]
        self.aFim = ["Até a próxima. bye bye", "Qualquer coisa, estarei aqui", "Ok"]
        self.aRepetir = ["Você poderia repetir?", "Pode repetir", "hummm, você poderia repetir?"]
        self.aInicio = ["Do que você precisa?", "Como posso te ajudar?", "Diga, o que você precisa?"]
    
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