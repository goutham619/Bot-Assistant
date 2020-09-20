import os
import speech_recognition as sr
from tkinter import *
from tkinter.ttk import Progressbar
import time
import threading
from datetime import datetime
from datetime import date


class MonApp(Tk):
    n = 0
    while n < 100:

        def __init__(self):
            super().__init__()
            self.title("Bot Assistant")
            self.configure()
            self.geometry("500x500")
            self.btn1 = Button(self, text='click and speak', bg="#F9F624", command=self.traitement)
            self.btn1.place(x=205, y=250)
            label1 = Label(self, text="BOT ASSISTANT", relief='solid', bg="#48EDD6", width=20,
                           font=("arial", 16, "bold"))
            label1.place(x=90, y=53)
            label2 = Label(self, text="Developed by Goutham", relief='solid', bg="#48EDD6", width=32,
                           font=("arial", 16, "bold"))
            label2.place(x=9, y=415)
            label3 = Label(self, text="Copyrights reserved © 2020", relief='solid', bg="#48EDD6", width=32,
                           font=("arial", 16, "bold"))
            label3.place(x=9, y=450)
            self.progress = Progressbar(self, orient=HORIZONTAL, length=1000, mode='indeterminate')

        def traitement(self):

            def real_traitement():
                self.progress.grid(row=5000, column=0)

                # Record Audio
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    r.dynamic_energy_threshold = False
                    r.energy_threshold = 400
                    print("Say something!")
                    audio = r.listen(source, timeout=5.0)

                # Speech recognition using Google Speech Recognition
                try:
                    # for testing purposes, we're just using the default API key
                    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                    # instead of `r.recognize_google(audio)`
                    voice = r.recognize_google(audio)
                    print("You said: " + voice)
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))

                self.progress.start()
                time.sleep(5)
                self.progress.stop()
                self.progress.grid_forget()

                t = voice
                a = t.lower()
                b = a.split(" ")

                if a == "what is my ip":
                    os.system('ipconfig|findstr IPv4')

                elif a == "what is my mac":
                    os.system("ipconfig/all | findstr Physical")

                elif b[0] == "open":
                    # open chrome
                    os.system("start " + b[1])

                elif b[0] == "ping":
                    # ping ip
                    ip = b[1]
                    os.system("ping " + ip)

                elif b[0] == "go":
                    # go to eg.c drive*
                    c = b[2].upper()
                    os.system("start " + c + ":/")

                elif b[0] == "search":
                    # search for eg.hello
                    f = b[1:]
                    st = " ".join(f)
                    os.system("start chrome google.com/search?q={}".format(st))

                elif a == "what is today's date":
                    today = date.today()
                    print("Today's date:", today)

                elif a == "what's the time":
                    now = datetime.now()
                    dt_string = now.strftime(" %H:%M:%S")
                    print("time =", dt_string)

                elif a == "what is today's whether":
                    os.system("start chrome google.com/search?q=today+weather ")

                elif a == "close bot assistant":
                    print("Thank you for using bot assistant")
                    self.destroy()

                elif a == "shutdown":
                    os.system("shutdown/s")
                    print("your system will be switched off in a minute ")

                elif a == "abort shutdown":
                    os.system("shutdown/a")

                elif a == "restart":
                    os.system("shutdown/r")

                elif a == "log off":
                    os.system("shutdown/l")

                elif a == "turn wi-fi on":
                    # administrator permission
                    os.system("netsh interface set interface Wi-Fi enabled")

                elif a == "turn wi-fi off":
                    # administrator permission
                    os.system("netsh interface set interface Wi-Fi disabled")

                else:
                    print("Bot Assistant can't recognize this command at this movement")
                    print("Please try again")

                self.btn1['state'] = 'normal'

            self.btn1['state'] = 'disabled'
            threading.Thread(target=real_traitement).start()

        n = n + 1


if __name__ == '__main__':
    app = MonApp()
    app.mainloop()
