import importlib.util
import sys

# Lista de módulos requeridos para el programa
required_modules = ['speech_recognition', 'pywhatkit', 'pyautogui', 'time', 'pyaudio']

# Verifica si los módulos requeridos están instalados
for module in required_modules:
    if importlib.util.find_spec(module) is None:
        print(f"El módulo '{module}' no está instalado. Por favor, instale todos los módulos requeridos para continuar.")
        sys.exit()

# Si todos los módulos están instalados, continúa con la ejecución del programa
import speech_recognition as sr
import pywhatkit
import pyautogui
import time

r = sr.Recognizer()
paused = False  # Variable que controla si el video está pausado o no

# Configura el dispositivo de entrada de audio
with sr.Microphone() as source:
    print("Di el nombre de la canción:")
    audio = r.listen(source)

# Reconoce el texto utilizando la API de Google Speech Recognition
try:
    song_name = r.recognize_google(audio)
    print(f"Reproduciendo {song_name}")
    # Utiliza pywhatkit para reproducir el video en YouTube
    pywhatkit.playonyt(song_name)

    # Agrega la funcionalidad de reconocimiento de comandos de voz
    while True:
        with sr.Microphone() as source:
            print("Di un comando:")
            audio = r.listen(source)
            try:
                command = r.recognize_google(audio, language='es-ES')
                print(f"Comando reconocido: {command}")

                if "pausa" in command.lower():
                    if not paused:  # Verifica si el video ya está pausado
                        pyautogui.keyDown('space')
                        time.sleep(0.1)
                        pyautogui.keyUp('space')
                        print("Reproducción en pausa")
                        paused = True  # Establece la variable de pausa como True
                    else:
                        print("El video ya está pausado")
                elif "reproducir" in command.lower():
                    if paused:  # Verifica si el video está pausado
                        pyautogui.keyDown('space')
                        time.sleep(0.1)
                        pyautogui.keyUp('space')
                        print(f"Reproduciendo {song_name}")
                        paused = False  # Establece la variable de pausa como False
                    else:
                        print("El video ya se está reproduciendo")
                elif "salir" in command.lower():
                    break
                else:
                    print("Comando no reconocido")
            except sr.UnknownValueError:
                print("No se pudo reconocer el audio")
            except sr.RequestError as e:
                print(
                    f"No se pudo conectar con el servicio de reconocimiento de voz; {e}")
except sr.UnknownValueError:
    print("No se pudo reconocer el audio")
except sr.RequestError as e:
    print(f"No se pudo conectar con el servicio de reconocimiento de voz; {e}")

