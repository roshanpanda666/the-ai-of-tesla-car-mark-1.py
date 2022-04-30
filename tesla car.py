while True:
    import os
    #........................................................................
    import pyttsx3 #the main module.........  not a pre build module        .
                                                #                           .
    engine=pyttsx3.init('sapi5')                #                           .
    voices=engine.getProperty('voices')  #david voice.........#             .
    engine.setProperty('voices',voices[0].id)#                              .
    #                                                                       ..... the code for speech output
    def speak(audio):                           #                           .
        engine.say(audio)                         #                         .
        engine.runAndWait() #speak code..........#                          .            
        return "None"                     #                                 . 
    # .......................................................................  


    name=input("enter your name")

    age=input("enter your age ")

    if(int(age)>18):

        speak("hello, "+name)
        speak("welcome to tesla, model 5xz")
        speak("type the password to start the engine ")
        pwd=input("enter the password here ::")
        if(pwd=="tesla"):
            speak("starting the engine, enjoy your ride")

            music_dir= "D:\songs"
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[5]))
            print("hello ",name,"starting the engine enjoy your ride")

        else:
            speak("enter the correct password")

    else:
        speak("you are under age to drive a car, "+name)
        
