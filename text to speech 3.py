from gtts import gTTS
from playsound import playsound
text=input("enter the text:")
lang="en"
voice=gTTS(text=text,lang="en",slow=False)
voice.save("voice.mp3")
playsound("voice.mp3")
