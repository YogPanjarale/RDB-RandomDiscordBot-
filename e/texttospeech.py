import speech_recognition as sr
def mc():
    #Initialize the recognizer
    #The primary purpose of a Recognizer instance is, of course, to recognize speech. 
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 0.5
        #wait for a second to let the recognizer adjust the  
        #energy threshold based on the surrounding noise level 
        r.adjust_for_ambient_noise(source, duration=2)
        #listens for the user's input
        audio = r.listen(source)
        print("thinking...")
    try:
        command = r.recognize_google(audio)
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = mc()
        command = command.lower()

    return command

mc()