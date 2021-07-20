import json
from SSMLStripper import SSMLStripper

# ********* CLASSE PARA MANIPULAÇÃO DO JSON ********* #
class Lol:

    def __init__(self):
        # Abre o arquivo .json dos campeões para leitura UTF8
        with open('champion.json', 'r', encoding="utf8") as json_file:
            dados = json.load(json_file)
            self.JsonCampeoes = dados['data'] # Json com os campeões especificamente
        
        # Abre o arquivo .json dos itens para leitura UTF8
        with open('itens.json', 'r', encoding="utf8") as json_file:
            dados = json.load(json_file)
            self.JsonItens = dados['data'] # Json com os campeões especificamente
        
        
    # Transforma marcação em texto
    def mark_to_text(self,text):
        ssml = SSMLStripper()
        ssml.feed(text)
        return ssml.get_data()
    
    # História dos campeões
    def historia(self, campeao):
        return self.JsonCampeoes[campeao]['lore']
    
    # Runa campeões (Em desenvolvimento)
    def runa(self, campeao):
        return "Desculpe, mas ainda estamos desenvolvendo essa funcionalidade"
        #return self.JsonCampeoes[campeao]['runa']

    # Dicas campeões (Aliados)
    def dicasAliados(self, campeao):
        dicasStr = ""

        temDica = len(self.JsonCampeoes[campeao]['allytips'])

        if(temDica != False):
            for i in range(len(self.JsonCampeoes[campeao]['allytips'])):
                dicasStr +=  "Dica {}, {}. ".format(i+1, self.JsonCampeoes[campeao]['allytips'][i])
        else:
            dicasStr = "Infelizmente não tenho nenhuma dica para esse campeão. "

        return dicasStr
    
    # Dicas campeões (Inimigos)
    def dicasContra(self, campeao):
        dicasStr = ""

        temDica = len(self.JsonCampeoes[campeao]['enemytips'])

        if(temDica != False):
            for i in range(len(self.JsonCampeoes[campeao]['enemytips'])):
                dicasStr +=  "Dica {}: {}. ".format(i+1, self.JsonCampeoes[campeao]['enemytips'][i])
        else:
            dicasStr = "Infelizmente não tenho nenhuma dica contra esse campeão. "
        
        return dicasStr
        
    # Habilidades campeão
    def habilidadesCampeao(self, campeao):
        habilidadesStr = ""
        for i in range(len(self.JsonCampeoes[campeao]['spells'])):
            habilidadesStr +=  "Habilidade {}, {}: {}. ".format(i+1, self.JsonCampeoes[campeao]['spells'][i]["name"], self.mark_to_text(self.JsonCampeoes[campeao]['spells'][i]["description"]))
        
        return habilidadesStr

    # Passiva campeão
    def passivaCampeao(self, campeao):
        passiva = self.mark_to_text(self.JsonCampeoes[campeao]['passive']['description'])
        passivaStr = "A passiva de {} se chama {}: {}. ".format(campeao, self.JsonCampeoes[campeao]['passive']['name'], passiva)
        return passivaStr
    
    # Descrição dos itens
    def descricaoItem(self, cod_item):
        nomeItem = self.JsonItens[cod_item]['name']
        descItemStr = self.JsonItens[cod_item]['plaintext']

        if(descItemStr == ""):
            return "Infelizmente não tenho informação sobre sobre o item " + nomeItem + ". "
        else:
            return "O que posso dizer sobre o item " + nomeItem + " é que " + descItemStr
            

    # Descrição dos itens
    def classeCampeao(self, campeao):
        qtdClasses = len(self.JsonCampeoes[campeao]['tags'])
        aClasses = []
        
        for i in range(qtdClasses):
            classe = self.JsonCampeoes[campeao]['tags'][i]
            if classe == "Fighter":
                aClasses.append("Lutador")
            elif classe == "Tank":
                aClasses.append("Tanque")
            elif classe == "Marksman":
                aClasses.append("Atirador")
            elif classe == "Mage":
                aClasses.append("Mago")
            elif classe == "Assassin":
                aClasses.append("Assasino")
            elif classe == "Support":
                aClasses.append("Suporte")

        return campeao + " é classificado como um campeão do tipo " + " barra ".join(aClasses)
    