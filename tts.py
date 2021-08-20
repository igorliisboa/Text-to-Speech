#pip install gtts
from gtts import gTTS
import os

fh = open("text.txt","r")

text = fh.read().replace("\n"," ")

lang = "pt-br" #Escolha o idioma

output = gTTS(text=text,lang=lang,slow=False)

output.save("text.mp3") #Arquivo para salvar

os.system("start text.mp3")