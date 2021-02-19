import json

# ********* CLASSE PARA MANIPULAÇÃO DO JSON ********* #
class Lol:

    def __init__(self):
        # Abre o arquivo json para leitura UTF8
        with open('champion.json', 'r', encoding="utf8") as json_file:
            dados = json.load(json_file)
            self.JsonCampeoes = dados['data'] # Json com os campeões especificamente
    
    # História dos campeões
    def historia(self, campeao):
        return self.JsonCampeoes[campeao]['lore']
    
    # Runa campeões (Em desenvolvimento)
    def runa(self, campeao):
        return "Desculpe, mas ainda estamos desenvolvendo essa funcionalidade"
        #return self.JsonCampeoes[campeao]['runa']