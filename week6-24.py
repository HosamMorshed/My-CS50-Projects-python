import speech_recognition as spr
rec =spr.Recognizer()

with spr.Microphone() as src:
    print("say something ....")
    audio =rec.listen(src)
    text = rec.recognize_google(audio)

print(text)


