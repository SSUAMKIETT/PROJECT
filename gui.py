from tkinter import *
from chat import get_response
import pyttsx3 as pp
import speech_recognition as s
import threading

engine = pp.init()
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)
gui = Tk()
gui.geometry("500x500")
gui.title("CHATBOT")

def speak(word):
    engine.say(word)
    engine.runAndWait()

def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("listening")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognized")


def ask_from_bot():
    query = textF.get()
    answer_from_bot = get_response(query)
    msgs.insert(END, "you : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "Bot : " + str(answer_from_bot))
    pp.speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)


frame = Frame(gui)
sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()

# creating text field
textF = Entry(gui, font=("Times", 20))
textF.pack(fill=X, pady=10)
btn = Button(gui, text="Send", font=("Times", 15), command=ask_from_bot)
btn.pack()

# creating a function
def enter_function(event):
    btn.invoke()

# going to bind gui window with enter key...
gui.bind('<Return>', enter_function)

def repeatL():
    while True:
        takeQuery()

t = threading.Thread(target=repeatL)
t.start()
gui.mainloop()