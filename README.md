# youtube-voice-control (BETA)
Control de reproducción de video en YouTube mediante reconocimiento de voz

Este es un programa en Python que utiliza el reconocimiento de voz para reproducir videos de YouTube y controlar la reproducción mediante comandos de voz. 
El programa permite pausar y reanudar la reproducción de video, y salir del programa.

![ejemplo1](https://user-images.githubusercontent.com/91538079/222335477-c77034d7-29d1-43c5-b381-fa84ffe55142.png)



- # Requerimientos

  El programa requiere los siguientes módulos de Python:

  ```speech_recognition```  para reconocimiento de voz.
  
  ```pywhatkit```           para reproducir videos de YouTube.
  
  ```pyautogui```           para controlar la reproducción de video en YouTube.
  
  ```time```                para agregar pequeñas pausas entre las acciones del programa.
  
  ```pyaudio```             para configurar el dispositivo de entrada de audio.
  
  Si no funciona, intente instalar todas las bibliotecas que se encuentran en el archivo requisitos.txt


- # Instalación
  Para instalar los módulos requeridos, puede ejecutar el siguiente comando en una terminal:
  
  Primero descargue la herramienta.

```
git clone https://github.com/Cedaleon/youtube-voice-control.git
cd youtube-voice-control
python youtube_voice_control.py
```

  ```
  pip install speech_recognition pywhatkit pyautogui pyaudio
  ```

- # USO
  Para utilizar el programa, ejecute el archivo youtube_voice_control.py en una terminal. El programa le pedirá que diga el nombre de la canción que desea reproducir.   Luego, puede controlar la reproducción del video mediante los siguientes comandos de voz:

  "pausa": para pausar la reproducción del video.
  "reproducir": para reanudar la reproducción del video.
  "salir": para salir del programa.

- # Ejemplo

  ```
  $ python youtube_voice_control.py
  ```
  
  Di el nombre de la canción:
  Imagine Dragons Believer
  
  Reproduciendo Imagine Dragons Believer
  
  Di un comando:
  pausa
  
  Reproducción en pausa
  
  Di un comando:
 
  salir

- # Creditos
  Este programa fue creado por [Cedaleon] con fines educativos. El código está disponible en https://github.com/Cedaleon.
