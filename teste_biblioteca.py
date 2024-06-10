import librosa
import matplotlib
import pyttsx3
import seaborn
import speech_recognition as sr
from playsound import playsound

# Abrir o assistente
#playsound('audio/n2.mp3')
# espostatt do assistente
# playsound('audio/n2.mp3')
# Som de error
# playsound('audio/n3.mp3')
print('librosa', librosa.__version__)
print('speech_recognition', sr.__version__)

# Inicializar pyttsx3
engine = pyttsx3.init()
engine.say('Testando a biblioteca que fala, Olá Maria')
engine.runAndWait()

print('Matplotlib',matplotlib.__version__)
print('seaborn', seaborn.__version__)

import pyaudio
print('Ola pyaudio')


