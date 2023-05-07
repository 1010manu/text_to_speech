import tkinter as tk
from gtts import gTTS
from playsound import playsound
Window=tk.Tk()
Window.title("Window")
Window.geometry("480x480")
Window.configure(background="Green")
lbl=tk.Label(Window,text="TEXT TO SPEECH",width=20,bg="black",fg="white",font=("Algerian",25,"bold"))
lbl.place(x=50,y=50)

def p1():
    a=text.get()
    lang="en"
    voice=gTTS(text=a,lang="en",slow=False)
    voice.save("voice.mp3")
    playsound("voice.mp3")
lbl=tk.Label(Window,text="text:",width=7,bg="red",fg="white",font=("Algerian",25,"bold"))
lbl.place(x=90,y=120)
text=tk.Entry(Window,text="",width=20,bg="white",fg="black")
text.place(x=250,y=130)
button=tk.Button(Window,text="Submit",command=p1,width=10,height=3,fg="purple",)
button.place(x=200,y=170)
Window.mainloop()
 
