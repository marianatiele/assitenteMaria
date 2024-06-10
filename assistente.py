import pyttsx3
import pyttsx3
import librosa
import speech_recognition as sr
from playsound import playsound
import webbrowser as web
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
sns.set()
#Impostando o modelos
from modules import comandos_respostas, carrega_agenda

comandos = comandos_respostas.comandos

respostas = comandos_respostas.respostas

#print("Comandos", comandos)
#print('Respostas',  respostas)

nome_assitente = 'Maria'

path_to_opera = 'C:/Users/maria/AppData/Local/Programs/Opera/launcher.exe'

# Registre o navegador Opera
web.register('Opera',None, web.BackgroundBrowser(path_to_opera))
#Criando a função que abre o browser
def search(frase):
    url = 'https://www.google.com/search?q=' + frase
    web.get('opera').open(url)


#search('Quais são as possibilidades de chatbot, telegram, aplicações web, quais outras possibilidades')

# Sintetizador da voz
def texto_audio(audio):
    #essa função inicia o sintetizador, configura o volume e a velocidade do audio.
    engine = pyttsx3.init()
    engine.setProperty('rate',180)
    engine.setProperty('volume', 1)
    engine.say(audio)
    engine.runAndWait()

#texto_audio('Olá Maria, Como vai?')

#Reconhecer o mic, transformar o áduio em texto
def reconhece_mic():
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source, duration=0.8)
        print('Ouvindo')
        audio = mic.listen(source)
        #salvando o áudio
        with open('recordings/audio.wev', 'wb') as f:
            f.write(audio.get_raw_data())
    try:
        frase = mic.recognize_google(audio, language='pt-BR')
        print('voce disse'+ frase)

    except sr.UnknownValueError:
        frese = ''
        print('Não entendi.')

    return frase


reconhece_mic()