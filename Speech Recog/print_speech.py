import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

word = ""

while word != "break":
    with m as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    print("Finished")
    word = r.recognize_sphinx(audio)
    print(word)