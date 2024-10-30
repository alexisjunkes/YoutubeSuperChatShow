import io
import random
import sys
import os
os.system("")
import time
import json
#############################################
try:
    import pygame.image
except:
    os.system('pip install pygame')

try:
    import pytchat
except:
    os.system('pip install pytchat')

try:
    from win32com.client import Dispatch
except:
    os.system('pip install pywin32')

try:
    import requests
except:
    os.system('pip install requests')

try:
    import gtts
except:
    os.system('pip install gtts')
#############################################



class Menassegam():
    def __init__(self,Configs):
        self.Configs = Configs
        self.language = self.Configs["Language"]
        self.song_end = True
        
    def GetImage(self,PY = "",ImagURL = ""):
        ImagURL =  ImagURL
        r = requests.get(ImagURL)
        img = io.BytesIO(r.content)
        self.imageCanal = pygame.image.load(img) # -> Surface
        self.imageCanal = pygame.transform.scale(self.imageCanal, (200,200))
        cor = fundocor[random.randint(0,len(fundocor)-1)]
        for i in range(25):
            time.sleep(1/60)
            screen.fill(fill)
            self.fundo = pygame.draw.rect(PY,cor,(10,10,500,250),border_radius=25)
            screen.blit(self.imageCanal,[i, 25])
            pygame.display.update()

    def textlines(self,TXT):
        text = []
        size = len(TXT)
        numero = 20
        numero = numero if size >= numero else size
        numerolinhas = size // numero if size // numero >= 1 else 1
        linhas = [["" for l in range(numero)] for l in range(numerolinhas)]
        c = 0
        for y in range(numerolinhas):
            for x in range(numero):
                linhas[y][x] = TXT[c]
                c+=1
            linhas[-1] = "".join(linhas[-1])
        return text
    
    def renderText(self,PY,Valor,mensagem,ImagURL,autor):
        self.GetImage(PY,ImagURL)
        fonts =pygame.font.get_fonts()
        idfont = 0#111#random.randint(0,len(fonts))
        fontuse = fonts[idfont]
        fonte_autor = pygame.font.SysFont(fontuse,30,False,False)
        #fonte_podium = pygame.font.SysFont(fontuse,60,True,False)
        font_Valor = pygame.font.SysFont(fontuse,60,True,False)
        #fonte_mensagem = pygame.font.SysFont(fontuse,30,False,False)
        dinheiro = f"{self.Configs["Voice"]["PrefixMoney"]} {Valor}"
        font_file = pygame.font.match_font("setofont")  # Select and 
        fonte_autor = pygame.font.Font(font_file, 30)          # open the font
        FormatedText_autor = fonte_autor.render(autor,True,(255,255,255))
        TextObject_autor =  screen.blit(FormatedText_autor,(250,50)) 
        FormatedText_valor = font_Valor.render(dinheiro,True,(255,255,255))
        TextObject_valor =  screen.blit(FormatedText_valor,(250,TextObject_autor.bottom))  
        '''
        menssagempermission = False
        if menssagempermission:
            t = type(mensagem)
            if t != dict:
                text =  self.textlines(mensagem)
                l = ""
                self.FormatedText_mensagem = fonte_mensagem.render(l,True,(255,255,255))
                self.TextObject_mensagem =  screen.blit(self.FormatedText_mensagem,(250,150))  
                c = self.TextObject_mensagem.bottom
                for l in text:
                    self.FormatedText_mensagem = fonte_mensagem.render(l,True,(255,255,255))
                    self.TextObject_mensagem =  screen.blit(self.FormatedText_mensagem,(250,c))  
                    c += self.TextObject_mensagem.height
        '''
    def show(self,PY,Valor,mensagem,autor,ImagURL):
        screen.fill(fill)
        self.renderText(PY,Valor,mensagem,ImagURL,autor)
        pygame.display.flip()
        self.som = inputSom
        prefixoautor = self.Configs["Voice"]["Prefix"]
        sulfixoautor = self.Configs["Voice"]["Sulfix"]
        moeda =  self.Configs["Voice"]["Money"]
        Final =  self.Configs["Voice"]["FinalMensage"]
        if self.som:
            fala = f"{prefixoautor}|{autor}|{sulfixoautor}|{Valor}|{moeda}"
            fala = fala+ f"|{mensagem}" if type(mensagem) != dict else fala
            fala = fala+ f"|{Final}"
            print(fala)
            nomemp3 = time.time()
            LinhadeFala = gtts.gTTS(text = fala.replace("|",","),lang = self.language,slow=False)
            LinhadeFala.save(f"{nomemp3}.mp3")
            pygame.mixer.music.load(f"{nomemp3}.mp3")
            pygame.mixer.music.play()
            gg = pygame.mixer.music.get_busy()
            while  gg:
                pygame.time.Clock().tick(10)
                pygame.event.poll()
                gg = pygame.mixer.music.get_busy()
            pygame.mixer.music.stop()
            time.sleep(0.5)



def hextorgb(HEXADECIMAL):
    r = int(HEXADECIMAL[:2],16)
    g = int(HEXADECIMAL[2:4],16)
    b = int(HEXADECIMAL[4:],16)
    return  r,g,b


DirApp = os.path.dirname(__file__)


if os.path.exists(f'{DirApp}\\python-3.13.0-amd64.exe'):
    os.remove(f'{DirApp}\\python-3.13.0-amd64.exe')

if os.path.exists(f"{DirApp}\\Configs.json") == False:
    Configsquivo = open(f"{DirApp}\\Configs.json","w")
    data={   "LiveId":"",
    "ReadText":True,
    "Language":"en",
    "Voice": {
        "Prefix":"yoooouuuu",
        "Sulfix":"donated",
        "PrefixMoney":"US$",
        "Money":"Dols",
        "FinalMensage":""
    },
    "ChromaKeyColor":"#00ff00",
    "Colors": [
        "#FAEA00",
        "#FA0041",
        "#00BCFA",
        "#A301FA",
        "#00FA79",
        "#FAA400",
        "#7E37A5",
        "#00F5B6",
        "#9535A0"]
}
    Configsquivo.write(json.dumps(data,indent = 8))
    Configsquivo.close()


Configsquivo = open(f"{DirApp}\\Configs.json","r")
Configs = json.load(Configsquivo)



fundocor = [hextorgb(c.replace("#","")) for c in Configs["Colors"]]

fill = hextorgb(Configs["ChromaKeyColor"].replace("#",""))
try:
    chat = pytchat.create(video_id=Configs["LiveId"])
except:
    chat = pytchat.create(video_id=input("Live Id: "))
    
inputSom = Configs["ReadText"]#False if input("Read text [S/N]: ").upper() == "N" else True

#######################################################################
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((550, 300))
pygame.display.set_icon(pygame.image.load(f'{DirApp}\\logo_ico.ico'))
pygame.display.set_caption('Youtube SuperChat Show')
running = chat.is_alive()

superchat = {}
Menassegam = Menassegam(Configs)
runningloop = True
while runningloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runningloop = False
       

    for message in chat.get().sync_items():
        M = message.__dict__
        if ("super" in M["type"]) == False:
            superchat[M["id"]] = M
        else:
            print(f"{message.author.name}")
        for SUPE in superchat:
            #print(f"{message.datetime} [{message.author.name}] - {message.messageEx[0]}")
            autor = superchat[SUPE]["author"].name
            Valor = superchat[SUPE]["amountValue"]
            mensagem = superchat[SUPE]["messageEx"][0]
            authoeId = superchat[SUPE]["author"].channelId
            ImagURL = superchat[SUPE]["author"].imageUrl
            ImagURL = ImagURL.split("=s")[0]
            Menassegam.show(screen,Valor,mensagem,autor,ImagURL)
        try:
            superchat.pop(SUPE)
        except:
            pass
        if len(superchat) == 0:
            screen.fill(fill)
    pygame.display.flip()
pygame.quit()