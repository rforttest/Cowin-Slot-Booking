import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(line,rate=130):
    engine.say(line)
    engine.runAndWait()
    engine.setProperty('rate',rate)

if __name__ == '__main__':
    speak("This IS For Testing")