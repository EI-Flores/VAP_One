import pyttsx3 
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser as wb 
import os
import pyautogui
import psutil
import pyjokes 


engine = pyttsx3.init()
voices = engine.getProperty('voices')
# For female voice 0, male voice 1
engine.setProperty('voice', voices[0].id)
# Rate
newVoiceRate = 150
engine.setProperty('rate', newVoiceRate)

r = sr.Recognizer()
m = sr.Microphone()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime('%Y-%m-%d')
    speak("La fecha actual es")
    speak(Time)

def date():
    # For only numbers of date
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("La fecha actual es")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Operativo y en línea. Bienvenido de vuelta usuario Juan Arturo!")
    #time()
    hour = int(datetime.datetime.now().hour)

    if hour >= 6 and hour < 12:
        speak("Buenos días")
    elif hour >=12 and hour < 18:
        speak("Buenas tardes")
    else:
        speak("Buenas noches")
    speak("¿Cómo te puedo apoyar?")

def takeCommand():
    r = sr.Recognizer()
    with m as source:
        print("Escuchando...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Reconociendo...")
        # chk your language/country code HERE : https://cloud.google.com/speech-to-text/docs/languages
        value = r.recognize_google(audio, "es-MX")
        print(value)

    except Exception as e:
        print(e)
        speak("¿Puede repetir la orden por favor?")
    
        return "None"
    
    return value

def mandarmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("ing.flores.rivera@gmail.com", "1233Test")
    server.sendmail("ing.flores.rivera@gmail.com", to, content)
    server.close()

def screenshot():
    img =pyautogui.screenshot()
    img.save("URL a guardar")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU usado al" + usage + "%")

    battery = psutil.sensors_battery()
    speak("Batería está al")
    speak(battery.percent) 
    speak("%") 

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishme()

    while True:

        print("Le escucho")
        speak("Le escucho")
        with m as source: audio = r.listen(source)
        print("Lo tengo, realizo instrucción...")

        try:
            value = r.recognize_google(audio)

            if value == "fecha":
                print("Dijiste {}".format(value))
                time()
                
            
            elif value == "fecha numérica":
                print("Dijiste {}".format(value))
                date()
            
            elif value == "adios":
                print("Dijiste {}".format(value))
                quit()
            
            elif value == "wikipedia":
                print("Dijiste {}".format(value))
                speak("Buscando...")
                value = value.replace("wikipedia", "")
                result = wikipedia.summary(value, sentences = 2)
                speak(result)
            
            elif value == "enviar email":
                try:
                    speak("¿Que deseas decir?")
                    content = takeCommand()
                    to = "ing.flores.rivera@gmail.com"
                    #sendmail(to, content)
                    speak(content)
                    speak("Correo enviado!")
                except Exception as e:
                    speak(e)
                    speak("No se envió correo")
            
            elif value == "buscar en el navegador":
                speak("¿Qué deseas buscar?")
                chromepath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe %s"
                seach = takeCommand().lower()
                wb.get(chromepath).open_new_tab(search + ".com")
            
            elif value == "cerrar sesión":
                os.system("shutdown -l")
            
            elif value == "Apagar equipo":
                os.system("shutdown /s /t 1")
            
            elif value == "reiniciar":
                os.system("shutdown /r /t 1")
            
            elif value == "Reproducir camción":
                songs_dir = "URL"
                songs = os.listdir(songs_dir)
                os.startfile(os.path.join(songs_dir, songs[0]))
            
            elif value == "recuerda pendiente":
                print("Dijiste {}".format(value))
                speak("¿Qué debo recordar?")
                date = takeCommand()
                speak("Dime lo que debo recordar" + data)
                remember = open("data.txt", "w")
                remember.write(data)
                remember.close()
            
            elif value == "¿Hay pendientes?":
                print("Dijiste {}".format(value))
                remember = open("data.txt", "r")
                speak("Tienes de recordatorio" + remember.read())

            elif "captura pantalla" in value:
                screenshot()
                speak("Captura de pantalla hecha")
            
            elif value == "estado computadora":
                print("Dijiste {}".format(value))
                cpu()
            
            elif value == "chiste":
                jokes()
        
        except sr.UnknownValueError:
            print("No entendí lo que quisiste decir")
            speak("No entendí lo que quisiste decir")
        
        except sr.RequestError as e:
            print("No encontré resultados del Servicio de reconocimiento de voz de Google; {0}".format(e))

        
